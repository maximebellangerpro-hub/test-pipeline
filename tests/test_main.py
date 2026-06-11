from main import hello_world, add, multiply


def test_hello_world():
    assert hello_world() == "Hello from Hermes Pipeline"


def test_add():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0
    assert add(10, -5) == 5


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0
    assert multiply(-2, 3) == -6
    assert multiply(7, 1) == 7