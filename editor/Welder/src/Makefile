CC=gcc
CFLAGS=$(shell python3.4-config --cflags)
LDFLAGS=$(shell python3.4-config --libs)
RUNDIRFLAGS=-Wl,-R,'$$ORIGIN'

all: Welder library

Welder: Welder.c
	$(CC) $(CFLAGS) $(RUNDIRFLAGS) Welder.c -o Welder $(LDFLAGS)

library:
	python3.4 build_lib.py
