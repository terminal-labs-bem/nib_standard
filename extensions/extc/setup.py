import io, os, sys
unbufferedstdout = io.TextIOWrapper(open(sys.stdout.fileno(), 'wb', 0), write_through=True)
unbufferedstderr = io.TextIOWrapper(open(sys.stderr.fileno(), 'wb', 0), write_through=True)
sys.stdout = unbufferedstdout
sys.stderr = unbufferedstderr

from setuptools import setup, find_packages, Extension

setup(
    ext_modules = [Extension("extc.helloworld", ["bind.c", "libmypy.c"])],
)
