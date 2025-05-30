"""
word_counter.py
---------------
A simple utility script that counts the number of words in a user-input string.

Usage:
    python word_counter.py
"""

import re

def count_words(text: str) -> int:
    """
    Counts the number of words in the input text.
    Words are defined as sequences of alphanumeric characters separated by whitespace or punctuation.

    Args:
        text (str): The input string.

    Returns:
        int: The number of words.
    """
    # Use regex to find words (alphanumeric sequences)
    words = re.findall(r'\b\w+\b', text)
    return len(words)

def main():
    user_input = input("Enter your text: ").strip()
    if not user_input:
        print("Input is empty. Word count: 0")
        return

    word_count = count_words(user_input)
    print(f'Input Text: "{user_input}"')
    print(f'Word Count: {word_count}')

if __name__ == "__main__":
    main()