@ECHO off
cls
echo =====================================
echo **ARCed Build Operation for Windows**
echo =====================================

:: set up envierment
set working=%~dp0
set name=ARCed
set "src_path=%working%src\"
set version="0.0.1"
set author="ARC Developers"
set "icon=%working%icon.ico"
set "out_path=%working%build\"
set "py_installer=%working%pyinstaller-1.5.1\"

::get if we want to build in optimised pyhton (important for speed up of opengl)
:INVALID_CHOICE
echo.
set /p optimize="Build Optimised? y/n: "
if "%optimize%"=="y" goto SET_OPTIMISE_YES
if "%optimize%"=="n" goto SET_OPTIMISE_NO
echo invalid choice
goto INVALID_CHOICE

:SET_OPTIMISE_YES
set optimize=-O
goto CONTINUE

:SET_OPTIMISE_NO
set optimize=
goto CONTINUE


:: Main process
:CONTINUE

echo.
echo Deleating old build...
rmdir /s /q "%out_path%"

::Change working directory to the py-installer folder
cd /d "%py_installer%"

::Configure pyinstaller
echo.
echo =====================================
echo ** Configuring Python Installation **
echo =====================================
echo. 
echo deleating old config...
del "%py_installer%config.dat"

python %optimize% "%py_installer%Configure.py"

::Make spec file
echo. 
echo =====================================
echo **       Making Spec File          **
echo =====================================
echo.
python "%py_installer%Makespec.py" --onefile --windowed --out=%out_path% --paths=%src_path% --icon=%icon% --name=%name% "%src_path%Main.py"


if "%optimize%"=="-O" goto EDIT_SPEC_NOW_O
goto BUILD

:AFTER_EDIT_O
set /p c="Did you edit the %name%.spec file in %out_path% file? y/n: "
if "%c%"=="y" goto BUILD
if "%c%"=="n" goto EOF
echo invalid choice
goto AFTER_EDIT_O

::Build the exe
:BUILD
echo. 
echo =====================================
echo **          Building Exe           **
echo =====================================
echo.
python %optimize% "%py_installer%Build.py" "%out_path%%name%.spec"

echo.
echo ========= Building Compleate =========
echo exe located in %out_path%dist\
echo.
pause
goto EOF

::if we are building optimised we need to make a small edit to the generated spec file before we build
:EDIT_SPEC_NOW_O
echo.
echo you are building optimised:
echo at this point you should edit the
echo %name%.spec file in %out_path%
echo by changing the line
echo "a.scripts," 
echo to
echo "a.scripts + [('O','','OPTION')],"
echo to build optimised properly. 
echo if you don't know how to do this select no on the next question
echo. 
pause
goto AFTER_EDIT

:EOF