# Strings

## Concepts I Learned
- Anagram
- Palindrome
- Two-Pointer Technique

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

### 003. Reverse String

- **Difficulty:** Easy
- **Approach:** Two-Pointer Technique ($O(n)$ time, $O(1)$ space).
- **My Solution:** Implemented an in-place swap using a `while` loop with `left` and `right` pointers moving inward until they meet.
- **Optimization:** Already optimal for in-place modifications ($O(1)$ auxiliary space). Python also offers the native `s.reverse()` method or slicing `s[::-1]` (though slicing creates a new copy in memory).
- **LeetCode Link:** https://leetcode.com/problems/reverse-string/
- **Date Solved:** 2026-10-24