import time
from multiprocessing import Process


def background(i):
    print(f"Process started with i = {i}")
    while True:
        print("Process running...")
        i += 1
        time.sleep(1)


if __name__ == "__main__":
    i = 0
    while i < 5:
        print(f"Main loop iteration {i}")
        time.sleep(1)
        p = Process(target=background, args=(i,))
        p.start()
        i += 1

    print("Main finished")
    # main exits, but process keeps running
