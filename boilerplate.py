#!/usr/bin/python3

import sys
import re

HEADERSTART= [
    '# This file is part of ansible',
    '# This module is free software',
    '# Ansible is free software',
    '# This program is free software',
]


OLD_BOILDERPLATE = [
    re.compile(start+r'.*?ANSIBLE_METADATA', flags=re.IGNORECASE+re.DOTALL)
    for start in HEADERSTART
]

NEW_BOILDERPLATE = """# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA"""


def add_boilerplate(buf):
    for possibleheader in OLD_BOILDERPLATE:
        newbuf = possibleheader.sub(NEW_BOILDERPLATE, buf)
        if newbuf != buf:
            return newbuf
    return buf

def process_module_file(filename):
    with open(filename, 'r') as f:
        buf = f.read()

    buf = add_boilerplate(buf)

    with open(filename, 'w') as f:
        f.write(buf)


def main():
    for filename in sys.argv[1:]:
        process_module_file(filename)


if __name__ == '__main__':
    main()
