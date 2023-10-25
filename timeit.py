from random import randint
import time
from functools import wraps
from imppkg.harmonic_mean import harmonic_mean as hmc

def timefn(fn):
    @wraps(fn)
    def measure_time(*args, **kwargs):
        t1 = time.time()
        result = fn(*args, **kwargs)
        t2 = time.time()
        print(f"@timefn: {fn.__name__} took {t2 - t1} seconds")
        return result
    return measure_time

def harmonic_mean(values):
    n = len(values)
    return n/sum([1/i for i in values])

@timefn
def main():
    nums = [randint(1, 1_000_000) for _ in range(1_000_000)]
    val = harmonic_mean(nums)
    print(val)

@timefn
def main_c():
    nums = [randint(1, 1_000_000) for _ in range(1_000_000)]
    val = hmc(nums)
    print(val)

if __name__ == "__main__":
    main()
    main_c()