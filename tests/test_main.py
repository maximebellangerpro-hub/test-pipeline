from main import hello_world, add


def test_hello_world():
    assert hello_world() == "Hello from Hermes Pipeline"


def test_add():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0
    assert add(10, -5) == 5