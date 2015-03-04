# pyprofiler
Profiler utility for python

##sample program used
```python

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
    print "method 1"
    time.sleep(0.1)
    call_next(funcs)


def meth2(funcs=None):
    """
    @type funcs: None, list
    @return: None
    """
    print "method 2"
    time.sleep(0.2)
    call_next(funcs)


def meth3(funcs=None):
    """
    @type funcs: None, list
    @return: None
    """
    print "method 3"
    time.sleep(0.3)
    call_next(funcs)


def meth4(funcs=None):
    """
    @type funcs: None, list, None
    @return: None
    """
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


def main():
    """
    main
    """
    meth1()
    meth2()
    meth3()
    meth4()
    aggregate()
```

###profile some code in body
```python
profiler = start_profile()
meth1()
meth2()
meth3()
meth4()
end_profile(profiler)
```
```bash
$ total time
         42 function calls (39 primitive calls) in 2.018 seconds

   Ordered by: internal time
   List reduced from 22 to 20 due to restriction <20>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        8    2.016    0.252    2.016    0.252 {time.sleep}
        1    0.001    0.001    0.002    0.002 pyprofiler.py:16(end_profile)
        1    0.000    0.000    0.000    0.000 functools.py:2(<module>)
        1    0.000    0.000    0.001    0.001 pstats.py:1(<module>)
        2    0.000    0.000    0.504    0.252 main_profile.py:32(meth2)
        2    0.000    0.000    0.205    0.103 main_profile.py:22(meth1)
        2    0.000    0.000    0.908    0.454 main_profile.py:42(meth3)
      8/5    0.000    0.000    0.604    0.121 main_profile.py:10(call_next)
        2    0.000    0.000    1.406    0.703 main_profile.py:52(meth4)
        1    0.000    0.000    1.006    1.006 main_profile.py:62(aggregate)
        1    0.000    0.000    0.000    0.000 pstats.py:32(Stats)
        3    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}
        1    0.000    0.000    0.000    0.000 pstats.py:62(__init__)
        1    0.000    0.000    0.000    0.000 {isinstance}
        1    0.000    0.000    0.000    0.000 pstats.py:106(load_stats)
        1    0.000    0.000    0.000    0.000 pstats.py:84(init)
        1    0.000    0.000    0.000    0.000 cProfile.py:90(create_stats)
        1    0.000    0.000    0.000    0.000 pstats.py:451(TupleComp)
        1    0.000    0.000    0.000    0.000 {hasattr}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```
###graphical representation, needs wxpython and runsnakerun
```bash
brew install wxPython
pip install runsnakerun
```

```python
graph_profile_program("main_graph.py")
```

![screenshot](main_graph.png)

###graphical representation, needs wxpython and runsnakerun
```bash
brew install wxPython
pip install runsnakerun
python run_graph_main.py
```

```python
runsnake_profile_method("aggregate", globals(), locals())
```

![screenshot](snake.png)
