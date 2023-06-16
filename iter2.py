def flatten(a_list: list, depth: int = -1) -> list:
    result = []
    for element in a_list:
        if depth == 0 or type(element) is not list:
            result.append(element)
        else:
            result.extend(flatten(element, depth - 1))
    return result


class FlatIterator:
    def __init__(self, list_of_list):
        self.list_of_list = flatten(list_of_list)

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.list_of_list):
            raise StopIteration
        item = self.list_of_list[self.index]
        return item


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]
    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item
    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()
