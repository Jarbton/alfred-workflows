from sys import argv, stderr


def main():
    input_string = argv[1]
    print(f"Input: {input_string}", file=stderr)

    output_string = input_string.upper()
    print(f"Output: {output_string}", file=stderr)


if __name__ == "__main__":
    main()
