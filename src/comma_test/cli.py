import argparse
from typing import Sequence
from comma_test import detect_extra_commas

def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog='detect-extra-commas')
    parser.add_argument(
        'filenames',
        nargs='*',
        help='Filenames to process.',
    )

    args = parser.parse_args(argv)

    results = [
        detect_extra_commas(filename)
        for filename in args.filenames
    ]
    return int(any(results))
