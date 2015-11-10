__author__ = 'Charles Engen'


import Battleship_1_0_0
import multiprocessing
import datetime
import cProfile
import sys

max_processes = (multiprocessing.cpu_count() - 1)
iterations = 3000


def update_progress(progress):
    print('\r[{0}] {1}%'.format('#'*(progress/10), progress))

def worker(x=0):
    while True:
        if x % 100 == 0:
            if sys.flags.interactive:
                update_progress(int(x/iterations * 100))
        Battleship_1_0_0._start_game(override=x, display=False)
        return


def main():
    try:
        start = datetime.datetime.now()

        thread_pool = multiprocessing.Pool(max_processes)

        results = thread_pool.map_async(worker, range(iterations))

        thread_pool.close()
        thread_pool.join()

        print("Job took: %s" % (datetime.datetime.now() - start))

        input()

    except KeyboardInterrupt:
        print(KeyboardInterrupt)
        thread_pool.close()
        thread_pool.join()

        input("Waiting for keypress")

if __name__ == "__main__":
    cProfile.run('main()')