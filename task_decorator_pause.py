import time

def pause(a):
    def decorator(b):
        def wrapper(*args, **kwargs):
            time.sleep(a)
            return b(*args, **kwargs)
        return wrapper
    return decorator