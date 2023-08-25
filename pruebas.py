from Practica_1 import repetidos
import pytest
import random

n1 = random.randint(0,10)
n2 = random.randint(0,10)
n3 = random.randint(0,10)
n4 = random.randint(0,10)
def test_repetidos():
    assert repetidos([n1,n2,n3,n4]) == True
    assert repetidos([1,2,3,4]) == False

@pytest.mark.parametrize("nums, res", [([1,2,3,1], True), ([1,2,3,4], False)])
def test_repetidos_parametrizado(nums, res):
    assert repetidos(nums) == res