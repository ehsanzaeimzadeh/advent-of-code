from itertools import combinations


def part_1(lines, offset=1):
    universe = [list(line) for line in lines]
    r_exp = [r for r, row in enumerate(universe) if all(e == "." for e in row)]
    c_exp = [c for c, col in enumerate(list(map(list, zip(*universe)))) if all(e == "." for e in col)]
    galaxies = []
    _r = 0
    for r, row in enumerate(universe):
        _c = 0
        _r += 1 + offset if r in r_exp else 1
        for c, v in enumerate(row):
            _c += 1 + offset if c in c_exp else 1
            if v == "#":
                galaxies.append(f"{_r}.{_c}")
    pairs = list(combinations(galaxies, 2))
    dist_t = 0
    for e in pairs:
        dist_t += abs(int(e[0].split(".")[0]) - int(e[1].split(".")[0])) + abs(
            int(e[0].split(".")[1]) - int(e[1].split(".")[1])
        )
    return dist_t


def part_2(lines):
    return part_1(lines, 1000000 - 1)


def solve(lines):
    print(__file__.split("/")[-1], "part_1: ", part_1(lines))
    print(__file__.split("/")[-1], "part_2: ", part_2(lines))
