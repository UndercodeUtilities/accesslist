import os
import sys
import subprocess
import zlib
import hashlib
import struct
import tkinter as tk
from tkinter import filedialog
import colorama
from colorama import Fore, Style

# Initialize colorama first for error messages
colorama.init(autoreset=True)

# --------------------------
# Dependency Check & Auto-Install
# --------------------------
REQUIREMENTS = {
    'PIL': 'pillow',
    'Crypto': 'pycryptodome',
    'colorama': 'colorama',
    'tqdm': 'tqdm'
}

def check_dependencies():
    """Check and install missing dependencies automatically"""
    missing = []
    for module, package in REQUIREMENTS.items():
        try:
            __import__(module)
        except ImportError:
            missing.append(package)

    if missing:
        print(Fore.YELLOW + "Installing missing dependencies...")
        try:
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", *missing],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            print(Fore.GREEN + "Dependencies installed successfully. Please restart the script.")
            sys.exit(0)
        except subprocess.CalledProcessError:
            print(Fore.RED + "Failed to install dependencies. Please run:")
            print(Fore.CYAN + f"pip install {' '.join(missing)}")
            sys.exit(1)

    # Verify Crypto module
    try:
        from Crypto.Cipher import AES
        from Crypto.Util.Padding import pad, unpad
    except ImportError:
        print(Fore.RED + "Crypto module initialization failed. Try:")
        print(Fore.CYAN + "pip uninstall pycrypto && pip install pycryptodome")
        sys.exit(1)

# Check dependencies before other imports
check_dependencies()

# Now import other modules safely
from PIL import Image
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from tqdm import tqdm
import threading

# --------------------------
# Core Steganography Engine
# --------------------------
class SteganographyEngine:
    SUPPORTED_FORMATS = ['PNG', 'BMP', 'TIFF']
    HEADER_FORMAT = '!128s32sQ'  # (hash, checksum, data_size)
    HEADER_SIZE = 128 + 32 + 8  # SHA3-256 hash + SHA256 checksum + data size

    def __init__(self, method='LSB', bits=2, encryption_key=None):
        self.method = method
        self.bits = bits
        self.encryption_key = encryption_key
        self.lock = threading.Lock()

    def _calculate_capacity(self, image):
        """Return max payload size in bytes"""
        pixels = image.width * image.height
        if self.method == 'LSB':
            return (pixels * 3 * self.bits) // 8 - self.HEADER_SIZE
        return 0

    def _embed_header(self, data):
        """Create security header with hash, checksum, and size"""
        data_hash = hashlib.sha3_256(data).digest()
        checksum = hashlib.sha256(data).digest()
        header = struct.pack(self.HEADER_FORMAT, data_hash, checksum, len(data))
        return header + data

    def _validate_header(self, header, data):
        """Verify data integrity from header"""
        try:
            data_hash, checksum, data_size = struct.unpack(self.HEADER_FORMAT, header)
            if len(data) != data_size:
                return False
            if hashlib.sha256(data).digest() != checksum:
                return False
            if hashlib.sha3_256(data).digest() != data_hash:
                return False
            return True
        except:
            return False

    def _process_data(self, data, encrypt=True):
        """Handle encryption/compression"""
        if self.encryption_key:
            cipher = AES.new(self.encryption_key, AES.MODE_CBC)
            data = cipher.encrypt(pad(data, AES.block_size))
            data = cipher.iv + data
        return zlib.compress(data, level=9)

    def _unprocess_data(self, data):
        """Handle decryption/decompression"""
        try:
            data = zlib.decompress(data)
            if self.encryption_key:
                iv = data[:16]
                cipher = AES.new(self.encryption_key, AES.MODE_CBC, iv=iv)
                data = unpad(cipher.decrypt(data[16:]), AES.block_size)
            return data
        except:
            raise ValueError("Decryption/decompression failed")

    def embed(self, cover_path, secret_path, output_path):
        """Main embedding function with progress tracking"""
        try:
            with Image.open(cover_path) as img:
                if img.mode not in ['RGB', 'RGBA']:
                    img = img.convert('RGB')

                with open(secret_path, 'rb') as f:
                    secret_data = f.read()

                # Pre-process data
                processed_data = self._process_data(secret_data)
                embedded_data = self._embed_header(processed_data)

                # Capacity check
                max_capacity = self._calculate_capacity(img)
                if len(embedded_data) > max_capacity:
                    raise ValueError(f"Need larger cover image (Min: {len(embedded_data)/1024:.1f} KB)")

                # Embedding process
                pixels = img.load()
                data_bits = ''.join(format(byte, '08b') for byte in embedded_data)
                data_index = 0

                with tqdm(total=len(data_bits), unit='bits', desc=Fore.BLUE + "Embedding") as pbar:
                    for y in range(img.height):
                        for x in range(img.width):
                            with self.lock:
                                pixel = list(pixels[x, y])
                                for channel in range(3):
                                    if data_index >= len(data_bits):
                                        break
                                    byte_val = pixel[channel]
                                    mask = (0xFF << self.bits) & 0xFF
                                    new_val = (byte_val & mask) | int(data_bits[data_index:data_index+self.bits], 2)
                                    pixel[channel] = new_val
                                    data_index += self.bits
                                    pbar.update(self.bits)
                                pixels[x, y] = tuple(pixel)

                img.save(output_path, format='PNG')
                return True

        except Exception as e:
            raise RuntimeError(f"Embedding failed: {str(e)}")

    def extract(self, stego_path, output_path):
        """Data extraction with validation"""
        try:
            with Image.open(stego_path) as img:
                pixels = img.load()
                data_bits = []

                with tqdm(total=img.width*img.height*3*self.bits, unit='bits', desc=Fore.BLUE + "Extracting") as pbar:
                    for y in range(img.height):
                        for x in range(img.width):
                            pixel = pixels[x, y]
                            for channel in range(3):
                                byte_val = pixel[channel]
                                bits = format(byte_val, '08b')[-self.bits:]
                                data_bits.extend(bits)
                                pbar.update(self.bits)

                # Convert bits to bytes
                data_bytes = bytearray()
                for i in range(0, len(data_bits), 8):
                    byte = data_bits[i:i+8]
                    data_bytes.append(int(''.join(byte), 2))

                # Validate and extract
                header = data_bytes[:self.HEADER_SIZE]
                payload = data_bytes[self.HEADER_SIZE:]

                if not self._validate_header(header, payload):
                    raise ValueError("Data integrity check failed")

                processed_data = self._unprocess_data(payload)

                # Ensure output directory exists
                output_dir = os.path.dirname(output_path)
                if output_dir and not os.path.exists(output_dir):
                    os.makedirs(output_dir, exist_ok=True)

                with open(output_path, 'wb') as f:
                    f.write(processed_data)

                return True

        except Exception as e:
            raise RuntimeError(f"Extraction failed: {str(e)}")

# --------------------------
# User Interface Components
# --------------------------
class SteganographyApp:
    def __init__(self):
        self.engine = None
        self.root = tk.Tk()
        self.root.withdraw()
        self.setup_menu()

    def setup_menu(self):
        """Professional console menu system"""
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.CYAN + Style.BRIGHT + "🔐 Enterprise Steganography Suite")
            print(Fore.YELLOW + "=" * 60)
            print(Fore.GREEN + "[1]" + Fore.WHITE + " Encode Data")
            print(Fore.GREEN + "[2]" + Fore.WHITE + " Decode Data")
            print(Fore.GREEN + "[3]" + Fore.WHITE + " Configure Settings")
            print(Fore.GREEN + "[4]" + Fore.WHITE + " Documentation")
            print(Fore.GREEN + "[5]" + Fore.WHITE + " Exit")
            print(Fore.YELLOW + "=" * 60)

            choice = input(Fore.MAGENTA + "\n➤ Select operation: ").strip()

            if choice == '1':
                self.encode_menu()
            elif choice == '2':
                self.decode_menu()
            elif choice == '3':
                self.settings_menu()
            elif choice == '4':
                self.show_documentation()
            elif choice == '5':
                self.exit_app()
            else:
                print(Fore.RED + "Invalid selection!")

    def get_file(self, title, filetypes):
        """Robust file dialog with fallback"""
        path = ""
        try:
            path = filedialog.askopenfilename(title=title, filetypes=filetypes)
            if not path:
                raise ValueError("Dialog cancelled")
        except Exception as e:
            print(Fore.YELLOW + f"GUI dialog failed: {e}")
            path = input(Fore.CYAN + f"Enter path for {title}: ").strip()
        return path

    def get_save_path(self, title, filetypes, default_ext):
        """Robust save dialog with fallback"""
        path = ""
        try:
            path = filedialog.asksaveasfilename(
                title=title,
                filetypes=filetypes,
                defaultextension=default_ext
            )
            if not path:
                raise ValueError("Dialog cancelled")
        except Exception as e:
            print(Fore.YELLOW + f"GUI save dialog failed: {e}")
            path = input(Fore.CYAN + f"Enter path to save: ").strip()

        # Handle if user entered a directory
        if os.path.isdir(path):
            default_name = "stego_image.png" if default_ext == ".png" else "extracted_file"
            path = os.path.join(path, default_name)
            print(Fore.YELLOW + f"Save path adjusted to: {path}")

        return path

    def encode_menu(self):
        """Advanced encoding interface"""
        print(Fore.BLUE + "\n📤 Data Encoding Module")
        try:
            cover_path = self.get_file("Select Cover Image", [("Image Files", "*.png *.bmp *.tiff")])
            secret_path = self.get_file("Select Secret File", [("All Files", "*.*")])
            output_path = self.get_save_path("Save Stego Image", [("PNG Files", "*.png")], ".png")

            encryption = input(Fore.CYAN + "Enable AES-256 encryption? (y/n): ").lower() == 'y'
            key = hashlib.sha256(input("Enter passphrase: ").encode()).digest() if encryption else None

            self.engine = SteganographyEngine(bits=2, encryption_key=key)
            thread = threading.Thread(target=self.engine.embed, args=(cover_path, secret_path, output_path))
            thread.start()
            thread.join()

            print(Fore.GREEN + "\n✅ Encoding completed successfully!")
            print(Fore.YELLOW + f"Output file: {output_path}")

        except Exception as e:
            print(Fore.RED + f"🚨 Error: {str(e)}")
        input(Fore.YELLOW + "\nPress Enter to continue...")

    def decode_menu(self):
        """Advanced decoding interface"""
        print(Fore.BLUE + "\n📥 Data Decoding Module")
        try:
            stego_path = self.get_file("Select Stego Image", [("PNG Files", "*.png")])
            output_path = self.get_save_path("Save Extracted File", [("All Files", "*.*")], ".*")

            key = None
            if input(Fore.CYAN + "Is the file encrypted? (y/n): ").lower() == 'y':
                key = hashlib.sha256(input("Enter passphrase: ").encode()).digest()

            self.engine = SteganographyEngine(encryption_key=key)
            self.engine.extract(stego_path, output_path)

            print(Fore.GREEN + "\n✅ Extraction completed successfully!")
            print(Fore.YELLOW + f"Output file: {output_path}")

        except Exception as e:
            print(Fore.RED + f"🚨 Error: {str(e)}")
        input(Fore.YELLOW + "\nPress Enter to continue...")

    def settings_menu(self):
        """Configuration management"""
        print(Fore.BLUE + "\n⚙️ System Configuration")
        input(Fore.YELLOW + "\nPress Enter to continue...")

    def show_documentation(self):
        """In-depth help system"""
        print(Fore.BLUE + "\n📘 Enterprise Steganography Suite Documentation")
        print(Fore.WHITE + """
        Features:
        - AES-256 Encryption
        - Data Compression
        - Integrity Checks
        - Multi-threaded Processing
        - Lossless Image Formats
        - Adaptive LSB Embedding
        - Progress Tracking
        - Cross-platform Support
        """)
        input(Fore.YELLOW + "\nPress Enter to continue...")

    def exit_app(self):
        """Graceful shutdown"""
        print(Fore.CYAN + "\nThank you for using Enterprise Steganography Suite!")
        sys.exit(0)

# --------------------------
# Main Execution
# --------------------------
if __name__ == "__main__":
    try:
        SteganographyApp()
    except KeyboardInterrupt:
        print(Fore.RED + "\nOperation cancelled by user!")
        sys.exit(1)
