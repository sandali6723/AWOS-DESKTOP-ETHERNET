@echo off
echo Building AWOS Desktop App...

REM Create virtual environment
python -m venv venv
call venv\Scripts\activate.bat

REM Install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt

REM Build executable
pyinstaller awos.spec --clean

echo ✅ Build complete! Check dist\ folder
pause