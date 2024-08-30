nums = [1, 6, 3, 2, 6, 3, 76, 9, 0]

def merge(left: list, right: list):
    result = []
    l = 0
    r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    if l == len(left):
        result.extend(right[r:])
    elif r == len(right):
        result.extend(left[l:])
    return result

def merge_sort(array):
    if len(array) == 1:
        return array
    mid_idx = len(array) // 2
    left = array[:mid_idx]
    right = array[mid_idx:]
    return merge(merge_sort(left), merge_sort(right))

print(merge_sort(nums))
print(sorted(nums))