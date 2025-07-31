import argparse
from pathlib import Path

from radialreal.config import load_config,print_config


def main():
    parser = argparse.ArgumentParser(
        prog='radialreal',
        description='# Radial Real-Space Solve'
    )
    parser.add_argument('-i', '--input')
    args = parser.parse_args()
    print("### RR begin o0v0o ###")
    # read input file
    config=load_config(Path(args.input))
    print_config(config)
    # print input file

if __name__ == '__main__':
    main()
