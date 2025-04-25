import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"執行時間:{end-start:.2f}秒")
        return result
    return wrapper

@timer
def slow_function(seconds):
    time.sleep(seconds)
    print("函式執行完畢")

slow_function(3)