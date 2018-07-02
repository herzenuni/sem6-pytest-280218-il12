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

class TestDictn:

    def test_dictn1(self):
        assert(dictn([1,2,3],['a','b','c'])=={1: 'a', 2: 'b', 3: 'c'})

    def test_dictn2(self):
        assert(dictn([1,2,3], 3)==None)

    def test_dictn3(self):
        assert(dictn(3,['a','b','c'])==None)

    def test_dictn4(self):
        assert(dictn([],['a','b','c'])=={})

