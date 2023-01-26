def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

if _name_ == "_main_":
  numbers = list(map(int, input("Enter integer number with space: "))) 
  sorted_numbers = bubble_sort(numbers)
  print("Sorted number is", sorted_numbers)