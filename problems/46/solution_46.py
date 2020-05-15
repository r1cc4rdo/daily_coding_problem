'''
This problem was asked by Amazon.
Given a string, find the longest palindromic contiguous substring.
If there are more than one with the maximum length, return any one.
For example, the longest palindromic substring of "aabcdcb" is "bcdcb".
The longest palindromic substring of "bananas" is "anana".
'''

#________________________________________________________________

def is_palindrome(x):  # checks if a string is palindrome
    for i in range(len(x)//2):
        if x[i] != x[-1 - i]: return False
    else: return True

string, long_palindromes = input(), (("", 0),)  # 'long_palindromes' is the tuple of longest palindrome
substrings = [string[i: i+j] for i in range(len(string)) for j in range(1, len(string) - i + 1)]  # finding all substrings in the input string

for substring in substrings:
    if is_palindrome(substring) and len(substring) > long_palindromes[-1][-1]: long_palindromes = ((substring, len(substring)),)  # when substring (which is a palindrome) of length greater than that of the previous one is found
    elif is_palindrome(substring) and len(substring) == long_palindromes[-1][-1]: long_palindromes = long_palindromes + ((substring, len(substring)),)  # when substring (which is a palindrome) of length equal to that of the previous one is found

for long_palindrome in set(long_palindromes): print(long_palindrome[0])  # typecast to set to remove duplicate palindromes, if exist
