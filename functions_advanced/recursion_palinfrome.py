def palindrome(text, idx):
    if idx == len(text) // 2:
        return f'{text} is a palindrome'
    if text[idx] != text[len(text) - 1 - idx]:
        return f'{text} is not a palindrome'
    return palindrome(text, idx + 1)

