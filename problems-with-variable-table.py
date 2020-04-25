""" 
Question: Given a sorted linked list, delete all duplicates such that each element appear only once.

1. Reasonable inputs:
input           output
[1,2,3,4,4] ->  [1,2,3,4]
[1,1,2,3,4] ->  [1,2,3,4]

2-3. Solving and Find Patterns:
So for this problem I would have a pointer that starts at index 0
It will then compare the element at the start index to the element right after
which is at start + 1, and if they are the not the same then I would increment start by 1, 
to move along the array, and also adding that element to a different array
However, if they are the same then I would increment start by two because I want to use the 
delete method in python to delete the duplicate, and since I deleted the item, I need to 
increment start by two to essentially skip that and loop the entire array properly

4. Pseudocode
Set start to equal 0
Loop through array, while start is less than len of array
If the element at start index in the array is equal to element at start index + 1
Then move the start pointer by one down the array, like normal, while adding that element to
new array.
If the element at the start index is not equal to the  element at start index + 1
Then move the start pointer by 2, and adding that element the new array
Return the created array

Variable Table 
Variable : Value
array: [1, 1, 2, 3, 3, 4, 4, 6, 6]
start: 0 2 3 5 7 9
len(array)-1: 8
array[start]: 1 2 3 4 6
array[start+1]: 1 3 4 6
no_duplicates [1,2,3,4,6]

"""

def remove_duplicates(array):
    no_duplicates = []
    start = 0 

    while start < len(array)-1:
      if array[start] != array[start+1]:
        no_duplicates.append(array[start])
        start += 1
      else:
        no_duplicates.append(array[start])
        start += 2

    # return no_duplicates
    return no_duplicates

"""
Quesiton: Given an integer, write a function to determine if it is a power of two.

1. Reasonable Inputs:
input   output
1     -> true
16    -> true
512   -> true
218   -> false

2-3. Solving and Find Patterns:
I need to take the input and divide it by 2 and save that answer and just divide by 2 again and again until
the answer is equal to 1 when it is a product of 2 or when the answer is not meaning there's some remainder
so the input would not be a power of 2.

4. Pseudocode
Set remainder to equal the input which is n
Create a loop where it stops when remainder is greater than 1, because it mean be that it would either be completely 
divisible by 2 ie 2/2 = 1 
  Within the loop update the remainder to be the answer when n/2 
  Update the value of n to be the remainder

Check to see if remainder equals 1 meanning 2/2 = 1
  Return True because it's divisble by 2
Else
  Return False because n is not completely divisble by 2 in all iterations of division. 

"""

def is_power_2(n):
  remainder = n

  while remainder > 1:
    remainder -= n / 2
    n = remainder

  if remainder == 1:
    return True
  return False


if __name__ == "__main__":
    # Inputs
    array1 = [1, 1, 2, 3, 3, 4, 4, 6, 6]
    array2 = [1,2,3,4,4]
    array3 = [1,1,2,3,4]
    
    print(remove_duplicates(array1))
    print(remove_duplicates(array2))
    print(remove_duplicates(array3))

    # Inputs
    n1 = 1
    n2 = 16
    n3 = 512
    n4 = 218

    print(is_power_2(n1))
    print(is_power_2(n2))
    print(is_power_2(n3))
    print(is_power_2(n4))