#!/usr/bin/env python3
"""
Build script for creating a standalone executable of the Procedural Generation Demo.
This script uses PyInstaller to package the application with all its dependencies.
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def check_pyinstaller():
    """Check if PyInstaller is installed."""
    try:
        import PyInstaller
        print(f"✓ PyInstaller {PyInstaller.__version__} is installed")
        return True
    except ImportError:
        print("✗ PyInstaller is not installed. Installing...")
        return False

def install_pyinstaller():
    """Install PyInstaller if not already installed."""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller>=5.0.0"])
        print("✓ PyInstaller installed successfully")
        return True
    except subprocess.CalledProcessError:
        print("✗ Failed to install PyInstaller")
        return False

def build_executable():
    """Build the standalone executable using PyInstaller."""
    
    # PyInstaller command arguments
    cmd = [
        "pyinstaller",
        "--onefile",                    # Create a single executable file
        "--windowed",                   # Don't show console window on Windows
        "--name=ProceduralGenerationDemo",  # Name of the executable
        "--icon=icon.ico",              # Icon file (if exists)
        "--add-data=README.md;.",       # Include README in the package
        "--hidden-import=pygame",       # Ensure pygame is included
        "--hidden-import=perlin_noise", # Ensure perlin_noise is included
        "--clean",                      # Clean cache before building
        "main.py"                       # Main script to package
    ]
    
    # Remove icon argument if icon file doesn't exist
    if not os.path.exists("icon.ico"):
        cmd = [arg for arg in cmd if arg != "--icon=icon.ico"]
        print("Note: No icon.ico found, using default icon")
    
    print("Building standalone executable...")
    print(f"Command: {' '.join(cmd)}")
    
    try:
        subprocess.check_call(cmd)
        print("✓ Executable built successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Build failed with error: {e}")
        return False

def create_icon():
    """Create a simple icon file for the application."""
    try:
        from PIL import Image, ImageDraw
        
        # Create a 256x256 icon
        size = 256
        img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        # Draw a simple procedural generation themed icon
        # Background gradient from blue to green
        for y in range(size):
            color = (
                int(50 + (y / size) * 100),  # Blue to green
                int(100 + (y / size) * 150), # Green component
                int(200 - (y / size) * 100), # Blue component
                255
            )
            draw.line([(0, y), (size, y)], fill=color)
        
        # Add some "terrain" lines
        for i in range(5):
            y = size // 2 + (i - 2) * 20
            draw.line([(0, y), (size, y)], fill=(139, 69, 19, 255), width=3)
        
        # Save as ICO
        img.save("icon.ico", format='ICO')
        print("✓ Created icon.ico")
        return True
        
    except ImportError:
        print("Note: PIL/Pillow not available, skipping icon creation")
        return False
    except Exception as e:
        print(f"Note: Could not create icon: {e}")
        return False

def create_installer_script():
    """Create a simple installer script."""
    installer_content = '''@echo off
echo Procedural Generation Demo - Installer
echo =====================================
echo.
echo This will install the Procedural Generation Demo to your desktop.
echo.

set "DESKTOP=%USERPROFILE%\\Desktop"
set "INSTALL_DIR=%DESKTOP%\\ProceduralGenerationDemo"

if not exist "%INSTALL_DIR%" mkdir "%INSTALL_DIR%"

echo Copying files...
copy "dist\\ProceduralGenerationDemo.exe" "%INSTALL_DIR%\\"
copy "README.md" "%INSTALL_DIR%\\"

echo Creating desktop shortcut...
echo @echo off > "%DESKTOP%\\Procedural Generation Demo.bat"
echo cd /d "%INSTALL_DIR%" >> "%DESKTOP%\\Procedural Generation Demo.bat"
echo start ProceduralGenerationDemo.exe >> "%DESKTOP%\\Procedural Generation Demo.bat"

echo.
echo Installation complete!
echo You can now run the application from your desktop.
echo.
pause
'''
    
    with open("install.bat", "w") as f:
        f.write(installer_content)
    print("✓ Created install.bat")

def main():
    """Main build process."""
    print("Procedural Generation Demo - Build Script")
    print("=" * 45)
    print()
    
    # Check and install PyInstaller if needed
    if not check_pyinstaller():
        if not install_pyinstaller():
            print("Failed to install PyInstaller. Please install it manually:")
            print("pip install pyinstaller>=5.0.0")
            return False
    
    # Create icon if possible
    create_icon()
    
    # Build the executable
    if not build_executable():
        return False
    
    # Create installer script
    create_installer_script()
    
    print()
    print("Build completed successfully!")
    print()
    print("Files created:")
    print("- dist/ProceduralGenerationDemo.exe (standalone executable)")
    print("- install.bat (installer script)")
    print()
    print("To install the application:")
    print("1. Run install.bat to install to desktop")
    print("2. Or run dist/ProceduralGenerationDemo.exe directly")
    print()
    print("The executable is completely standalone and doesn't require Python!")
    
    return True

if __name__ == "__main__":
    success = main()
    if not success:
        sys.exit(1) 