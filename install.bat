@echo off
echo Procedural Generation Demo - Installer
echo =====================================
echo.
echo This will install the Procedural Generation Demo to your desktop.
echo.

set "DESKTOP=%USERPROFILE%\Desktop"
set "INSTALL_DIR=%DESKTOP%\ProceduralGenerationDemo"

if not exist "%INSTALL_DIR%" mkdir "%INSTALL_DIR%"

echo Copying files...
copy "dist\ProceduralGenerationDemo.exe" "%INSTALL_DIR%\"
copy "README.md" "%INSTALL_DIR%\"

echo Creating desktop shortcut...
echo @echo off > "%DESKTOP%\Procedural Generation Demo.bat"
echo cd /d "%INSTALL_DIR%" >> "%DESKTOP%\Procedural Generation Demo.bat"
echo start ProceduralGenerationDemo.exe >> "%DESKTOP%\Procedural Generation Demo.bat"

echo.
echo Installation complete!
echo You can now run the application from your desktop.
echo.
pause
