def longest_subpalindrome_slice(string):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    normalized_string = string.lower()

    longest_subpalindrome = (0,0)

    left_edge, right_edge = 0, len(normalized_string) + len(normalized_string) - 1
    for i in range(right_edge):
        print(i)

        if i % 2 == 0:
            k = 0
            while (i-k >= left_edge) and (i+k < right_edge):
                print(f"Even Left: {i - k} {normalized_string[(i-k)//2]}")
                print(f"Even Right: {i + k} {normalized_string[(i+k)//2]}")
                substring = normalized_string[(i-k)//2:(i+k)//2+1]
                if _palindrome(substring):

                    print(f"Palindrome! {substring}")
                    if len(substring) > (longest_subpalindrome[1] - longest_subpalindrome[0]):
                        longest_subpalindrome = ((i-k)//2, (i+k)//2+1)
                k += 2
        else:
            m = 0
            while (i-m >= left_edge) and (i+m < right_edge):
                print(f"Odd Left letter: {normalized_string[(i-m)//2]}")
                print(f"Odd Right letter: {normalized_string[(i+m)//2 + 1]}")
                substring = normalized_string[(i-m)//2:(i+m)//2+2]
                if _palindrome(substring):

                    print(f"Palindrome! {substring}")
                    if len(substring) > (longest_subpalindrome[1] - longest_subpalindrome[0]):
                        longest_subpalindrome = ((i-m)//2, (i+m)//2+2)
                m += 2

    return longest_subpalindrome


def _palindrome(string):
    "Return a Boolean indicating whether the string is a palindrome."
    reversed_string = ''
    for letter in reversed(string):
        reversed_string += letter

    return string == reversed_string
