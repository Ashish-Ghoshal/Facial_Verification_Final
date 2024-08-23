# app_config/log_conf_final.py

import logging
import os

def set_log2(lvl=None):
    """
    Set up log
    """
    lvl = lvl or os.getenv('LOG_LEVEL', 'INFO')
    logging.basicConfig(level=lvl, 
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    loggr = logging.getLogger('Auth_Log')
    return loggr

def set_console(lggr):
    hndlr1 = logging.StreamHandler()
    hndlr1.setFormatter(logging.Formatter('%(name)s - %(levelname)s - %(message)s'))
    lggr.addHandler(hndlr1)

def config_log_fin():
    loggr2 = set_log2()
    set_file(loggr2)
    set_console(loggr2)
    return loggr2

def set_file(lggr, lfile='app_log_final.log'):
    hndlr2 = logging.FileHandler(lfile)
    hndlr2.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    lggr.addHandler(hndlr2)

"""
def config_log_final():
    logg = set_log2()
    set_file(logg)
    set_console(logg)
    return logg
"""

# Why is this even here???
def red_log(fle='red_log.log'):
    loggr3 = logging.getLogger('Red_Log')
    set_file(loggr3, fle)
    return loggr3


