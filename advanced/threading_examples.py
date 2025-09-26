"""Threading example: parallel sum with threads (I/O-bound style demo)."""

import threading

def worker(data, out, idx):
    out[idx] = sum(data)

def parallel_sum(nums, chunks=4):
    size = max(1, len(nums)//chunks)
    parts = [nums[i:i+size] for i in range(0, len(nums), size)]
    out = [0]*len(parts)
    threads = []
    for i, part in enumerate(parts):
        t = threading.Thread(target=worker, args=(part, out, i))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    return sum(out)

if __name__ == "__main__":
    print(parallel_sum(list(range(1_0000))))
