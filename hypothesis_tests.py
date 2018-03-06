from hypothesis import given
import hypothesis.strategies as st
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


@given(st.lists(st.integers()), st.lists(st.text()))
def test_dictn(a, b):
    res = dict.fromkeys(a, None)
    res.update(zip(a,b))
    assert dictn(a,b) == res

