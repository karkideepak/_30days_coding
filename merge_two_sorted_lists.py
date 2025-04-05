# Step 1: Define the two sorted lists
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]

# Step 2: Create an empty list to store the merged result
merged_list = []

# Step 3: Use two pointers (indexes) to track positions in both lists
i = 0  # pointer for list1
j = 0  # pointer for list2

# Step 4: Loop until we reach the end of one list
while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
        merged_list.append(list1[i])  # take from list1
        i += 1  # move pointer i forward
    else:
        merged_list.append(list2[j])  # take from list2
        j += 1  # move pointer j forward

# Step 5: Add the remaining elements from list1 (if any)
while i < len(list1):
    merged_list.append(list1[i])
    i += 1

# Step 6: Add the remaining elements from list2 (if any)
while j < len(list2):
    merged_list.append(list2[j])
    j += 1

# Step 7: Print the final merged list
print("Merged List:", merged_list)
