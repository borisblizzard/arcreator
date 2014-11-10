@echo off

python src/build_lib.py

python setup.py build_ext --inplace

echo Done
pause