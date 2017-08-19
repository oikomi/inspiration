import time
import functools


def sortable_by_creation_time(cls):
    """
    give a cls sorted by created time
    :param cls:
    :return:
    """
    original_init = cls.__init__

    @functools.wraps(original_init)
    def new_init(self, *args, **kwargs):
        print(args)
        print(kwargs)
        original_init(self, *args, **kwargs)
        self._created = time.time()
        print(self._created)

    cls.__init__ = new_init

    cls.__lt__ = lambda self, other: self._created < other._created
    cls.__gt__ = lambda self, other: self._created > other._created

    return cls


@sortable_by_creation_time
class Sortable(object):
    def __init__(self, identifier):
        self.identifier = identifier

    def __repr__(self):
        return self.identifier


if __name__ == '__main__':
    first = Sortable("first")
    time.sleep(1)
    second = Sortable("second")
    time.sleep(1)
    third = Sortable("third")
    sortables = [first, second, third]
    print(sorted(sortables))
