CC=gcc
CFLAGS=$(shell python-config --cflags)
LDFLAGS=$(shell python-config --libs)
RUNDIRFLAGS=-Wl,-R,'$$ORIGIN'

all: Welder

Welder: Welder.c
	$(CC) $(CFLAGS) $(RUNDIRFLAGS) Welder.c -o Welder $(LDFLAGS)

cython:
	python cythonize.py build_ext --inplace

library:
	python build_lib.py

purge:
	python purge.py
