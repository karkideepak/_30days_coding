def word_break(s, word_dict):
    """
    Determines if a string can be segmented into a space-separated sequence of one or more dictionary words.

    Args:
        s (str): The input string.
        word_dict (list): A list of words in the dictionary.

    Returns:
        bool: True if s can be segmented, False otherwise.
    """
    dp = [False] * (len(s) + 1)
    dp[0] = True
    
    for i in range(1, len(s) + 1):
        for w in word_dict:
            if dp[i - len(w)] and s[i-len(w):i] == w:
                dp[i] = True
                break
    return dp[-1]

