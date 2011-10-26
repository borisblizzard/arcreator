@ECHO off
cls

::setup envierment
set working=%~dp0
echo working in %working%
set "ocra_file=%working%ocrasa.rb"
set "out_path=%working%bin\"
set "script=%working%src\program.rbw"
::set "temp_exe=%working%program.exe"
set "name=RMXP2ARC.exe"
set "icon=%working%src\icon.ico"

echo ====================================================
echo ** RMXP to ARC Project Converter Compile via Orca **
echo ====================================================
echo.

echo.
echo Deleating old build...
del /s /q "%out_path%%name%"

:: --console --windows --chdir-first 
:: run ocra
echo.
ruby "%ocra_file%" "%script%" "%icon%" --icon "%icon%" --windows --output "%out_path%%name%" --chdir-first

::echo.
::echo Moving resultent exe to bin\ dir

::mkdir "%out_path%"
::ren "%temp_exe%" "%name%"
::move "%working%%name%" "%out_path%"

echo =========== Finished Build ===========

PAUSE
