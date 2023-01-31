from json import dumps
from sys import argv

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

    # Generate Alfred response
    alfred_results = []
    for item in store:
        if input_string in item.keyword:
            result = {
                "title": item.keyword,
                "subtitle": item.url,
                "arg": item.url,
                "autocomplete": item.keyword,
            }
            alfred_results.append(result)

    response = dumps({"items": alfred_results})

    print(response, end="")


if __name__ == "__main__":
    main()
