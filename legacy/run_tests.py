import importlib
from pathlib import Path
from doctest import testmod


def run_tests(wild_path='daily_coding_problem_*.py', verbose=False):

    for filename in sorted(Path(__file__).parent.glob(wild_path)):
        module = importlib.import_module(filename.stem)
        results = testmod(module, verbose=verbose)
        print(f'{filename.name}: {"FAIL" if results.failed else "PASS"}')


if __name__ == '__main__':
    run_tests()
