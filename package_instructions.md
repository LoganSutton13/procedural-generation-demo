# Packaging Instructions for Procedural Generation Demo

This guide explains how to package the Procedural Generation Demo into a standalone executable that can run on any Windows machine without requiring Python installation.

## Quick Start

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the build script**:
   ```bash
   python build_exe.py
   ```

3. **Install the application**:
   - Run `install.bat` to install to your desktop
   - Or run `dist/ProceduralGenerationDemo.exe` directly

## What Gets Created

After running the build script, you'll have:

- `dist/ProceduralGenerationDemo.exe` - The standalone executable
- `install.bat` - Simple installer script
- `icon.ico` - Application icon (if PIL is available)

## Manual Build Process

If you prefer to build manually:

### 1. Install PyInstaller
```bash
pip install pyinstaller>=5.0.0
```

### 2. Create the Executable
```bash
pyinstaller --onefile --windowed --name=ProceduralGenerationDemo --clean main.py
```

### 3. Test the Executable
```bash
dist/ProceduralGenerationDemo.exe
```

## Advanced Build Options

### With Custom Icon
```bash
pyinstaller --onefile --windowed --name=ProceduralGenerationDemo --icon=your_icon.ico main.py
```

### With Additional Files
```bash
pyinstaller --onefile --windowed --name=ProceduralGenerationDemo --add-data=README.md;. main.py
```

### Debug Build (with console)
```bash
pyinstaller --onefile --name=ProceduralGenerationDemo main.py
```

## Distribution

### Single File Distribution
The `--onefile` option creates a single executable that contains everything needed to run the application. Users can simply double-click the `.exe` file.

### Folder Distribution
If you want to distribute as a folder (faster startup):
```bash
pyinstaller --onedir --windowed --name=ProceduralGenerationDemo main.py
```

## Troubleshooting

### Common Issues

1. **"Missing module" errors**
   - Add `--hidden-import=module_name` to the PyInstaller command
   - Example: `--hidden-import=pygame --hidden-import=perlin_noise`

2. **Large executable size**
   - The executable includes Python runtime and all dependencies
   - Typical size: 50-100 MB
   - Use `--onedir` instead of `--onefile` for smaller size

3. **Antivirus false positives**
   - Some antivirus software may flag PyInstaller executables
   - This is a known issue with PyInstaller
   - You may need to add an exception or sign the executable

4. **Performance issues**
   - The first startup may be slower due to unpacking
   - Subsequent runs will be faster

### File Size Optimization

To reduce executable size:

1. **Use --onedir instead of --onefile**:
   ```bash
   pyinstaller --onedir --windowed --name=ProceduralGenerationDemo main.py
   ```

2. **Exclude unnecessary modules**:
   ```bash
   pyinstaller --onefile --windowed --exclude-module=matplotlib --exclude-module=numpy main.py
   ```

3. **Use UPX compression** (if available):
   ```bash
   pyinstaller --onefile --windowed --upx-dir=path/to/upx main.py
   ```

## Cross-Platform Building

### Building for Different Platforms

- **Windows**: Build on Windows
- **macOS**: Build on macOS
- **Linux**: Build on Linux

### Docker Build (for Linux/macOS from Windows)

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt
RUN pyinstaller --onefile --windowed main.py

# The executable will be in dist/
```

## Code Signing (Optional)

For production distribution, consider code signing:

1. **Get a code signing certificate**
2. **Sign the executable**:
   ```bash
   signtool sign /f certificate.pfx /p password dist/ProceduralGenerationDemo.exe
   ```

## Version Information

Add version information to the executable:

```bash
pyinstaller --onefile --windowed --version-file=version.txt main.py
```

Create `version.txt`:
```
VSVersionInfo(
  ffi=FixedFileInfo(
    filevers=(1, 0, 0, 0),
    prodvers=(1, 0, 0, 0),
    mask=0x3f,
    flags=0x0,
    OS=0x40004,
    fileType=0x1,
    subtype=0x0,
    date=(0, 0)
  ),
  kids=[
    StringFileInfo([
      StringTable(
        u'040904B0',
        [StringStruct(u'CompanyName', u'Your Company'),
         StringStruct(u'FileDescription', u'Procedural Generation Demo'),
         StringStruct(u'FileVersion', u'1.0.0'),
         StringStruct(u'InternalName', u'ProceduralGenerationDemo'),
         StringStruct(u'LegalCopyright', u'Copyright (c) 2024'),
         StringStruct(u'OriginalFilename', u'ProceduralGenerationDemo.exe'),
         StringStruct(u'ProductName', u'Procedural Generation Demo'),
         StringStruct(u'ProductVersion', u'1.0.0')])
    ])
  ]
)
```

## Final Notes

- The standalone executable is completely self-contained
- No Python installation required on target machines
- Works on Windows 10/11 (and Windows 7/8 with some limitations)
- File size is typically 50-100 MB due to included Python runtime
- First startup may be slower due to unpacking process 