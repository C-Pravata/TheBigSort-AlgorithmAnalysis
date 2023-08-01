import sys
sys.setrecursionlimit(1000000000)

def quicksort_with_count(arr):
    count = {'comparisons': 0, 'exchanges': 0}
    stack = [(0, len(arr) - 1)]
    while stack:
        start, end = stack.pop()
        if start >= end:
            continue
        pivot = arr[start]
        i = start + 1
        j = end
        while i <= j:
            count['comparisons'] += 1
            if arr[i] <= pivot:
                i += 1
            else:
                arr[i], arr[j] = arr[j], arr[i]
                j -= 1
                count['exchanges'] += 1
        arr[start], arr[j] = arr[j], arr[start]
        count['exchanges'] += 1
        stack.append((start, j - 1))
        stack.append((j + 1, end))
    return arr, count

def quicksort_insertion_sort_100_iterative(arr):
    num_exchanges = 0
    num_comparisons = 0
    stack = [(0, len(arr) - 1)]
    while stack:
        start, end = stack.pop()
        if end - start + 1 <= 100:
            insertion_sort_range(arr, start, end)
            num_exchanges += end - start
            num_comparisons += (end - start) * (end - start + 1) // 2
        else:
            pivot = arr[start]
            i = start + 1
            j = end
            while i <= j:
                num_comparisons += 1
                if arr[i] <= pivot:
                    i += 1
                else:
                    arr[i], arr[j] = arr[j], arr[i]
                    j -= 1
                    num_exchanges += 1
            arr[start], arr[j] = arr[j], arr[start]
            num_exchanges += 1
            stack.append((start, j - 1))
            stack.append((j + 1, end))
    return arr, num_exchanges, num_comparisons

def insertion_sort_range(arr, start, end):
    for i in range(start + 1, end + 1):
        j = i
        while j > start and arr[j - 1] > arr[j]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

def quicksort_insertion_sort_50_iterative(arr):
    num_exchanges = 0
    num_comparisons = 0
    stack = [(0, len(arr) - 1)]
    while stack:
        start, end = stack.pop()
        if end - start + 1 <= 50:
            insertion_sort_range(arr, start, end)
            num_exchanges += end - start
            num_comparisons += (end - start) * (end - start + 1) // 2
        else:
            pivot = arr[start]
            i = start + 1
            j = end
            while i <= j:
                num_comparisons += 1
                if arr[i] <= pivot:
                    i += 1
                else:
                    arr[i], arr[j] = arr[j], arr[i]
                    j -= 1
                    num_exchanges += 1
            arr[start], arr[j] = arr[j], arr[start]
            num_exchanges += 1
            stack.append((start, j - 1))
            stack.append((j + 1, end))
    return arr, num_exchanges, num_comparisons

def insertion_sort_range(arr, start, end):
    for i in range(start + 1, end + 1):
        j = i
        while j > start and arr[j - 1] > arr[j]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

def quicksort_median_of_three_iterative(arr):
    num_exchanges = 0
    num_comparisons = 0
    stack = [(0, len(arr) - 1)]
    while stack:
        start, end = stack.pop()
        if start >= end:
            continue
        pivot_index = median_of_three(arr, start, end)
        pivot = arr[pivot_index]
        i = start
        j = end
        while i <= j:
            num_comparisons += 1
            while arr[i] < pivot:
                i += 1
                num_comparisons += 1
            num_comparisons += 1
            while arr[j] > pivot:
                j -= 1
                num_comparisons += 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
                num_exchanges += 1
        stack.append((start, j))
        stack.append((i, end))
    return arr, num_exchanges, num_comparisons

def median_of_three(arr, start, end):
    first = arr[start]
    last = arr[end]
    middle_index = (start + end) // 2
    middle = arr[middle_index]
    if first < middle < last or last < middle < first:
        return middle_index
    elif middle < first < last or last < first < middle:
        return start
    else:
        return end

def natural_merge_sort_iterative(arr):
    num_comparisons = 0
    num_exchanges = 0

    def merge_iterative(l1, l2):
        nonlocal num_comparisons, num_exchanges
        merged = []
        i = j = 0
        while i < len(l1) and j < len(l2):
            num_comparisons += 1
            if l1[i] <= l2[j]:
                merged.append(l1[i])
                i += 1
            else:
                merged.append(l2[j])
                j += 1
                num_exchanges += len(l1) - i
        merged.extend(l1[i:])
        merged.extend(l2[j:])
        return merged

    def split_runs_iterative(arr):
        runs = []
        start = 0
        for i in range(1, len(arr)):
            if arr[i-1] > arr[i]:
                runs.append(arr[start:i])
                start = i
        runs.append(arr[start:])
        return runs

    if len(arr) <= 1:
        return arr, num_comparisons, num_exchanges
    runs = split_runs_iterative(arr)
    while len(runs) > 1:
        new_runs = []
        for i in range(0, len(runs)-1, 2):
            new_runs.append(merge_iterative(runs[i], runs[i+1]))
        if len(runs) % 2 == 1:
            new_runs.append(runs[-1])
        runs = new_runs
    return runs[0], num_comparisons, num_exchanges

def insertion_sort_iterative(arr):
    if len(arr) <= 1:
        return arr
    else:
        sorted_arr = insertion_sort_iterative(arr[:-1])
        i = len(sorted_arr) - 1
        while i >= 0 and sorted_arr[i] > arr[-1]:
            i -= 1
        return sorted_arr[:i+1] + [arr[-1]] + sorted_arr[i+1:]

def sort_data_iterative(filename, sort_function):
    with open(filename, 'r') as f:
        data = []
        for line in f:
            numbers = line.strip().split()
            data += [int(x) for x in numbers]
    sorted_data = sort_function(data)
    #print(sorted_data)
    return sorted_data

input_files = ['ran50.dat', 'rev50.dat', 'asc50.dat', 'ran1K.dat','rev1K.dat', 'asc1K.dat', 'ran2K.dat','rev2K.dat', 'asc2K.dat', 'ran5K.dat','rev5K.dat', 'asc5K.dat', 'ran10K.dat','rev10K.dat', 'asc10K.dat']
#input_files = ['dup500.dat']
sorting_algorithms = [quicksort_with_count, quicksort_insertion_sort_100_iterative, quicksort_insertion_sort_50_iterative, quicksort_median_of_three_iterative, natural_merge_sort_iterative]

for filename in input_files:
    for sort_function in sorting_algorithms:
        sorted_data = sort_data_iterative(filename, sort_function)
        output_filename = f'sorted_{filename}_{sort_function.__name__}.txt'
        with open(output_filename, 'w') as f:
            for num in sorted_data:
                f.write(str(num) + '\n')

print(sort_data_iterative('ran50.dat', quicksort_with_count))
print(sort_data_iterative('ran50.dat', quicksort_insertion_sort_100_iterative))
print(sort_data_iterative('ran50.dat', quicksort_insertion_sort_50_iterative))
print(sort_data_iterative('ran50.dat', quicksort_median_of_three_iterative))
print(sort_data_iterative('ran50.dat', natural_merge_sort_iterative))

print(sort_data_iterative('rev50.dat', quicksort_with_count))
print(sort_data_iterative('rev50.dat', quicksort_insertion_sort_100_iterative))
print(sort_data_iterative('rev50.dat', quicksort_insertion_sort_50_iterative))
print(sort_data_iterative('rev50.dat', quicksort_median_of_three_iterative))
print(sort_data_iterative('rev50.dat', natural_merge_sort_iterative))

print(sort_data_iterative('asc50.dat', quicksort_with_count))
print(sort_data_iterative('asc50.dat', quicksort_insertion_sort_100_iterative))
print(sort_data_iterative('asc50.dat', quicksort_insertion_sort_50_iterative))
print(sort_data_iterative('asc50.dat', quicksort_median_of_three_iterative))
print(sort_data_iterative('asc50.dat', natural_merge_sort_iterative))


#print('\n'.join(map(str, sort_data_recursive('ran50.dat', quicksort_recursive))))
#print('\n'.join(map(str, sort_data_recursive('ran50.dat', quicksort_insertion_sort_100_recursive))))
#print('\n'.join(map(str, sort_data_recursive('ran50.dat', quicksort_insertion_sort_50_recursive))))
#print('\n'.join(map(str, sort_data_recursive('ran50.dat', quicksort_median_of_three_recursive))))
#print('\n'.join(map(str, sort_data_recursive('ran50.dat', natural_merge_sort_recursive))))

#print('\n'.join(map(str, sort_data_recursive('rev50.dat', quicksort_recursive))))
#print('\n'.join(map(str, sort_data_recursive('rev50.dat', quicksort_insertion_sort_100_recursive))))
#print('\n'.join(map(str, sort_data_recursive('rev50.dat', quicksort_insertion_sort_50_recursive))))
#print('\n'.join(map(str, sort_data_recursive('rev50.dat', quicksort_median_of_three_recursive))))
#print('\n'.join(map(str, sort_data_recursive('rev50.dat', natural_merge_sort_recursive))))

#print('\n'.join(map(str, sort_data_recursive('asc50.dat', quicksort_recursive))))
#print('\n'.join(map(str, sort_data_recursive('asc50.dat', quicksort_insertion_sort_100_recursive))))
#print('\n'.join(map(str, sort_data_recursive('asc50.dat', quicksort_insertion_sort_50_recursive))))
#print('\n'.join(map(str, sort_data_recursive('asc50.dat', quicksort_median_of_three_recursive))))
#print('\n'.join(map(str, sort_data_recursive('asc50.dat', natural_merge_sort_recursive))))
