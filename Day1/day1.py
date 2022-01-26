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

def parse(filename: str) -> List[List[int]]:
    matrix = []
    with open(filename, "r") as f:
        lines = f.read().strip().split("\n")

    return list(map(int, lines))

def p1(changes: List[int], p2=False):
    freq = 0

    for change in changes:
        freq += change
    return freq


def p2(changes: List[int], freq=0, history=None):
    if not history:
        history = {freq}

    for change in changes:
        freq += change
        if freq in history:
            return freq
        else:
            history.add(freq)
    return p2(changes, freq, history)



def main(filename: str) -> Tuple[Optional[int], Optional[int]]:
    from time import time

    start = time()
    answer_a, answer_b = None, None

    changes = parse(filename)
    # ver_count, end_idx, val = parse_string(s, 0, 0)
    answer_a = p1(changes)
    answer_b = p2(changes)
    end = time()
    print(end - start)
    return answer_a, answer_b


if __name__ == "__main__":

    from utils import submit_answer
    from aocd.exceptions import AocdError

    sample = "sample.txt"
    input = "input.txt"

    sample_a_answer = 3
    sample_b_answer = 2

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
        submit_answer(answer_a, "a", day=1, year=2018)
    except AocdError:
        submit_answer(answer_b, "b", day=1, year=2018)
    