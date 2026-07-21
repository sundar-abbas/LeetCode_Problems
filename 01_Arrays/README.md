# Arrays & Hashing

## Concepts I Learned

- Access elements using indexes.
- Use nested loops to compare elements.
- range(len(nums)) loops through indexes.
- range(x + 1, len(nums)) avoids comparing the same element twice.
- Set removes the duplicate values.
- Running Sum of 1d Array

## Problems Solved

### 001. Two Sum

- **Difficulty:** Easy
- **Approach:** Brute-force nested loops (O(n^2)) OR Hashmap (O(n)).
- **My Solution:** Used nested loops to check all pairs.
- **Optimization:** Could use a hashmap to check complement in O(n).
- **LeetCode Link:** https://leetcode.com/problems/two-sum/
- **Date Solved:** 2026-07-16

### 002. Contains Duplicate

- **Difficulty:** Easy
- **Approach:** Hash Set.
- **My Solution:** Used a hash Set .
- **Optimization:** Could use a Hash Map and also compare with set length .
- **LeetCode Link:** https://leetcode.com/problems/contains-duplicate/
- **Date Solved:** 2026-07-17

### 003. Running Sum of 1d Array

- **Difficulty:** Easy
- **Approach:** In-place Iteration.
- **My Solution:** Modified the input array in-place by adding the previous element to the current element.
- **Optimization:** Current solution is optimal at (O(1)) space, but could also use itertools.accumulate() for a one-liner.
- **LeetCode Link:** https://leetcode.com/problems/running-sum-of-1d-array/
- **Date Solved:** 2026-07-18

### 004. Richest Customer Wealth

- **Difficulty:** Easy
- **Approach:** Iterative Nested Loops.
- **My Solution:** Maintained a running maximum while iterating through every bank account row by row.
- **Complexity:** Time: O(M x N) | Space: O(1)
- **Optimization:** Can be written as a pythonic one-liner using `max(sum(row) for row in accounts)`.
- **LeetCode Link:** https://leetcode.com/problems/richest-customer-wealth/
- **Date Solved:** 2026-07-19

### 005. Find Pivot Index

- **Difficulty:** Easy
- **Approach:** Prefix Sum / Running Total.
- **My Solution:** Maintained a running left sum and compared it to the remaining right sum at each index.
- **Complexity:** Time: O(N) | Space: O(1)
- **Optimization:** Can be written in a single pass by subtracting the left sum and current element from the total sum.
- **LeetCode Link:** https://leetcode.com/problems/find-pivot-index/
- **Date Solved:** 2026-07-20

### 006. Find the Highest Altitude

- **Difficulty:** Easy
- **Approach:** Brute Force / Cumulative Re-calculation.
- **My Solution:** Iterated through all possible road trip points and recalculated the total cumulative altitude gain from the starting point using an inner loop.
- **Complexity:** Time: $O(N^2)$ | Space: $O(1)$
- **Optimization:** Can be optimized to $O(N)$ time in a single pass by maintaining a single running total variable (Prefix Sum) and updating the maximum altitude dynamically.
- **LeetCode Link:** https://leetcode.com/problems/find-the-highest-altitude/
- **Date Solved:** 2026-07-21
