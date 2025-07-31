import argparse


def main():
    parser = argparse.ArgumentParser(
        prog='radialreal',
        description='# Radial Real-Space Solve'
    )
    parser.add_argument('-i', '--input')
    args = parser.parse_args()
    print(args.input)
    print("begin")

if __name__ == '__main__':
    main()