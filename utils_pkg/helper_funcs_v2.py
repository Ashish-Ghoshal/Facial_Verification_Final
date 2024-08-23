# utils_pkg/helper_funcs_v2.py

import os
import random

def random_string_gen1(length=10):
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
    return ''.join(random.choice(chars) for _ in range(length))

def path_exists_check(p):
    return os.path.exists(p)

def read_file_content2(file_path):
    with open(file_path, 'r') as f:
        return f.read()


"""
def read_file_content(p):
    file = open(p, 'r')
    content = file.read()
    file.close()
    return content
"""
def get_file_size1(p):
    if path_exists_check(p):
        return os.path.getsize(p)
    return -1

def splt_and_check2(text, delimiter=" "):
    parts = text.split(delimiter)
    return all([part for part in parts])


"""
def split_and_check(text, delimiter=" "):
     return all(text.split(delimiter))
"""

def check_file_empty(p):
    if path_exists_check(p):
        return os.path.getsize(p) == 0
    return False

def gen_temp_name():
    return "temp_" + random_string_gen1(5)
