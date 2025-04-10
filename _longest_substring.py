def lengthOfLongestSubstring(s):
    # Initialize an empty dictionary to keep track of the last index of each character
    checklist = {}
    # Initialize the starting index of the current substring without repeating characters
    starting_index_of_current_substring = 0
    # Initialize the length of the longest substring found so far
    length_of_longest_substring = 0
    
    # Loop through each character in the string 's'
    for i, v in enumerate(s):
        # If the character 'v' is already in the checklist dictionary
        if v in checklist:
            # Check if the last occurrence of 'v' is within the current substring
            if checklist[v] >= starting_index_of_current_substring:
                # Update the starting index of the current substring to the index right after the last occurrence of 'v'
                starting_index_of_current_substring = checklist[v] + 1
        
        # Calculate the length of the current substring
        length_of_current_substring = i - starting_index_of_current_substring + 1
        # Update the length of the longest substring if the current substring is longer
        length_of_longest_substring = max(length_of_current_substring, length_of_longest_substring)
        # Update the last index of the character 'v' in the checklist dictionary
        checklist[v] = i
    
    # Return the length of the longest substring without repeating characters
    return length_of_longest_substring
def lengthOfLongestSubstring(s):
    # Initialize an empty dictionary to keep track of the last index of each character
    checklist = {}
    # Initialize the starting index of the current substring without repeating characters
    starting_index_of_current_substring = 0
    # Initialize the length of the longest substring found so far
    length_of_longest_substring = 0
    
    # Loop through each character in the string 's'
    for i, v in enumerate(s):
        # If the character 'v' is already in the checklist dictionary
        if v in checklist:
            # Check if the last occurrence of 'v' is within the current substring
            if checklist[v] >= starting_index_of_current_substring:
                # Update the starting index of the current substring to the index right after the last occurrence of 'v'
                starting_index_of_current_substring = checklist[v] + 1
        
        # Calculate the length of the current substring
        length_of_current_substring = i - starting_index_of_current_substring + 1
        # Update the length of the longest substring if the current substring is longer
        length_of_longest_substring = max(length_of_current_substring, length_of_longest_substring)
        # Update the last index of the character 'v' in the checklist dictionary
        checklist[v] = i
    
    # Return the length of the longest substring without repeating characters
    return length_of_longest_substring
