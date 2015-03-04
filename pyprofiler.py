
__author__ = 'rabshakeh'


def start_profile():
    """
    start_profile
    @rtype: Profile
    """
    from cProfile import Profile
    pr = Profile()
    pr.enable()
    return pr


def end_profile(pr, items=20, printstats=False):
    """
    @type pr: Profile
    @type items: int
    @type printstats: bool
    """
    if not "console" in globals():
        def console(x):
            """
            @type x: str, unicode
            @return: None
            """
            print "\033[93m$", x, "\033[0m"
    from pstats import Stats
    p = Stats(pr)
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

    import cProfile
    import os
    cProfile.runctx(method + "()", globals=cglobals, locals=clocals, filename=method + ".profile")
    os.system("python /usr/local/lib/python2.7/site-packages/runsnakerun/runsnake.py " + method + ".profile")
    os.system("rm " + method + ".profile")


def graph_profile_program(sourcefile):
    """
    @type sourcefile: str, unicode
    @return: None
    """

    import os
    if 0 != os.system("python -m cProfile -o output.pstats ./" + sourcefile):
        print "\033[31mprofile error:\033[0m"
        print "\033[33m", "pip install graphviz", "\033[0m"
        print "\033[33m", "pip install gprof2dot", "\033[0m"

    elif 0 != os.system("gprof2dot -f pstats output.pstats | dot -Tpng -o " + sourcefile.replace(".py", ".png")):
        print "\033[31mgprof2dot error:\033[0m"
        print "\033[33m", "pip install graphviz", "\033[0m"
        print "\033[33m", "pip install gprof2dot", "\033[0m"
        print "\033[33m", "gprof2dot is in path? (/usr/local/bin/gprof2dot)", "\033[0m"
    else:
        if not os.path.exists("./" + sourcefile.replace(".py", ".png")):
            print "\033[31mcannot find", sourcefile.replace(".py", ".png"), "\033[0m"
        else:
            os.system("open " + sourcefile.replace(".py", ".png"))

            if os.remove("output.pstats"):
                os.remove("output.pstats")
