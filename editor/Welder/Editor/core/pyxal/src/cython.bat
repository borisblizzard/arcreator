@echo off

echo ==========================================================
echo starting Cython compiler
echo ==========================================================
echo.

cython.exe -I "..\pyxal\include" -o _pyxal.cpp --cplus _pyxal.pyx

echo ++DONE
echo.

pause
