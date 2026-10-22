# Strings

## Concepts I Learned
- Anagram
- Palindrome

## Problems Solved

### 001. Valid Anagram

- **Difficulty:** Easy
- **Approach:** Sorting (\(O(n \log n)\)) OR Hashmap (O(n)).
- **My Solution:** Used the built-in `sorted()` function to compare alphabetical representations.
- **Optimization:** Could use a hashmap (`collections.Counter` in Python) to count character frequencies in O(n) time.
- **LeetCode Link:** https://leetcode.com/problems/valid-anagram/
- **Date Solved:** 2026-07-16

### 002. Valid Palindrome

- **Difficulty:** Easy
- **Approach:** String Slicing (O(n) time, O(n) space).
- **My Solution:** Used a list comprehension combined with `.isalnum()` and `.lower()` to filter out special characters and spaces, then checked for equality against its reversed slice `[::-1]`.
- **Optimization:** Can be optimized to O(1) auxiliary space by using a **Two-Pointer technique**, moving pointers inward from both ends of the original string and skipping non-alphanumeric characters on the fly.
- **LeetCode Link:** https://leetcode.com/problems/valid-palindrome/
- **Date Solved:** 2026-10-22