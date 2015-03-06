# coding=utf-8
"""
test for pyprofile
"""
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
from main_profile import *


def main():
    """
    main
    """
    meth1()
    meth2()
    meth3()
    meth4()
    aggregate()


if __name__ == "__main__":
    main()
