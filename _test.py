import pytest

#function to test square
def square(n):
    return n ** 2

#function to test cube
def cube(n):
    return n ** 3   

#function to test 4th power
def power_4(n):
    return n ** 4       

#function to test 5th power
def power_5(n):
    return n ** 5

def test_calculations():
    n = 2
    assert square(n) == 4,"Square calculation is incorrect"
    assert cube(n) == 8,"Cube calculation is incorrect"
    assert power_4(n) == 16,"4th power calculation is incorrect"
    assert power_5(n) == 32,"5th power calculation is incorrect"


def test_invalid_input():
    with  pytest.raises(TypeError):
        square("Savio")

    