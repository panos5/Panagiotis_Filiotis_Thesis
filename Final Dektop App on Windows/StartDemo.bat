
setlocal


echo  "Setting up PYTHONPATH..."

::for pynaoqi version 1.9 
set pynaoqi_dir="%cd%\pynaoqi-python-2.7-naoqi-1.14-Win32"

::for pygame version 1.9 
set pygame_dir="%cd%\pygame-1.9.1release" 

::for PIL-Imaging version 1.9
set pil_dir="%cd%\PIL"  


set python_dir=%pynaoqi_dir%

::;%pil_dir%;%pygame_dir%;

setx PYTHONPATH %python_dir%


REM move AnuDaw.ttf %systemroot%\Fonts
REM regedit /s fonts.reg

REM [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts]
REM "fontname (TrueType)"="AnuDaw.ttf" 

Rem fontinstall.bat
Rem xcopy AnuDaw.ttf %systemroot%\fonts
Rem regedit /s font.reg


::setx PATH "%PATH%;C:\Python34\Scripts"

echo "Starting NAO Demonstrator..."

py  Main.py


::LD_PRELOAD=/usr/lib64/libX11.so py Main.py


endlocal