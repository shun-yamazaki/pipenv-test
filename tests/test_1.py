from lambda_function import some_func


def test_function():
    assert some_func("1", 2) == "12"
    assert some_func("a", 2) == "a2"


def test_function2():
    assert some_func("1", 2) == "12"
    assert some_func("a", 2) == "a2"
