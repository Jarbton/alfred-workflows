from json import dumps
from sys import argv, stderr


def spongebob_case(text: str) -> str:
    """
    Convert text to Spongebob case

    Args:
        text (str): Text to convert

    Returns:
        str: Spongebob case text
    """
    return "".join([c.lower() if i % 2 == 0 else c.upper() for i, c in enumerate(text)])


def transform_string(text: str) -> dict[str, str]:
    """
    Transform string to all cases.

    Args:
        text (str): Text to transform

    Returns:
        dict[str, str]: Dictionary of transformed strings
    """
    return {
        "spongebob": spongebob_case(text),
        "upper": text.upper(),
        "lower": text.lower(),
        "title": text.title(),
        "pascal": text.title().replace(" ", ""),
        "camel": text.split(" ")[0].lower()
        + "".join(ele.title() for ele in text.split(" ")[1:]),
        "snake": text.lower().replace(" ", "_"),
        "kebab": text.lower().replace(" ", "-"),
    }


def main():
    """
    Main function which takes input from alfred with argv and
    returns a json of transform strings by printing to stdout.
    """
    input_string = argv[1]
    print(f"Input: {input_string}", file=stderr)

    output_strings = transform_string(input_string)

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
