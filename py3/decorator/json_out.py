import functools
import json


class JSONOutputError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


def json_output(indent=None, sort_keys=False):
    def actual_decorator(decorated):
        @functools.wraps(decorated)
        def inner(*args, **kwargs):
            try:
                result = decorated(*args, **kwargs)
            except JSONOutputError as ex:
                result = {
                    'status': 'error',
                    'message': str(ex),
                }
            return json.dumps(result, indent=indent, sort_keys=sort_keys)

        return inner

    return actual_decorator


@json_output(4)
def foo():
    return {'status': 'done'}


if __name__ == '__main__':
    print(foo())
