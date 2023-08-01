 # Sorting Algorithms

This code provides implementations of several sorting algorithms in Python, including the quicksort and natural merge sort algorithms. The quicksort algorithm is a fast and efficient sorting algorithm that uses a divide-and-conquer approach to sort the input array. The natural merge sort algorithm is a variant of the merge sort algorithm that takes advantage of existing order in the input array to reduce the number of comparisons and exchanges required to sort the data. Both algorithms are implemented using an iterative approach and return the sorted array along with the number of comparisons and exchanges made during the sorting process.

## Algorithms

The following sorting algorithms are implemented:

- `quicksort_with_count`: Sorts an array using the quicksort algorithm and returns the sorted array along with the number of comparisons and exchanges made during the sorting process.
- `quicksort_insertion_sort_100_iterative`: Sorts an array using quicksort. It uses quicksort for subarrays larger than 100 elements and insertion sort for subarrays with 100 or fewer elements. It returns the sorted array along with the number of exchanges and comparisons made during the sorting process.
- `quicksort_insertion_sort_50_iterative`: Similar to `quicksort_insertion_sort_100_iterative`, but uses a threshold of 50 elements instead of 100 for switching between quicksort and insertion sort.
- `quicksort_median_of_three_iterative`: Sorts an array using an iterative implementation of the quicksort algorithm with the median-of-three pivot selection strategy. It returns the sorted array along with the number of exchanges and comparisons made during the sorting process.
- `natural_merge_sort_iterative`: Sorts an array using an iterative implementation of the natural merge sort algorithm. It returns the sorted array along with the number of exchanges and comparisons made during the sorting process.

## Usage

The code provides a convenient `sort_data_iterative` function that allows you to sort data from a file using any of the implemented sorting algorithms. This function takes as input the name of the file containing the data to be sorted and a reference to the sorting function to be used. The input file should be formatted as one or more lines of space-separated integers, where each line represents a separate dataset to be sorted. The `sort_data_iterative` function reads the data from the input file, sorts it using the specified sorting function, and returns the sorted data as a list of integers.

## Example usage:

```python
sorted_data = sort_data_iterative('input_file.dat', quicksort_with_count)
```

The code also includes several print statements that demonstrate how to use the sort_data_iterative function to sort data from input files using each of the implemented sorting algorithms.

## Output
The code is designed to write the sorted data to output files for easy access and analysis. The names of the output files are generated automatically based on the name of the input file and the sorting function used. Specifically, the output file name is constructed by appending the string sorted_ to the input file name, followed by the name of the sorting function (obtained using the __name__ attribute of the function object), and finally the .txt file extension. For example, if the input file is named input_file.dat and the sorting function is quicksort_with_count, then the output file will be named sorted_input_file_quicksort_with_count.txt.

Each output file contains one line for each element in the sorted data. In addition to the sorted data, some of the implemented sorting algorithms also return counts of the number of __comparisons__ and __exchanges__ made during the sorting process. These counts can be useful for analyzing and comparing the performance of different sorting algorithms.