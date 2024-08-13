# bubble_sort.py
def bubble_sort(lt):
    n = len(lt)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lt[j] > lt[j + 1]:
                temp = lt[j]
                lt[j] = lt[j + 1]
                lt[j + 1] = temp
    return lt


if __name__ == "__main__":
    unsorted_list = [50, 40, 10, 15, 60, 6]
    print(f'Unsorted list : {unsorted_list}')
    sorted_list = bubble_sort(unsorted_list)
    print(f'Sorted list : {sorted_list}')