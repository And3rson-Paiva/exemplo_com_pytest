from pytest import raises


def test_in_even_true():
    assert is_even(10) == True
    assert is_even(6) == True


def test_in_even_false():
    assert is_even(7) == False
    assert is_even(5) == False


def test_in_even_except():
    is_even('a')
    is_even(lambda z: z)

