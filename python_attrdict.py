'''
A class for accessing dictionaries as if they were classes (syntactically nice)

You can't access attributes outside of what you declare in the init


For example:

tasks = {"a": [1, 2], "b": [10, 11]}
task_nice = AttrDict(tasks)


tasks.a.append(3)
tasks["b"].append(12)

tasks.c # should throw keyerror or attributerror
'''


class AttrDict(dict):
    """ Syntax candy """
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
