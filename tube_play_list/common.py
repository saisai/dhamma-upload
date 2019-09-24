#!/usr/bin/env python
# coding=utf-8
import inspect
from pathlib import Path

def _get_input(name):
    code_path = Path(inspect.currentframe().f_back.f_back.f_code.co_filename)
    return code_path.parent / name

def read_line(name="input.txt"):
    with open(_get_input(name)) as f:
        return next(f).strip("\n")

def read_lines(name="input.txt"):
    with open(_get_input(name)) as f:
        return [l for l in (l.strip("\n") for l in f) if l]
        
def read_file(name="input.txt"):

    return open(_get_input(name))


# https://raw.githubusercontent.com/davidism/advent/master/common.py
