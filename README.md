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

###profile some code
```python
profiler = start_profile()
meth1()
meth2()
meth3()
meth4()
end_profile(profiler)
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
