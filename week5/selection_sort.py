# selection_sort.py
def selection_sort(lt):
    for i in range(len(lt)):
        min_index = i
        for j in range(i + 1, len(lt)):
            if lt[j] < lt[min_index]:
                min_index = j
        temp = lt[i]
        lt[i] = lt[min_index]
        lt[min_index] = temp
    return lt


if __name__ == "__main__":
    unsorted_list = [50, 40, 10, 15, 60, 6]
    print(f'Unsorted list : {unsorted_list}')
    sorted_list = selection_sort(unsorted_list)
    print(f'Sorted list : {sorted_list}')