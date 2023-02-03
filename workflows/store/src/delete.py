from sys import argv

from utils import load_store, save_store


def main():
    """
    Main function for removing provided URL from store.

    Does not check input as it is not possible to run
    this script with no input in Alfred.
    """
    # Get input args from Alfred
    args = argv[1:]
    url = args[0]

    # Check if url is in store
    store = load_store()
    for item in store:
        if item.url == url:
            store.remove(item)
            save_store(store)
            print(f"Removed {item.keyword} from store", end="")
            return


if __name__ == "__main__":
    main()
