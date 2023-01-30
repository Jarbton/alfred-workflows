from json import dumps, loads
from sys import argv, stderr

# TODO: Make command to list bookmarks


def load_store():
    """
    Load store from file.
    """
    with open("store.json", "r") as store_file:
        store = loads(store_file.read())
    return store


def main():
    """
    Main function which takes input from alfred with argv and
    returns a json of transform strings by printing to stdout.
    """
    input_string = argv[1]
    print(f"Input: {input_string}", file=stderr)

    output_strings = ""  # find_url(input_string)

    alfred_results = []
    for key, value in output_strings.items():
        result = {
            "title": value,
            "subtitle": f"{key.title()} Case",
            "arg": value,
            "autocomplete": value,
            "icon": {"path": f"./icons/{key}.png"},
            "mods": {
                "cmd": {
                    "subtitle": f"Copy {key} case to clipboard",
                    "arg": value,
                }
            },
        }
        alfred_results.append(result)

    response = dumps({"items": alfred_results})

    print(response, end="")


if __name__ == "__main__":
    main()
