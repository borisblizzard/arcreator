@echo off

echo ==========================================================
echo starting Cython compiler
echo ==========================================================
echo.

cython.exe -I "..\PyXAL\include" -o _PyXAL.cpp --cplus _PyXAL.pyx

echo ++DONE
echo.

pause
