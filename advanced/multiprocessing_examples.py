"""Multiprocessing example: CPU-bound map."""

from multiprocessing import Pool

def square(x): return x*x

def parallel_square(nums, processes=4):
    with Pool(processes=processes) as p:
        return list(p.map(square, nums))

if __name__ == "__main__":
    print(parallel_square([1,2,3,4,5]))
