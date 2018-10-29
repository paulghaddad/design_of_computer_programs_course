def longest_subpalindrome_slice(string):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    normalized_string = string.lower()

    longest_subpalindromes = []
    left_edge, right_edge = 0, 2*len(normalized_string) - 1

    for i in range(right_edge):
        if i % 2 == 0:
            longest_subpalindromes.append(_grow(normalized_string, i, i))
        # else:
        #     k = 0
        #     while (i-k >= left_edge) and (i+k < right_edge):
        #         substring = normalized_string[(i-k)//2:(i+k)//2+2]
        #         if _palindrome(substring):
        #             if len(substring) > (longest_subpalindrome[1] - longest_subpalindrome[0]):
        #                 longest_subpalindrome = ((i-k)//2, (i+k)//2+2)
        #         else:
        #             break
        #         k += 2

    return max(longest_subpalindromes, key=length)

def length(subpalindrome):
    return subpalindrome[1] - subpalindrome[0]

def _grow(text, start, end):
    while (start >= 0 and end < 2*len(text) - 1 and text[(start//2)] == text[(end//2)]):
        start -= 2; end += 2

    return (start//2+1, end//2)


def _palindrome(string):
    "Return a Boolean indicating whether the string is a palindrome."
    reversed_string = ''
    for letter in reversed(string):
        reversed_string += letter

    return string == reversed_string
