
import random
from memory_profiler import profile

array = []
def init_random_array(array_size):
  global array

  array = []
  random.seed(3102)

  for i in range(array_size):
      array.append(random.randint(0, array_size))
  return (array)

@profile
def insertion_sort(arr):
  for i in range(1, len(arr)):
    curr_val = arr[i]
    curr_index = i
    while curr_index > 0 and arr[curr_index-1] > curr_val:
      arr[curr_index] = arr[curr_index-1]
      curr_index -= 1

    arr[curr_index] = curr_val

init_random_array(1000)
insertion_sort(array)
