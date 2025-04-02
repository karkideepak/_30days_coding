def twoSum(nums, target):
	hashmap = {}

	for index, num in enumerate(nums):
		if target - num in hashmap:
			return index, hashmap[target - num]
		hashmap[num]=index
	return None
"""
Question:
Given an array of integers nums and an integer target
Return indices of the two numbers such that they add up to target

Assume each input would have exactly one solution
Not allowed to use the same element twice

Example:
Input: nums = [2, 7, 11, 15] target = 9
Solution [2, 7]
Index[0] and index[1]
Output = [0,1]

Brute Force:
We loop through each number of array, and find another number that
add upto the target. This is n^2.


Data Structure: HashMap
Have I seen this value before! So that we don't have to go through the
array twice

Lookup: O(1)
Insert: O(1)

HashMap Data Structure 
Trying to find taret - value is it in the array.
8 - 3 = 5 ,is 5 in the hashtable
8 - 4 = 4 , this is in the array

HashMap
Key| Value
3 | 0
4 | 1
7 | 2

Output = [3,1]

"""


