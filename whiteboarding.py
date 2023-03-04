
# PROBLEM 1: 

# Image a list of numbers from 1 to a max_num, inclusive- except that one of 
# these numbers will be missing from the list. Write a function that takes this 
# list of numbers, as well as the max_num, and returns the missing number. If no 
# numbers are missing, return 0. The function needs to have an O(n) runtime. 


# input --> ([2, 1, 4, 3, 6, 5, 7, 10, 9], 10)
# output --> 8 

def find_missing_num(nums, max_num):

    to_max_num = []
    for num in range(1, max_num+1):
        to_max_num.append(num)

    nums_dict = {}
    for num in nums:
        nums_dict[num] = 0

    for num in to_max_num: 
        if num not in nums_dict:
            return num
    else:
        return 0 

print(find_missing_num([2, 1, 4, 3, 6, 5, 7, 10, 9], 10))

################################################################################

# PROBLEM 2: 

# Write a function that takes in a string and returns True or False depending 
# on whether the string’s opening and closing brackets are balanced. Account for 
# the following bracket types:
    # Parentheses ()
    # Square Brackets []
    # Curly Braces {}

# If an open bracket appears, the pair should also be closed correctly. Examples:
    # "([ok])" => True
    # "{[[This has too many open square brackets]}" => False
    # ")(Closing bracket before opening bracket" => False
    # "[{Wrong order]}" => False
    # "No brackets!" => True


# GOOGLE DOC: https://docs.google.com/document/d/1CuzP6iXhrQcxYhV7e9NtCuKiEoc-21YpNojJAiQ4IF4/edit 

        
################################################################################

# PROBLEM 3: 

# Write a function that takes in two sorted lists. Merge them into one sorted 
# list. For example: 
    # input --> [1, 3], [2, 8, 10]
    # output --> [1, 2, 3, 8, 10]

    # This function should run in O(n) runtime. 

# This solution works, BUT it has a runtime of O(log n), so I need to re-do this...
def merge_and_sort(list1, list2):
    return sorted(list1 + list2)


 # Solution with O(n) runtime: 
    # Hint: Think of using two separate counters to keep track of where I'm at

def merge_sorted_lists(nums_1, nums_2):
  
   merged_list = []
   i = j = 0
  
   while i < len(nums_1) and j < len(nums_2):
      
       if nums_1[i] <= nums_2[j]:
           merged_list.append(nums_1[i])
           i += 1
       else:
           merged_list.append(nums_2[j])
           j += 1
  
   merged_list += nums_1[i:] + nums_2[j:]
  
   return merged_list


# A problem we didn't get to: 

# You are given an array of prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# There is a fairly straightforward O(n^2) solution, but the best solution has a runtime of O(n).

# Example 1:

# Input: prices = [7,1,5,3,6,4]

# Output: 5

# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5. Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Example 2:

# Input: prices = [7,6,4,3,1]

# Output: 0

# Explanation: In this case, no transactions are done because the price always goes down, and the max profit = 0.

# Hint1:
# For the O(n) solution – as you loop through the list, keep track of two values: the lowest (best) buy price so far, and the max profit so far.




