# Arrays & Hashing

## Concepts I Learned

- Access elements using indexes.
- Use nested loops to compare elements.
- range(len(nums)) loops through indexes.
- range(x + 1, len(nums)) avoids comparing the same element twice.
- Set removes the duplicate values.
- Running Sum of 1d Array
- Zero-Based Permutation (No missing numbers, starts at 0, no repeats).

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

### 007. Kids with the Greatest Number of Candies

- **Difficulty:** Easy
- **Approach:** Maximum Element Tracking & Single Pass.
- **My Solution:** Found the maximum candy count in the array first, then iterated through each child once to check if their candies plus the extras met or exceeded that maximum.
- **Complexity:** Time: O(N) | Space: O(1) auxiliary space O(N) to store the result
- **Optimization:** Optimized from a nested loop O(N^2) brute-force approach to a linear O(N) time solution by eliminating the inner loop and using a pre-calculated maximum.
- **LeetCode Link:** https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
- **Date Solved:** 2026-07-24

### 8. Shuffle the Array

- **Difficulty:** Easy
- **Approach:** Array Slicing & Zipping with List Comprehension.
- **My Solution:** Split the array into two halves, paired the elements using the `zip` function, and flattened the pairs into a single list using a nested list comprehension.
- **Complexity:** Time: O(N) | Space: O(N) to store the slices and the final zipped result
- **Optimization:** Streamlined the index-tracking loop into a pythonic, clean one-liner that interleaves both halves in a single pass.
- **LeetCode Link:** https://leetcode.com/problems/shuffle-the-array/
- **Date Solved:** 2026-07-25

### 9. Concatenation Of Array

- **Difficulty:** Easy
- **Approach:** List Duplication & Iterative Append.
- **My Solution:** Created an initial copy of the input list and iterated through the original elements, appending each one to the copy to double the array's length.
- **Complexity:** Time: O(N) | Space: O(N) to store the duplicated elements in the final result array
- **Optimization:** Utilized a clean `for` loop to append elements sequentially, which can be further optimized into a one-liner like `nums * 2` or `nums + nums`.
- **LeetCode Link:** https://leetcode.com/problems/concatenation-of-array/
- **Date Solved:** 2026-07-26

### 010. Build Array From Permutation

- **Difficulty:** Easy
- **Approach:** Iterative Permutation Mapping / Treasure Hunt.
- **My Solution:** Iterated through the list using a `for` loop, nested the current element value inside the array index (`nums[nums[num]]`), and appended the targeted values to a new list.
- **Complexity:** Time: O(N) | Space: O(N) to store the elements in the new output array
- **Optimization:** Can be optimized into a clean list comprehension one-liner: `[nums[num] for num in nums]`.
- **LeetCode Link:** https://leetcode.com/problems/build-array-from-permutation/
- **Date Solved:** 2026-07-27
