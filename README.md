# pyprofiler
Profiler utility for python

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

[screenshot](./main_graph.png)

###graphical representation, needs wxpython and runsnakerun
```bash
brew install wxPython
pip install runsnakerun
python run_graph_main.py
```

```python
runsnake_profile_method("aggregate", globals(), locals())
```

[screenshot](./snake.png)
