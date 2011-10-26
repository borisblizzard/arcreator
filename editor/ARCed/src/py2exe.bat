@ECHO off

cls
echo =====================================
echo **ARCed Build Operation for Windows**
echo =====================================
echo.

python setup.py py2exe

echo.
echo ========= Building Compleate =========
echo exe located in dist\ folder
echo.
pause
