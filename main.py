from part1 import *
from part2 import *
from util import CodeTimer


def main():
    with CodeTimer("Part1"):
        run_kmeans("./sample/sample.jpg")

    with CodeTimer("Part2"):
        run_agg("./sample/sample.jpg")


if __name__ == "__main__":
    main()
