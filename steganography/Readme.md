# Advanced Steganography Suite 🔐

**Hide and extract secret data within images with military-grade security**
A professional steganography solution for secure data embedding in image files with encryption, compression, and advanced validation.

---

## ✨ Features

- **Auto-Dependency Management** - Script automatically checks and guides installation of required packages
- **AES-256 Encryption** - Military-grade data protection
- **Smart Compression** - zlib optimization for maximum payload
- **Adaptive Steganography** - 1-4 bit LSB embedding with auto-configuration
- **Cross-Platform** - Windows/macOS/Linux support

---

## 🚀 Installation & Setup

```bash
# Clone repository
git clone https://github.com/UndercodeUtilities/accesslist
cd accesslist/steganography

# Run tool (Auto-checks dependencies😁)
python crystego.py
```

*The script will automatically:*
1. Verify required packages (Pillow, PyCryptodome, Colorama, tqdm)
2. Guide you to install any missing dependencies
3. Launch the intuitive console interface

---

## 🌈 Supported Formats

| Category        | Supported Formats                                                                 |
|-----------------|-----------------------------------------------------------------------------------|
| **Cover Images** | PNG, BMP, TIFF (lossless formats only)                                           |
| **Secret Files** | Any file type/extension                                                          |
| **Output Files** | PNG (preserves alpha channel transparency)                                       |

---

## 🔧 Technical Specifications

### Embedding Architecture
- **Method**: Adaptive LSB (Least Significant Bit) Steganography
- **Bit Depth**: Configurable 1-4 bits per color channel
- **Header Structure**:
  ```
  128-bit SHA3-256 Hash |
  256-bit AES Initialization Vector |
  64-bit Data Size Header
  ```

### Security Framework
- **Encryption**: AES-256-CBC with PBKDF2 key derivation
- **Compression**: zlib Level 9 optimization
- **Integrity Checks**: Dual-layer SHA3-256 + CRC32 validation

### Capacity Calculator
**Maximum Payload Size**:
```python
(Image_Width × Image_Height × 3 × Bits_Per_Channel) / 8 - 256_byte_header
```

---

> **⚠️ Legal Disclaimer**
> This tool is intended for:
> - Privacy protection research
> - Ethical security testing
> - Educational purposes
>
> **Always**:
> - Obtain proper authorization before use
> - Comply with local cyberlaws (GDPR, HIPAA, CCPA, etc.)
> - Never engage in illegal data concealment

