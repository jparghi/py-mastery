"""Read/write text files safely."""

from pathlib import Path

def write_lines(path: str, lines):
    Path(path).write_text("\n".join(lines), encoding="utf-8")

def read_lines(path: str):
    return Path(path).read_text(encoding="utf-8").splitlines()

if __name__ == "__main__":
    write_lines("/mnt/data/demo.txt", ["hello", "world"])  # adjust path locally if needed
    print(read_lines("/mnt/data/demo.txt"))
