def reverse_array(idx, elements):
    if idx == len(elements) // 2:
        return
    swap_idx = len(elements) - 1 - idx
    elements[idx], elements[swap_idx] = elements[swap_idx], elements[idx]
    reverse_array(idx + 1, elements)

elements = input().split()


reverse_array(0, elements)

print(*elements)

# iterative method:
# for left_idx in range(len(elements) // 2):
#     right_idx = len(elements) - 1 - left_idx
#     elements[left_idx], elements[right_idx] = elements[right_idx], elements[left_idx]
#
# print(*elements)