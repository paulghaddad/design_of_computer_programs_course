def longest_subpalindrome_slice(string):
    normalized_string = string.lower()

    longest_subpalindrome = (0,0)
    for i, starting_letter in enumerate(normalized_string):
        for x, ending_letter in enumerate(normalized_string[i:]):
            substring = normalized_string[i:i+x+1]
            print(substring)

            if _palindrome(substring):
                if len(substring) > (longest_subpalindrome[1] - longest_subpalindrome[0]):
                    print(f"Longest Palindrom! {substring}")
                    longest_subpalindrome = (i, i+x+1)

    return longest_subpalindrome


def _palindrome(string):
    reversed_string = ''
    for letter in reversed(string):
        reversed_string += letter

    return string == reversed_string
