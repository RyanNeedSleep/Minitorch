from hypothesis import given, settings
from hypothesis.strategies import integers

@settings(max_examples=10)
@given(integers(), integers())
def test_addition_is_commutative(x, y):
    print(x, y)
    assert x + y == y + x




