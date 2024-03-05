import argparse


def generate_numbers_smaller_than(n):
    for i in range(1, n):
        yield i


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Print numbers smaller than a given number.')
    parser.add_argument('-n', type=int, help='Enter a number to print numbers smaller than it.')
    args = parser.parse_args()

    if args.n is None:
        parser.print_help()
    else:
        for num in generate_numbers_smaller_than(args.n):
            print(num)
