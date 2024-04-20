import io, os, sys
unbufferedstdout = io.TextIOWrapper(open(sys.stdout.fileno(), 'wb', 0), write_through=True)
unbufferedstderr = io.TextIOWrapper(open(sys.stderr.fileno(), 'wb', 0), write_through=True)
sys.stdout = unbufferedstdout
sys.stderr = unbufferedstderr

from setuptools import setup, find_packages, Extension
from Cython.Distutils import build_ext

setup(
    ext_modules = [Extension("extcython.hello", ["hello.pyx"])],
)
