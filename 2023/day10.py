ngrid = []


# Directions: bottom-up: A, top-down: V, left-right: >, right-left: <
def find_next(grid, r, c, in_dir):
    r_max = len(grid)
    c_max = len(grid[0])
    if grid[r][c] == "F":
        if in_dir == "A" and c + 1 < c_max and grid[r][c + 1] in "-7J":
            ngrid[r][c] = "F"
            return r, c + 1, ">"
        if in_dir == "<" and r + 1 < r_max and grid[r + 1][c] in "|JL":
            ngrid[r][c] = "F"
            return r + 1, c, "V"
    if grid[r][c] == "7":
        if in_dir == ">" and r + 1 < r_max and grid[r + 1][c] in "|JL":
            ngrid[r][c] = "7"
            return r + 1, c, "V"
        if in_dir == "A" and c - 1 >= 0 and grid[r][c - 1] in "-FL":
            ngrid[r][c] = "7"
            return r, c - 1, "<"
    if grid[r][c] == "-":
        if in_dir == ">" and c + 1 < c_max and grid[r][c + 1] in "-7J":
            ngrid[r][c] = "-"
            return r, c + 1, ">"
        if in_dir == "<" and c - 1 >= 0 and grid[r][c - 1] in "-LF":
            ngrid[r][c] = "-"
            return r, c - 1, "<"
    if grid[r][c] == "|":
        if in_dir == "A" and r - 1 >= 0 and grid[r - 1][c] in "|F7":
            ngrid[r][c] = "|"
            return r - 1, c, "A"
        if in_dir == "V" and r + 1 < r_max and grid[r + 1][c] in "|JL":
            ngrid[r][c] = "|"
            return r + 1, c, "V"
    if grid[r][c] == "J":
        if in_dir == "V" and c - 1 >= 0 and grid[r][c - 1] in "-FL":
            ngrid[r][c] = "J"
            return r, c - 1, "<"
        if in_dir == ">" and r - 1 >= 0 and grid[r - 1][c] in "|F7":
            ngrid[r][c] = "J"
            return r - 1, c, "A"
    if grid[r][c] == "L":
        if in_dir == "V" and c + 1 < c_max and grid[r][c + 1] in "-J7":
            ngrid[r][c] = "L"
            return r, c + 1, ">"
        if in_dir == "<" and r - 1 >= 0 and grid[r - 1][c] in "|F7":
            ngrid[r][c] = "L"
            return r - 1, c, "A"
    return -1, -1, -1


def find_s(board, r, c):
    r_max, c_max = len(board), len(board[0])
    if c + 1 < c_max and board[r][c + 1] in "-J7" and r + 1 < r_max and board[r + 1][c] in "|JL":
        return "F"
    if ((c - 1) >= 0) and (board[r][c - 1] in "-FL") and ((r + 1) < r_max) and (board[r + 1][c] in "|JL"):
        return "7"
    if c + 1 < c_max and board[r][c + 1] in "-J7" and c - 1 >= 0 and board[r][c - 1] in "-LF":
        return "-"
    if r + 1 < r_max and board[r + 1][c] in "-JL" and r - 1 >= 0 and board[r - 1][c] in "|F7":
        return "|"
    if c - 1 >= 0 and board[r][c - 1] in "-FL" and r - 1 >= 0 and board[r - 1][c] in "|F7":
        return "J"
    if c + 1 < c_max and board[r][c + 1] in "-J7" and r - 1 >= 0 and board[r - 1][c] in "|F7":
        return "L"


def part_1(lines):
    board = [list(line) for line in lines]
    i = 0
    for line in lines:
        ngrid.append(["." for i in range(len(line))])
        if "S" in line:
            r, c = i, list(line).index("S")
            board[r][c] = find_s(board, r, c)
            print(board[r][c])
        i += 1
    steps = 0
    _r = r
    _c = c
    d = "A"
    while True:
        if r == -1:
            break
        r, c, d = find_next(board, r, c, d)
        if r == _r and c == _c:
            break
        steps += 1

    return (steps + 1) / 2


def part_2(lines):
    inside_cnt = 0
    for row in range(len(ngrid)):
        for col in range(len(ngrid[row])):
            if ngrid[row][col] == ".":
                isinside = False
                isupward = False
                for ch in ngrid[row][col:]:
                    if ch == "|":
                        isinside = not isinside
                    elif ch in "LF":
                        isupward = ch == "L"
                    elif ch in "7J":
                        if ch != ("J" if isupward else "7"):
                            isinside = not isinside
                        isupward = False
                if isinside:
                    inside_cnt += 1

    return inside_cnt


def solve(lines):
    print(__file__.split("/")[-1], "part_1: ", part_1(lines))
    print(__file__.split("/")[-1], "part_2: ", part_2(lines))
