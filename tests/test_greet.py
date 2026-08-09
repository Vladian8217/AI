from greet import greet


def test_greet_with_name():
    assert greet("Vladimir") == "Hello, Vladimir!"


def test_greet_with_empty_name():
    assert greet("") == "Hello, there!"
