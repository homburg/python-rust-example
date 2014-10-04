#!/usr/bin/env python2.7

print("Hello, python!")

from cffi import FFI
ffi = FFI()

ffi.cdef("""
        void it_works(const char* input, const int j);
""")

C = ffi.dlopen("./libit-works-c.so")
C.it_works("something from python", 52)

rust = ffi.dlopen("./libit-works.so")
rust.it_works("something from python to rust", 42)

print("fin!")
