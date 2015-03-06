# coding=utf-8
"""
appinstance
Active8 (04-03-15)
license: GNU-GPL2
"""
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
import unittest
from unittester import unit_test_main
from main_profile import *


class ProfilerTest(unittest.TestCase):

    def test_profiler(self):
        """
        test_assert_raises
        """
        self.assertEqual(len(get_print_list()[1]), 15)


def main():
    """
    main
    """
    unit_test_main(globals())


if __name__ == "__main__":
    main()
