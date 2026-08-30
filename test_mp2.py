import sys
sys.path.insert(0, 'src')
from concurrent.futures import ProcessPoolExecutor
from inquisitio.runner.batch import run_batch
def f(x):
    from inquisitio.runner import batch
    return batch._HAS_NATIVE
if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=1) as ex:
        print(list(ex.map(f, [1])))
