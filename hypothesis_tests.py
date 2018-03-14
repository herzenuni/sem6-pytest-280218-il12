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
def test_len_dictn(a, b):
    assert len(dictn(a,b)) == len(a) or len(dictn(a,b)) == len(b)

@given(st.lists(st.integers()), st.lists(st.text()))
def test_type_dictn(a, b):
    assert type(dictn(a,b)) == dict

@given(st.lists(), st.lists())
def test_try_different_lists_dictn(a, b):
    assert type(dictn(a,b)) == dict
    assert len(dictn(a,b)) == len(a) or len(dictn(a,b)) == len(b)
