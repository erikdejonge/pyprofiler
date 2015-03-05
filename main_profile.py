# coding=utf-8
"""
test for pyprofile
"""

import time
from pyprofiler import start_profile, end_profile, runsnake_profile_method


def call_next(funcs=None):
    """
    @type funcs: None, list
    @return: None
    """
    if funcs:
        func = funcs.pop()

        if func:
            func(funcs)


def meth1(funcs=None):
    """
    @type funcs: None, list
    @return: None
    """
    if funcs:
        print "method 1"

    time.sleep(0.1)
    call_next(funcs)


def meth2(funcs=None):
    """
    @type funcs: None, list
    @return: None
    """
    if funcs:
        print "method 2"

    time.sleep(0.2)
    call_next(funcs)


def meth3(funcs=None):
    """
    @type funcs: None, list
    @return: None
    """
    if funcs:
        print "method 3"

    time.sleep(0.3)
    call_next(funcs)


def meth4(funcs=None):
    """
    @type funcs: None, list, None
    @return: None
    """
    if funcs:
        print "method 4"

    time.sleep(0.4)
    call_next(funcs)


def aggregate():
    """
    aggregate
    """
    print "aggregate"
    funcs = [meth1, meth2, meth3]
    meth4(funcs)


def get_print_list():
    """
    get_print_list
    """
    profiler = start_profile()
    meth1()
    meth2()
    meth3()
    meth4()
    return end_profile(profiler, returnvalue=True)


def main():
    """
    main
    """
    profiler = start_profile()
    meth1()
    meth2()
    meth3()
    meth4()
    aggregate()
    end_profile(profiler)
    runsnake_profile_method("aggregate", globals(), locals())


if __name__ == "__main__":
    main()
