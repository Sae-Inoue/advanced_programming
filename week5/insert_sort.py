# insertion_sort.py
def insertion_sort(lt):
    n = len(lt)
    a = 0
    for i in range(n):
        sort_list = lt[i]
        j = i-1
        while j >= 0 and lt[j] > sort_list:
            lt[j+1] = lt[j]
            j = j-1
        lt[j+1] = sort_list
    return lt


if __name__ == "__main__":
    unsorted_list = [50, 40, 10, 15, 60, 6]
    print(f'Unsorted list : {unsorted_list}')
    sorted_list = insertion_sort(unsorted_list)
    print(f'Sorted list : {sorted_list}')