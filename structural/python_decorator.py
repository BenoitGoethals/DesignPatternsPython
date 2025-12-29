def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_call
def process_order(order_id):
    print(f"Processing order {order_id}")

process_order(42)


def timing(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Took {time.time() - start:.4f}s")
        return result
    return wrapper


@log_call
@timing
def heavy_task():
    import time
    time.sleep(1)

heavy_task = log_call(timing(heavy_task))


class Authorize:
    def __init__(self, role):
        self.role = role

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print(f"Checking role: {self.role}")
            return func(*args, **kwargs)
        return wrapper

@Authorize("admin")
def delete_user():
    print("User deleted")
