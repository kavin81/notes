st = "hello world"

from itertools import permutations

perms = ["".join(p) for p in permutations(st)]
print(list(set(sorted(perms))))
