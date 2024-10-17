import pytest 
from herons_formula import area_calculate, input_validate
from consecutive_zeros import longest_zeros

# Tests for Herons formula
def test_area_calculate():
    assert area_calculate([3, 4, 5]) == 6.0
    assert area_calculate([5, 12, 13]) == 30.0
    assert area_calculate([6, 8, 10]) == 24.0
    assert area_calculate([7, 8, 9]) == pytest.approx(26.832815729997478)
    
def test_input_validate():
    assert input_validate([3, 4, 5]) == True
    assert input_validate([5, 5, 5]) == True
    assert input_validate([1, 2, 3]) == False
    assert input_validate([5, 12]) == False
    assert input_validate([5, 'a', 10]) == False
    assert input_validate([5, 5, 15]) == False
    
# Tests for longest consecutive zeros
def test_longest_zeros():
    assert longest_zeros("") == 0
    assert longest_zeros("1111") == 0
    assert longest_zeros("00001000") == 4
    assert longest_zeros("010101001") == 2
    assert longest_zeros("0 0") == 1

pytest.main()