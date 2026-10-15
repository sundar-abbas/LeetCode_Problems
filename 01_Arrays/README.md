# Arrays & Hashing

## Concepts I Learned

- Access elements using indexes.
- Use nested loops to compare elements.
- `range(len(nums))` loops through indexes.
- `range(x + 1, len(nums))` avoids comparing the same element twice.
- Backward iteration with step `-1` using `range(start, stop, -1)`.
- Set removes duplicate values but destroys original order.
- In-place slice modification (`nums[:k] = ...`) alters the original list without allocating new memory.
- Running Sum of 1d Array.
- Zero-Based Permutation (No missing numbers, starts at 0, no repeats).
- Math carry-over handling by resetting digits to 0 during array traversal.
- Merging sorted arrays by overwriting trailing empty space and re-sorting.
- Single-Pass Optimization (O(N)): Reducing an $O(N^2)$ nested loop problem to a linear $O(N)$ single loop by using dynamic tracking.
- Dynamic Variable Tracking: Maintaining running global values (like `min_price` and `max_profit`) while walking through an array from left to right.

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

### 008. Shuffle the Array

- **Difficulty:** Easy
- **Approach:** Array Slicing & Zipping with List Comprehension.
- **My Solution:** Split the array into two halves, paired the elements using the `zip` function, and flattened the pairs into a single list using a nested list comprehension.
- **Complexity:** Time: O(N) | Space: O(N) to store the slices and the final zipped result
- **Optimization:** Streamlined the index-tracking loop into a pythonic, clean one-liner that interleaves both halves in a single pass.
- **LeetCode Link:** https://leetcode.com/problems/shuffle-the-array/
- **Date Solved:** 2026-07-25

### 009. Concatenation Of Array

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

### 011. Remove Duplicates from Sorted Array

- **Difficulty:** Easy
- **Approach:** Type Conversion & In-Place Slice Assignment.
- **My Solution:** Filtered unique elements via `set()`, sorted them back into order, and modified the original array's prefix using python slice assignment (`nums[:k]`).
- **Complexity:** Time: O(N log N) due to the sorting step | Space: O(N) to hold the unique list values temporarily
- **Optimization:** Can be optimized to O(N) time and O(1) space using a traditional two-pointer approach to leverage the already sorted input array.
- **LeetCode Link:** https://leetcode.com/problems/remove-duplicates-from-sorted-array/
- **Date Solved:** 2026-07-28

### 012. Remove Element

- **Difficulty:** Easy
- **Approach:** Shallow Copy Iteration.
- **My Solution:** Iterated over a shallow copy of the list (`nums[:]`) to safely call `nums.remove(x)` without skipping elements during deletion.
- **Complexity:** Time: O(N²) due to nested removal scans | Space: O(N) to hold the shallow copy
- **Optimization:** Can be optimized to O(N) time and O(1) space using a two-pointer technique to overwrite values in-place without deleting or copying.
- **LeetCode Link:** https://leetcode.com/problems/remove-element/
- **Date Solved:** 2026-07-29

### 013. Plus One

- **Difficulty:** Easy
- **Approach:** In-Place Backward Iteration.
- **My Solution:** Iterated backward from the last digit. If a digit is less than 9, incremented it by 1 and returned early. If it equals 9, reset it to 0 to handle the carry-over. Handled edge cases (all 9s) by appending 1 to the front.
- **Complexity:** Time: O(N) | Space: O(1) auxiliary space (O(N) worst-case if creating a new list for carry overflow)
- **Optimization:** This solution is highly optimal as it processes elements in-place without converting types to strings or big integers.
- **LeetCode Link:** https://leetcode.com/problems/plus-one/
- **Date Solved:** 2026-07-30

### 014. Merge Sorted Array

- **Difficulty:** Easy
- **Approach:** Append and Sort.
- **My Solution:** Overwrote the trailing placeholder elements of the first array with all elements of the second array via index injection, then sorted the combined list in-place.
- **Complexity:** Time: O((M + N) log(M + N)) due to the sorting step | Space: O(1) auxiliary space as the operation is done entirely within `nums1`
- **Optimization:** Can be optimized to O(M + N) time by utilizing a three-pointer approach that works backward from the end of `nums1` to place elements without sorting.
- **LeetCode Link:** https://leetcode.com/problems/merge-sorted-array/
- **Date Solved:** 2026-07-31

### 015. Best Time to Buy and Sell Stock

- **Difficulty:** Easy
- **Approach:** Single Pass / Dynamic Tracking (Greedy).
- **My Solution:** Iterated through the list once. Maintained a running `buy_price` to lock in the lowest historical price seen so far, and dynamically updated the maximum `profit` whenever a day yielded a larger price spread.
- **Complexity:** Time: O(N) | Space: O(1)
- **Optimization:** Successfully optimized from an $O(N^2)$ brute-force double-loop calculation to an optimal single pass, avoiding the "Time Limit Exceeded" constraint.
- **LeetCode Link:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
- **Date Solved:** 2026-08-01

### 016. Majority Element

- **Difficulty:** Easy
- **Approach:** Boyer-Moore Voting Algorithm.
- **My Solution:** Iterated through the array tracking a `maj_num` candidate and a balance `count`. Reset the candidate whenever the count dropped to zero, and incremented or decremented the tracker depending on whether the current number matched the candidate.
- **Complexity:** Time: O(N) \| Space: O(1)
- **Optimization:** Optimized from an O(N) space hash map implementation to O(1) auxiliary space by using the cancelation properties of a true majority element, fulfilling the linear time and constant space constraint.
- **LeetCode Link:** https://leetcode.com/problems/majority-element/
- **Date Solved:** 2026-08-02

### 017. Remove Zeroes

- **Difficulty:** Easy
- **Approach:** Two-Pointer (Read/Write Index)
- **My Solution:** Maintained a `write_ptr` tracking the position for the next non-zero element. Iterated through the array, writing any non-zero values to `write_ptr` and advancing it. Filled all remaining indices up to the end of the array with zeroes.
- **Complexity:** Time: O(N) | Space: O(1)
- **Optimization:** Avoided the $O(N^2)$ complexity of standard array mutations (`pop` or `remove`) by modifying elements directly by index in-place, achieving an optimal single-pass style rewrite with constant extra space.
- **LeetCode Link:** https://leetcode.com/problems/move-zeroes/
- **Date Solved:** 2026-08-03

### 018. Squares of a Sorted Array

- **Difficulty:** Easy
- **Approach:** In-Place Modification & Sorting
- **My Solution:** Iterated through the list using index-based tracking (`range(len(nums))`) to directly square each element in-place, bypassing temporary loop variable copies. Sorted the mutated array exactly once after the loop completed.
- **Complexity:** Time: $O(N \log N)$ | Space: $O(1)$
- **Optimization:** Conserved memory by modifying the input array in-place, though performance can be further optimized from $O(N \log N)$ to a linear $O(N)$ single-pass solution using a Two-Pointer approach to leverage the initial sorted state of the array.
- **LeetCode Link:** https://leetcode.com/problems/squares-of-a-sorted-array/
- **Date Solved:** 2026-08-10

### 019. Third Maximum Number

- **Difficulty:** Easy
- **Approach:** Deduplication & Sorting
- **My Solution:** Eliminated duplicates by converting the array into a `set()`, transformed it back into a list, and sorted it in ascending order. If the deduplicated list contains fewer than 3 elements, it returns the absolute maximum (`unique_list[-1]`). Otherwise, it returns the third maximum element (`unique_list[-3]`).
- **Complexity:** Time: (O(N \log N)) due to sorting the unique elements | Space: \(O(N)\) to store unique elements in the set and list
- **Optimization:** This can be optimized to linear time \(O(N)\) and constant space \(O(1)\) by tracking the top three distinct maximum values using three independent pointer variables in a single pass.
- **LeetCode Link:** https://leetcode.com/problems/third-maximum-number
- **Date Solved:** 2026-10-15
