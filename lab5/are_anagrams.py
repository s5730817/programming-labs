def are_anagrams(str1, str2):
    """
    This function checks if two strings are anagrams of each other.

    Parameters:
    ----------
    str1 : str
        The first string to be compared.
    str2 : str
        The second string to be compared.

    Returns:
    -------
    bool:
        Returns True if the two strings are anagrams, otherwise False.

    Example:
    --------
    are_anagrams("listen", "silent")  # Output: True
    are_anagrams("hello", "world")    # Output: False
    """

    # Function implementation here ...
    output = True
    
    if len(str1) != len(str2):
        output = False
    else:
        for i in str1:
            if i in str2:
                continue
            else:
                output = False
                break
    return output

## Example 
# print(are_anagrams("listen", "silent"))  # Expected output: True
# print(are_anagrams("hello", "world"))    # Expected output: False
