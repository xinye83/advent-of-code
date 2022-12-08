from pathlib import Path
from typing import Self

data = (Path(__file__).parent / 'input' / 'day07.in').read_text().split('\n')


class File:
    name: str
    size: int

    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size


class Dir:
    ROOT = '__root__'

    name: str
    parent: Self
    subdir: dict[str, Self]
    file: dict[str, File]
    _size: int

    def __init__(self, name: str, parent: Self | None) -> None:
        self.name = name
        self.parent = parent
        self.subdir = dict()
        self.file = dict()
        self._size = -1

    def add_subdir(self, subdir: Self) -> None:
        self.subdir[subdir.name] = subdir

    def add_file(self, file: File) -> None:
        self.file[file.name] = file

    def size(self, part_one: bool = False) -> int:
        global sum_size

        if self._size < 0:
            self._size = 0
            for _, file in self.file.items():
                self._size += file.size
            for _, subdir in self.subdir.items():
                self._size += subdir.size(part_one)

        if part_one and self._size < 100000:
            sum_size += self._size
        return self._size


root = Dir(Dir.ROOT, None)

cur = root

for line in data[1:]:
    if line[:4] == '$ cd':
        if line[5:] == '..':
            cur = cur.parent
        else:
            cur = cur.subdir[line[5:]]
    elif line[:4] == '$ ls':
        continue
    else:
        size, name = line.split()
        if size == 'dir':
            cur.add_subdir(Dir(name, cur))
        else:
            cur.add_file(File(name, int(size)))

sum_size = 0
root.size(part_one=True)
print(sum_size)

# part 2

del_size = root.size()

ind = 0
stack = [root]

while ind < len(stack):
    cur = stack[ind]
    ind += 1

    if cur.size() > root.size() - 40000000:
        del_size = min(del_size, cur.size())

    for _, subdir in cur.subdir.items():
        stack.append(subdir)

print(del_size)
