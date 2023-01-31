from sys import argv, stderr

from utils import load_store


def main():
    """
    Main function to open stored URLs.

    Gets store from harded coded file located in utils.py
    """
    # Get input from Alfred
    input_string = argv[1]

    # Check if input is in store
    store = load_store()
    if input_string in store:
        url = store.get(input_string)

        # Return to Alfred
        print(url, end="")
    else:
        print("Keyword not found in store", file=stderr)


if __name__ == "__main__":
    main()
