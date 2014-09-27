CC=gcc
CFLAGS=$(shell python3.4-config --cflags)
LDFLAGS=$(shell python3.4-config --libs)
RUNDIRFLAGS=-Wl,-R,'$$ORIGIN'

all: Welder library

Welder: Welder.c
	$(CC) $(CFLAGS) $(RUNDIRFLAGS) Welder.c -o Welder $(LDFLAGS)

cython:
	python3.4 cythonize.py build_ext --inplace

library:
	python3.4 build_lib.py

purge:
	python3.4 purge.py
