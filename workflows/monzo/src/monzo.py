import os
from sys import argv, stderr


def main():
    """
    Main function for the URL generator.

    Gets username from environment variables (monzo_username)
    and amount and reason from argv. Prints the URL to stdout
    for Alfred to capture.
    """
    # Get username from Alfred environment variable
    username = os.getenv("monzo_username")
    print(f"Username: {username}", file=stderr)

    # Get input args from Alfred
    args = argv[1:]

    # Generate url with username and cost
    url = "https://monzo.me/" + username

    # Check if args were provided
    if len(args) > 0:
        print(f"Args: {args}", file=stderr)

        cost = args[0]

        # Check if cost is a number
        try:
            float(cost)
        except ValueError:
            print(
                "Cost must be the first argument and must be a valid number",
                file=stderr,
            )
            print(url, end="")
            return

        url += "/" + cost

        # Try to get reason from args
        for index, item in enumerate(args[1:]):
            if not index:
                url += "?d=" + item
            else:
                url += "%20" + item

    # Return to Alfred
    print(url, end="")


if __name__ == "__main__":
    main()
