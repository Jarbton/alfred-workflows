from os import environ

from pytest import CaptureFixture, mark

from workflows.monzo.src import monzo


@mark.parametrize(
    "username,reason,expected",
    [
        ("username1", ["10", "Item"], "https://monzo.me/username1/10?d=Item\n"),
        ("username2", ["10"], "https://monzo.me/username2/10\n"),
    ],
)
def test_e2e_url_generator(
    username: str, reason: list[str], expected: str, capsys: CaptureFixture
):
    """
    Test the end-to-end functionality of the URL generator.
    Sets environment variables and argv parameters.

    Args:
        username: The username to use in the URL.
        reason: The reason to use in the URL.
        expected: The expected output of the URL generator.
        capsys: The pytest fixture for capturing stdout.
    """

    # Set env vars
    environ["monzo_username"] = username

    # Add argv parameters
    monzo.argv = ["monzo.py"]
    monzo.argv.extend(reason)

    monzo.main()

    # Assert stdout is expected
    captured = capsys.readouterr()
    assert captured.out == expected
