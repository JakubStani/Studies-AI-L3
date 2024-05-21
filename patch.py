import collections
try:
    collections.Mapping
except AttributeError:
    import collections.abc
    collections.Mapping = collections.abc.Mapping