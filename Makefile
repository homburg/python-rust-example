.PHONY: run

run: libit-works.so libit-works-c.so
	./hello.py

libit-works.o: it-works.c it-works.h
	gcc -fpic -c it-works.c

libit-works-c.so: libit-works.o
	gcc -shared -o libit-works-c.so it-works.o

libit-works.so: it-works.rs
	rustc it-works.rs --crate-type=dylib

