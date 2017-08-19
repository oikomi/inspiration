class Task(object):
    """

    """

    def __call__(self, *args, **kwargs):
        return self.run(*args, **kwargs)

    def run(self, *args, **kwargs):
        raise NotImplementedError("subclass must inplement `run`")

    def identify(self):
        return "i am a task"


def task(decorated):
    """
    :param decorated:
    :return:
    """

    class TaskSubclass(Task):
        def run(self, *args, **kwargs):
            return decorated(*args, **kwargs)

    return TaskSubclass()


@task
def foo():
    return 2 + 2


if __name__ == '__main__':
    print(foo())
    print(foo.identify())
