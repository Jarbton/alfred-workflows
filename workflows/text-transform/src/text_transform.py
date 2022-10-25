from json import dumps
from sys import argv, stderr


def spongebob_case(text: str) -> str:
    """Convert text to Spongebob case"""
    return "".join([c.lower() if i % 2 == 0 else c.upper() for i, c in enumerate(text)])


def main():
    input_string = argv[1]
    print(f"Input: {input_string}", file=stderr)

    output_strings = {
        "upper": input_string.upper(),
        "lower": input_string.lower(),
        "title": input_string.title(),
        "pascal": input_string.title().replace(" ", ""),
        "snake": input_string.replace(" ", "_"),
        "kebab": input_string.lower().replace(" ", "-"),
        "spongebob": spongebob_case(input_string),
    }

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
                    "subtitle": f"Paste {key} case to cursor position",
                    "arg": value,
                }
            },
        }
        alfred_results.append(result)

    response = dumps({"items": alfred_results})

    print(response, end="")


if __name__ == "__main__":
    main()
