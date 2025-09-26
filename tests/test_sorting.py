from problem_solving.sorting_algorithms import merge_sort, quick_sort

def test_merge_sort():
    assert merge_sort([3,1,2,1]) == [1,1,2,3]

def test_quick_sort():
    assert quick_sort([5,4,3,2,1]) == [1,2,3,4,5]
