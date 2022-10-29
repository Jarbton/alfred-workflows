from pytest import mark

from workflows.text_transform.src.text_transform import spongebob_case


@mark.parametrize(
    "input_string,expected",
    [
        (
            "hello world",
            "hElLo wOrLd",
        ),
        (
            "Hello World",
            "hElLo wOrLd",
        ),
        (
            "HELLO WORLD",
            "hElLo wOrLd",
        ),
    ],
)
def test_spongebob_case(input_string: str, expected: str):
    """
    Test the spongebob_case function.

    Args:
        input_string: The input string to transform.
        expected: The expected output of the spongebob_case function.
    """
    assert spongebob_case(input_string) == expected
