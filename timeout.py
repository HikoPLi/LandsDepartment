
import time
import signal


class TimeoutError(Exception):
    def __init__(self, msg):
        super(TimeoutError, self).__init__()
        self.msg = msg


def time_out(interval, callback):
    def decorator(func):
        def handler(signum, frame):
            raise TimeoutError("run func timeout")

        def wrapper(*args, **kwargs):
            try:
                signal.signal(signal.SIGALRM, handler)
                signal.alarm(interval)
                result = func(*args, **kwargs)
                signal.alarm(0)
                return result
            except TimeoutError as e:
                callback(e)
        return wrapper
    return decorator


def timeout_callback(e):
    print(e.msg)
