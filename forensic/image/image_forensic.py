#!/usr/bin/env python3

import os
import sys
import subprocess
import shutil
from tkinter import Tk, filedialog
from termcolor import colored

# Function to install system packages using apt
def install_system_package(package):
    try:
        subprocess.run(["sudo", "apt", "install", "-y", package], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(colored(f"[+] Installed system package: {package}", "green"))
        return True
    except subprocess.CalledProcessError:
        print(colored(f"[!] Failed to install system package: {package}", "red"))
        return False

# Function to install Python packages using pip
def install_python_package(package):
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", package], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(colored(f"[+] Installed Python package: {package}", "green"))
        return True
    except subprocess.CalledProcessError:
        print(colored(f"[!] Failed to install Python package: {package}", "red"))
        return False

# Check and install required packages
def install_requirements():
    system_packages = ["exiftool", "binwalk", "steghide", "foremost", "python3-tk"]
    python_packages = ["termcolor", "Pillow"]

    missing_system_packages = [pkg for pkg in system_packages if shutil.which(pkg) is None]
    for package in missing_system_packages:
        print(colored(f"[!] Missing system requirement '{package}'. Installing...", "red"))
        install_system_package(package)

    for package in python_packages:
        try:
            __import__(package)
        except ImportError:
            print(colored(f"[!] Python package '{package}' is missing. Installing...", "red"))
            install_python_package(package)

# File selection dialog
def select_image_file():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Select an image file",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.gif *.tiff *.ps *.webp")]
    )
    return file_path

# Save results to file with user confirmation
def save_results(results, default_filename):
    save = input(colored("Would you like to save the results? (y/n): ", "yellow")).strip().lower()
    if save == 'y':
        with open(default_filename, "w") as file:
            file.write(results)
        print(colored(f"[+] Results saved to {default_filename}", "green"))

# Menu display
def show_menu():
    print(colored("🦑 Fast Image Forensic Analyzer", "yellow"))
    print(colored("""
                          ,######,            ,######,
                           ,##*##,  ,######,  ,##*##,
                   ,,##(,    ,###.,##########,,###,    ,(##,,
                  ,######/  ,###,.###########.,###,  *######,
                   ,*(,###. ,###.,############,,###,  ###,(/,
                      ,###.,###/ .## * ## * ##, (###. ###,
                      ,###,,###,   ##########,  *###, ###,
               ,,,,,  ,###,,####,.,#########(,,,####,,###,  .,,,,
             ,#######,,####,,######################,,####,*#######,
             ,####,##########################################,####,
               *################*Image Forensic*################*
                     ,####################################,
                       ,*########,,####(#####,,########*,
                    ,###############p,     ,i###############,
                   ,###,,,########*s,       ,p#########,,,###,
                   ,####, ,  ...                     /####,,,
             | | | | \ | |  _ \| ____|  _ \ / ___/ _ \|  _ \| ____|
             | | | |  \| | | | |  _| | |_) | |  | | | | | | |  _|
             | |_| | |\  | |_| | |___|  _ <| |__| |_| | |_| | |___
              \___/|_| \_|____/|_____|_| \_ \____\___/|____/|_____|
    """, "white"))

    print(colored("1. Extract Metadata (ExifTool)", "green"))
    print(colored("2. Analyze for Hidden Files (Binwalk)", "green"))
    print(colored("3. Extract Hidden Data (Steghide)", "green"))
    print(colored("4. Recover Deleted Files (Foremost)", "green"))
    print(colored("5. Perform Error Level Analysis (ELA)", "green"))
 #  print(colored("6. Full Forensic Analysis (All Tools)", "blue", "on_white"))
    print(colored("6. Full Forensic Analysis (All Tools)", "blue", "on_white", attrs=['bold']))
    print(colored("7. Exit", "red"))
    return input(colored("Select an option: ", "yellow"))

# Extract metadata
def extract_metadata(image_path):
    result = subprocess.run(["exiftool", image_path], capture_output=True, text=True)
    return result.stdout if result.returncode == 0 else None

# Analyze for hidden files
def analyze_hidden_files(image_path):
    result = subprocess.run(["binwalk", image_path], capture_output=True, text=True)
    return result.stdout if result.returncode == 0 else None

# Extract hidden data
def extract_hidden_data(image_path):
    passphrase = input(colored("Enter passphrase (leave blank if none): ", "yellow")).strip()
    command = ["steghide", "extract", "-sf", image_path]
    if passphrase:
        command += ["-p", passphrase]
    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=10)
        return result.stdout if result.returncode == 0 else None
    except subprocess.TimeoutExpired:
        print(colored("[!] Steghide operation timed out.", "red"))
        return None

# Recover deleted files
def recover_deleted_files(image_path):
    output_dir = f"{image_path}_recovered"
    shutil.rmtree(output_dir, ignore_errors=True)
    result = subprocess.run(["foremost", "-i", image_path, "-o", output_dir], capture_output=True, text=True)
    return f"Recovered files saved to {output_dir}" if result.returncode == 0 and os.listdir(output_dir) else None

# Error Level Analysis
def perform_ela(image_path):
    from PIL import Image, ImageChops
    ela_path = f"{image_path}_ela.png"
    image = Image.open(image_path)
    ela_image = ImageChops.difference(image, image.convert('RGB'))
    ela_image.save(ela_path)
    return f"ELA image saved to {ela_path}"

# Full forensic analysis
def full_forensic_analysis(image_path):
    results = []
    results.append("=== Metadata ===")
    metadata = extract_metadata(image_path)
    if metadata: results.append(metadata)

    results.append("=== Hidden Files ===")
    hidden_files = analyze_hidden_files(image_path)
    if hidden_files: results.append(hidden_files)

    results.append("=== Hidden Data ===")
    hidden_data = extract_hidden_data(image_path)
    if hidden_data: results.append(hidden_data)

    results.append("=== Recovered Files ===")
    recovered_files = recover_deleted_files(image_path)
    if recovered_files: results.append(recovered_files)

    results.append("=== Error Level Analysis ===")
    ela_results = perform_ela(image_path)
    if ela_results: results.append(ela_results)

    return "\n".join(results)

# Main logic
def main():
    install_requirements()
    while True:
        choice = show_menu()
        if choice == "7":
            print(colored("Exiting program. Goodbye!", "yellow"))
            break

        image_path = select_image_file()
        if not image_path:
            print(colored("[!] No file selected. Returning to menu...", "red"))
            continue

        if choice == "1":
            results = extract_metadata(image_path)
        elif choice == "2":
            results = analyze_hidden_files(image_path)
        elif choice == "3":
            results = extract_hidden_data(image_path)
        elif choice == "4":
            results = recover_deleted_files(image_path)
        elif choice == "5":
            results = perform_ela(image_path)
        elif choice == "6":
            results = full_forensic_analysis(image_path)
        else:
            print(colored("[!] Invalid option. Try again.", "red"))
            continue

        if results:
            print(results)
            save_results(results, "forensic_report.txt")

if __name__ == "__main__":
    main()

#Join Our Telegram: T.me/UndercodeCommunity (Hacking Tutorials & Tips, Cyber & Tech News, CVE)
