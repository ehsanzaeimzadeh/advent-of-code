import argparse
import importlib
import os

print(os.getcwd())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advent of code")
    parser.add_argument("days", metavar="N", type=int, nargs="+", help="Days to solve")

    args = parser.parse_args()
    print(args.days)

    modules = [f"2023.day{day}" for day in args.days]
    for module in modules:
        day = importlib.import_module(module)
        with open(module.replace(".", "/") + ".txt") as f:
            lines = [line.strip() for line in f.readlines()]
            day.solve(lines)
