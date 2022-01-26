from collections import Counter, defaultdict, deque
from functools import reduce, lru_cache
from typing import (
    List,
    Tuple,
    Set,
    Dict,
    Iterable,
    DefaultDict,
    Optional,
    Union,
    Generator,
)
from copy import deepcopy
import re


def parse(filename: str):
    matrix = []
    with open(filename, "r") as f:
        lines = f.read().strip().split("\n")

    return [list(s) for s in lines]


def checksum(inputs: List[List[str]]):

    threes = 0
    twos = 0

    for inp in inputs:
        c = Counter(inp)
        if 2 in c.values():
            twos += 1
        if 3 in c.values():
            threes += 1
    return threes * twos


def most_similar(inputs: List[List[str]]):
    from itertools import combinations

    for str1, str2 in combinations(inputs, 2):
        diff = 0
        diff_idx = None
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                diff += 1
                diff_idx = i
                if diff > 1:
                    break
        if diff == 1:
            print("".join(str1), "".join(str2))
            return "".join(str1[:diff_idx]) + "".join(str1[diff_idx + 1:])




def main(filename: str) -> Tuple[Optional[int], Optional[int]]:
    from time import time

    start = time()
    answer_a, answer_b = None, None

    inputs = parse(filename)
    answer_a = checksum(inputs)

    if "sample" in filename:
        filename = "sample2.txt"
    inputs = parse(filename)
    answer_b = most_similar(inputs)

    end = time()
    print(end - start)
    return answer_a, answer_b


if __name__ == "__main__":

    from utils import submit_answer
    from aocd.exceptions import AocdError

    sample = "sample.txt"
    input = "input.txt"

    sample_a_answer = 12
    sample_b_answer = "fgij"

    answer_a, answer_b = main(sample)
    assert (
        answer_a == sample_a_answer
    ), f"AnswerA incorrect: Actual: {answer_a}, Expected: {sample_a_answer}"
    print("sampleA correct")
    if answer_b:
        assert (
            answer_b == sample_b_answer
        ), f"AnswerB incorrect: Actual: {answer_b}, Expected: {sample_b_answer}"
        print("sampleB correct")

    # Test on your input and submit
    answer_a, answer_b = main(input)
    print(f"Your input answers: \nA: {answer_a}\nB: {answer_b}")
    try:
        submit_answer(answer_a, "a", day=2, year=2018)
    except AocdError:
        submit_answer(answer_b, "b", day=2, year=2018)
