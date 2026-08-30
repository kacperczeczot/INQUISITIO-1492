import sys, os
from concurrent.futures import ProcessPoolExecutor
sys.path.insert(0, 'src')
def f(x):
    try:
        import inquisitio_native
        return "NATIVE OK"
    except ImportError as e:
        return f"IMPORT ERROR: {e}"
if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=1) as ex:
        print(list(ex.map(f, [1])))
