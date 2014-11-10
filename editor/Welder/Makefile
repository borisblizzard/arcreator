CC=gcc
CFLAGS=$(shell python3.4-config --cflags)
LDFLAGS=$(shell python3.4-config --libs)
RUNDIRFLAGS=-Wl,-R,'$$ORIGIN'

all: Welder library cython

Welder: src/Welder.c
	$(CC) $(CFLAGS) $(RUNDIRFLAGS) src/Welder.c -o src/Welder $(LDFLAGS)

library:
	python3.4 src/build_lib.py

cython:
	pyhton3.4 setup.py build_ext --inplace
