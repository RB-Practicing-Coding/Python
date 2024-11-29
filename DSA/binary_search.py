"""Binary Search
    - Sort the array
    - Find mid = (low + high) / 2
    - 3 cases:
        + Target = mid -> Target
        + Target < mid -> Find in [low:mid-1]
        + Target > mid -> Find in [mid+1:high]
"""
import random


def binary_search(lst, target, low, high) -> int:
    if low > high:
        return -1

    if target not in lst:
        return -2

    mid = int((low + high) / 2)

    if target == lst[mid]:
        return mid
    elif target < lst[mid]:
        return binary_search(lst=lst, target=target, low=0, high=mid-1)
    else:
        return binary_search(lst=lst, target=target, low=mid + 1, high=len(lst))


if __name__ == '__main__':
    lst = [random.randint(1, 30) for _ in range(10)]
    lst = sorted(lst)
    print(f'We have list: {lst}')
    print('What number to search: ')
    target = int(input())
    res = binary_search(lst=lst, target=target, low=0, high=len(lst))
    if res == -1:
        print(f'input wrong')
    elif res == -2:
        print(f'{res} is not in {lst}')
    else:
        print(f'{res} appears in list at index {res}')
