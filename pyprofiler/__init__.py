# coding=utf-8
"""
Profiler utility for python
Erik de Jonge
erik@a8.nl
license: gpl2
"""
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()

import os
import cProfile
from pstats import Stats
from cProfile import Profile


def start_profile():
    """
    start_profile
    @rtype: Profile
    """
    pr = Profile()
    pr.enable()
    return pr


def console(x):
    """
    @type x: str, unicode
    @return: None
    """
    print("\033[33m$", x, "\033[0m")


def end_profile(pr, items=20, printstats=False, returnvalue=False):
    """
    @type pr: str, unicode
    @type items: int
    @type printstats: bool
    @type returnvalue: bool
    @return: None
    """
    p = Stats(pr)

    if returnvalue is True:
        return p.get_print_list([items])
    p.strip_dirs()
    console("total time")
    p.sort_stats('time')

    if items is None:
        p.print_stats()
    else:
        p.print_stats(items)

    if printstats:
        console("cumulative time")
        p.sort_stats('cumtime')

        if items is None:
            p.print_stats()
        else:
            p.print_stats(items)

        p.sort_stats('calls')

        if items is None:
            p.print_stats()
        else:
            p.print_stats(items)


def runsnake_profile_method(method, cglobals, clocals):
    """
    @type method: str, unicode
    @type cglobals: dict
    @type clocals: dict
    @return: None
    """
    cProfile.runctx(method + "()", globals=cglobals, locals=clocals, filename=method + ".profile")
    os.system("python /usr/local/lib/python2.7/site-packages/runsnakerun/runsnake.py " + method + ".profile")
    os.system("rm " + method + ".profile")


def graph_profile_program(sourcefile):
    """
    @type sourcefile: str, unicode
    @return: None
    """
    if 0 != os.system("python -m cProfile -o output.pstats ./" + sourcefile):
        print("\033[31mprofile error:\033[0m")
        print("\033[33m", "pip install graphviz", "\033[0m")
        print("\033[33m", "pip install gprof2dot", "\033[0m")

    elif 0 != os.system("gprof2dot -f pstats output.pstats | dot -Tpng -o " + sourcefile.replace(".py", ".png")):
        print("\033[31mgprof2dot error:\033[0m")
        print("\033[33m", "pip install graphviz", "\033[0m")
        print("\033[33m", "pip install gprof2dot", "\033[0m")
        print("\033[33m", "gprof2dot is in path? (/usr/local/bin/gprof2dot)", "\033[0m")
    else:
        if not os.path.exists("./" + sourcefile.replace(".py", ".png")):
            print("\033[31mcannot find", sourcefile.replace(".py", ".png"), "\033[0m")
        else:
            os.system("open " + sourcefile.replace(".py", ".png"))

            if os.remove("output.pstats"):
                os.remove("output.pstats")
