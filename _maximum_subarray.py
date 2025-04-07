# Function to find the maximum sum subarray
def max_subarray(nums):
    # If the list is empty, we return 0 (or you could handle this case differently depending on your needs)
    if len(nums) == 0:
        return 0

    # Initialize two variables:
    # 1. `current_sum`: This will store the maximum sum of the subarray that ends at the current index.
    # 2. `max_sum`: This will store the maximum sum found so far.
    current_sum = nums[0]
    max_sum = nums[0]
    
    # Iterate through the array starting from the second element
    for i in range(1, len(nums)):
        # Update `current_sum` by deciding whether to add the current element to the existing subarray,
        # or start a new subarray from the current element.
        current_sum = max(nums[i], current_sum + nums[i])
        
        # Update the `max_sum` to be the maximum of the current `max_sum` and the updated `current_sum`
        max_sum = max(max_sum, current_sum)
        
    # Return the maximum subarray sum found
    return max_sum

# Example usage:
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray(nums)
print("The maximum sum of the subarray is:", result)
