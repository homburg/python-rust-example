#!/usr/bin/env python2.7

print("Hello, python!")

from cffi import FFI
ffi = FFI()

ffi.cdef("""
        void it_works();
        void it_works_c();
""")

rust = ffi.dlopen("./libit-works.so")

C = ffi.dlopen("./libit-works-c.so")


C.it_works_c()
rust.it_works()

print("fin!")
