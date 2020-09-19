import time

def countdown(func):
    def timeit():
        for i in range(1, 4):
            print(i)
            time.sleep(1)
        func()
    return timeit()


@countdown
def time_now():
    print(time.strftime('%H:%M'))
