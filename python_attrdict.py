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


'''
To do it recursively
'''


class RecurisveDotDict(dict):
    """
    Adapted from user Curt Hagenlocher from
    https://stackoverflow.com/questions/3031219/recursively-access-dict-via-attributes-as-well-as-index-access
    """
    MARKER = object()

    def __init__(self, value=None):
        if value is None:
            pass
        elif isinstance(value, dict):
            for key in value:
                self.__setitem__(key, value[key])
        else:
            raise TypeError('expected dict')

    def __setitem__(self, key, value):
        if isinstance(value, dict) and not isinstance(value, RecurisveDotDict):
            value = RecurisveDotDict(value)
        super(RecurisveDotDict, self).__setitem__(key, value)

    def __getitem__(self, key):
        found = self.get(key, RecurisveDotDict.MARKER)
        if found is RecurisveDotDict.MARKER:
            found = RecurisveDotDict()
            super(RecurisveDotDict, self).__setitem__(key, found)
        return found

    __setattr__, __getattr__ = __setitem__, __getitem__