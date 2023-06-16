import types


def flatten(a_list: list, depth: int = -1) -> list:
    result = []
    for element in a_list:
        if depth == 0 or type(element) is not list:
            result.append(element)
        else:
            result.extend(flatten(element, depth - 1))
    return result


def flat_generator(list_of_list):
    fl_lst = flatten(list_of_list)
    for i in fl_lst:
        yield i


def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]
    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item
    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()