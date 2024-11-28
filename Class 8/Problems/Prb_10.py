x = -40
try:
    assert x > 0, "Number must be greater than 0"
    print(x)
except AssertionError as e:
    print(e)
