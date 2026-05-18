# Two Sum — LeetCode #1 | Easy | Arrays & Hashing

## Problem
Given an array of integers `nums` and an integer `target`, return indices of the two numbers that add up to `target`.

## Approach
Use a HashMap to store each number and its index as we iterate.
For each number, check if its complement (`target - num`) already exists in the map.
This avoids the O(n²) brute force nested loop.

## Pattern
**HashMap for O(1) Lookup** — See PATTERNS.md → Arrays & Hashing

## Solution

```python
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}  # value -> index
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        
        return []  # no solution found
```

## Complexity
- **Time:** O(n) — single pass through array
- **Space:** O(n) — HashMap stores up to n elements

## Key Insight
Don't reach for nested loops when you need to find pairs.
If you need "have I seen X before?", a HashMap gives you the answer in O(1).

## Similar Problems
- #167 Two Sum II (sorted array → Two Pointers instead)
- #15 3Sum
- #560 Subarray Sum Equals K
