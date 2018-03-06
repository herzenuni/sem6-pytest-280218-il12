import pytest

def dictn(keys, values):
    try:
        if type(keys) is not list or type(values) is not list:
            raise TypeError('Input argument is not a list')
    except TypeError:
        print('Argument is not a list.')
    else:
        result = dict.fromkeys(keys, None)
        result.update(zip(keys, values))
        return result

@pytest.mark.parametrize("a,b,expected",[
    ([1,2,3],['a','b','c','d'], {1: 'a', 2: 'b', 3: 'c'}),
    ([1,2,3], 3, None),
    (3,['a','b','c'],None),
    ([],['a','b','c'],{})
])
def test_dictn(a, b, expected):
    assert dictn(a,b)==expected
    assert dictn([1,2,3], 3)==None
    assert dictn(3,['a','b','c'])==None
    assert dictn([],['a','b','c'])=={}


