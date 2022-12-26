#!/usr/bin/env python
# -*- encoding=utf8 -*-


import os
import sys

root_path = os.path.abspath(__file__)
root_path = '/'.join(root_path.split('/')[:-2])
sys.path.append(root_path)

class SKException(Exception):

    def __init__(self, message):
        super().__init__(message)
