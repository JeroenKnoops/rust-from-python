from ctypes import cdll

lib = cdll.LoadLibrary("target/release/librust_from_python.dylib")

lib.process()

print("done!")
