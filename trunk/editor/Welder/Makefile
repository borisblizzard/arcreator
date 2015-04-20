CC=gcc
CFLAGS=$(shell python3.4-config --cflags)
LDFLAGS=$(shell python3.4-config --libs)
RUNDIRFLAGS=-Wl,-R,'$$ORIGIN'

all: welder library cython

welder: src/welder.c
	$(CC) $(CFLAGS) $(RUNDIRFLAGS) src/welder.c -o src/welder $(LDFLAGS)

library:
	python3.4 src/build_lib.py

cython:
	python3.4 setup.py build_ext --inplace
