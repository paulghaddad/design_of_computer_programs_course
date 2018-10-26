def longest_subpalindrome_slice(string):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    normalized_string = string.lower()

    longest_subpalindrome = (0,0)

    left_edge, right_edge = 0, len(normalized_string) - 1
    for i, starting_letter in enumerate(normalized_string):
        k = 0
        while (i -k >= left_edge) and (i + k <= right_edge):
            print(f"{i} {starting_letter}")
            print(f"Left: {i - k} {normalized_string[i-k]}")
            print(f"Right: {i + k} {normalized_string[i+k]}")
            substring = normalized_string[i-k:i+k+1]
            if _palindrome(substring):
                print(f"Palindrome! {substring}")
                if len(substring) > (longest_subpalindrome[1] - longest_subpalindrome[0]):
                    longest_subpalindrome = (i-k, i+k+1)
            k += 1

    return longest_subpalindrome



    # for i, starting_letter in enumerate(normalized_string):
    #     for x, ending_letter in enumerate(normalized_string[i:]):
    #         substring = normalized_string[i:i+x+1]
    #
    #         if _palindrome(substring):
    #             if len(substring) > (longest_subpalindrome[1] - longest_subpalindrome[0]):
    #                 longest_subpalindrome = (i, i+x+1)
    #
    # return longest_subpalindrome


def _palindrome(string):
    "Return a Boolean indicating whether the string is a palindrome."
    reversed_string = ''
    for letter in reversed(string):
        reversed_string += letter

    return string == reversed_string
