from sys import argv, stderr

from utils import StoreItem, load_store, save_store_item


def main():
    """
    Main function for storing provided URL with associated keyword.

    Gets keyword and url from Alfred input and stores in
    hard coded file located in utils.py
    """
    # Get input args from Alfred
    args = argv[1:]

    # Check if input is valid
    if len(args) != 2:
        print("Invalid number of arguments", file=stderr)
        return

    keyword, url = args

    # Check if keyword is already in store
    store = load_store()
    if keyword in store:
        print("Keyword already in store", file=stderr)
        print("Keyword is already in the store!")
        return

    # Check if url is valid and add http if not
    if not url.startswith("http"):
        url = "http://" + url

    # Add keyword and url to store
    item = StoreItem(keyword, url)
    save_store_item(item)

    # Return to Alfred
    print(f"Added {keyword} to store", end="")


if __name__ == "__main__":
    main()
