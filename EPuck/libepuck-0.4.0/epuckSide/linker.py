#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright 2008 Renato Florentino Garcia <fgar.renato@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3, as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

#
# linker.py
#
# Run the linker of MPLAB C30 using Wine, in all files *.o

# Configure MPLAB_C30_PATH for MPLabC30 install path,
#
# Example:
# MPLAB_C30_PATH="/usr/local/mplabC30"

MPLAB_C30_PATH=

import sys
import os
from glob import glob
from shutil import copy
from tempfile import mkdtemp

def quote(str):
    return '"' + str + '"'

THIS_DIR=os.getcwd()
BIN_DIR= MPLAB_C30_PATH + '/bin'
MPLAB_LIB_DIR= MPLAB_C30_PATH + '/lib'
SCRIPT= MPLAB_C30_PATH + '/support/gld/p30f6014A.gld'
OUTPUT= THIS_DIR + '/output.cof'
MAP= THIS_DIR + '/proj.map'

objects = glob('*.o')
objects += glob('libObj/*')
objects = map(os.path.abspath, objects)
objects = map(quote, objects)
objects = ','.join(objects)

MPLAB_LIB_DIR = quote(MPLAB_LIB_DIR)
SCRIPT = quote(SCRIPT)
MAP = quote(MAP)
OUTPUT = quote(OUTPUT)
THIS_DIR = quote(THIS_DIR)

os.chdir(BIN_DIR)
ARG_COMPILADOR = '-Wl,' + objects + ',-L' + MPLAB_LIB_DIR\
                 + ',' + ',--script=' + SCRIPT + ',--heap=512,-Map='\
                 + MAP + ',--report-mem,-o'  + OUTPUT
ARG_CONVERSOR =  THIS_DIR + '/output.cof'

print 'wine pic30-gcc.exe ' + ARG_COMPILADOR
os.system( 'wine pic30-gcc.exe ' + ARG_COMPILADOR)

print 'wine pic30-bin2hex.exe ' + ARG_CONVERSOR
os.system( 'wine pic30-bin2hex.exe ' + ARG_CONVERSOR)

