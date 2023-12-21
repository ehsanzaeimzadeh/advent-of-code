def pp(ptrn, t):
    print(t, "---" * 10)
    for v in ptrn:
        print(v)


def tilt_rocks(ptrn, dir):
    ptrn = ["".join(x) for x in zip(*ptrn)] if dir in "NS" else ptrn
    rev = False if dir in "SE" else True
    for i, v in enumerate(ptrn):
        ptrn[i] = "#".join(["".join(sorted(list(c), reverse=rev)) for c in v.split("#")])
    return ["".join(x) for x in zip(*ptrn)] if dir in "NS" else ptrn


def count_rocks(ptrn):
    cnt = 0
    for i, p in enumerate(ptrn):
        cnt += p.count("O") * (len(ptrn) - i)
    return cnt


def part_1(lines, offset=1):
    ptrn = [list(line) for line in lines]
    ptrn = tilt_rocks(ptrn, "N")
    return count_rocks(ptrn)


def part_2(lines):
    ptrn = [line for line in lines]
    looped = [ptrn]
    iterations = 1000000000
    end = 0
    while True:
        end += 1
        for d in "NWSE":
            ptrn = tilt_rocks(ptrn, d)
            pp(ptrn, d + str(end))
        if ptrn in looped:
            break
        looped.append(ptrn)
    start = looped.index(ptrn)
    ptrn = looped[(iterations - start) % (end - start) + start]
    return count_rocks(ptrn)


def solve(lines):
    print(__file__.split("/")[-1], "part_1: ", part_1(lines))
    print(__file__.split("/")[-1], "part_2: ", part_2(lines))
