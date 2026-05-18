# 🧩 DSA Patterns — Personal Cheat Sheet

> Add a new entry every time you solve a problem and identify its pattern.
> This file is worth more than any course after 2 months of consistent use.

**Format:**
```
### Problem Name (#LeetCode Number)
- Pattern: 
- Key Insight: 
- When to use this pattern: 
- Time: O(?) | Space: O(?)
- Similar problems: 
```

---

## 📦 Arrays & Hashing

### Pattern: HashMap for O(1) Lookup
- **When to use:** Any time you need to check "have I seen this before?" or find a complement/pair
- **Core idea:** Store values as keys in a dict → check existence in O(1) instead of scanning O(n)
- **Template:**
```python
seen = {}
for i, num in enumerate(nums):
    complement = target - num
    if complement in seen:
        return [seen[complement], i]
    seen[num] = i
```
- **Problems using this:** Two Sum, Group Anagrams, Valid Anagram

---

### Pattern: Frequency Count
- **When to use:** Comparing characters, finding duplicates, counting occurrences
- **Core idea:** Use `collections.Counter()` or a plain dict to count frequency
- **Template:**
```python
from collections import Counter
count = Counter(s)
# count['a'] gives frequency of 'a'
```
- **Problems using this:** Valid Anagram, Top K Frequent Elements, Group Anagrams

---

## 👉 Two Pointers

### Pattern: Left & Right Pointer (Opposite Ends)
- **When to use:** Sorted array, finding pairs, palindrome check, container problems
- **Core idea:** Start one pointer at 0, one at end. Move based on condition.
- **Template:**
```python
left, right = 0, len(arr) - 1
while left < right:
    if condition_met:
        return result
    elif need_larger:
        left += 1
    else:
        right -= 1
```
- **Problems using this:** Two Sum II, 3Sum, Container With Most Water, Valid Palindrome

---

### Pattern: Fast & Slow Pointer
- **When to use:** Cycle detection in linked list, finding middle of list
- **Core idea:** Slow moves 1 step, fast moves 2 steps. If they meet → cycle exists.
- **Template:**
```python
slow, fast = head, head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        return True  # cycle detected
return False
```
- **Problems using this:** Linked List Cycle, Find Duplicate Number

---

## 🪟 Sliding Window

### Pattern: Fixed Size Window
- **When to use:** "Subarray/substring of size k" problems
- **Core idea:** Maintain a window of exactly k elements. Add right, remove left.
- **Template:**
```python
window_sum = sum(nums[:k])
max_sum = window_sum
for i in range(k, len(nums)):
    window_sum += nums[i] - nums[i - k]
    max_sum = max(max_sum, window_sum)
```

---

### Pattern: Variable Size Window (Expand & Shrink)
- **When to use:** "Longest/shortest subarray with condition" problems
- **Core idea:** Expand right pointer, shrink left when condition violated
- **Template:**
```python
left = 0
result = 0
window = {}  # or a counter
for right in range(len(s)):
    # add s[right] to window
    window[s[right]] = window.get(s[right], 0) + 1
    
    while window_is_invalid:
        # remove s[left] from window
        window[s[left]] -= 1
        if window[s[left]] == 0:
            del window[s[left]]
        left += 1
    
    result = max(result, right - left + 1)
return result
```
- **Problems using this:** Longest Substring Without Repeating, Longest Repeating Char Replacement

---

## 📚 Stack

### Pattern: Monotonic Stack
- **When to use:** "Next greater/smaller element", temperature problems, stock span
- **Core idea:** Maintain a stack that is always increasing or decreasing
- **Template:**
```python
stack = []  # stores indices
result = [0] * len(temperatures)
for i, temp in enumerate(temperatures):
    while stack and temperatures[stack[-1]] < temp:
        idx = stack.pop()
        result[idx] = i - idx
    stack.append(i)
return result
```
- **Problems using this:** Daily Temperatures, Next Greater Element

---

### Pattern: Balanced Parentheses
- **When to use:** Matching brackets, validating expressions
- **Template:**
```python
stack = []
mapping = {')': '(', '}': '{', ']': '['}
for char in s:
    if char in mapping:
        top = stack.pop() if stack else '#'
        if mapping[char] != top:
            return False
    else:
        stack.append(char)
return not stack
```

---

## 🔍 Binary Search

### Pattern: Standard Binary Search
- **When to use:** Sorted array, find target or boundary
- **Template:**
```python
left, right = 0, len(nums) - 1
while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
return -1
```

---

### Pattern: Binary Search on Answer
- **When to use:** "Find minimum/maximum value that satisfies condition" — Koko, Capacity to Ship
- **Core idea:** Binary search over the *answer space*, not the array
- **Template:**
```python
def feasible(mid):
    # check if mid is a valid answer
    return True or False

left, right = min_possible, max_possible
while left < right:
    mid = (left + right) // 2
    if feasible(mid):
        right = mid       # try smaller
    else:
        left = mid + 1    # need larger
return left
```
- **Problems using this:** Koko Eating Bananas, Minimum Capacity to Ship

---

## 🔗 Linked List

### Pattern: Reverse a Linked List
- **Template:**
```python
prev, curr = None, head
while curr:
    next_node = curr.next
    curr.next = prev
    prev = curr
    curr = next_node
return prev
```

---

### Pattern: Find Middle of Linked List
- **Template:**
```python
slow, fast = head, head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
return slow  # slow is at middle
```

---

## 🌳 Trees

### Pattern: DFS on Binary Tree (Recursive)
- **When to use:** Height, diameter, path sum, tree validation
- **Template:**
```python
def dfs(node):
    if not node:
        return base_case
    
    left = dfs(node.left)
    right = dfs(node.right)
    
    # update global result if needed
    self.result = max(self.result, left + right)
    
    return 1 + max(left, right)  # return to parent
```

---

### Pattern: BFS on Binary Tree (Level Order)
- **When to use:** Level-by-level traversal, finding depth, zigzag traversal
- **Template:**
```python
from collections import deque
queue = deque([root])
result = []
while queue:
    level = []
    for _ in range(len(queue)):   # process entire level
        node = queue.popleft()
        level.append(node.val)
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
    result.append(level)
return result
```

---

## 📊 Graphs

### Pattern: BFS (Shortest Path / Level Traversal)
- **When to use:** Shortest path in unweighted graph, connected components
- **Template:**
```python
from collections import deque
visited = set()
queue = deque([start])
visited.add(start)
while queue:
    node = queue.popleft()
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
```

---

### Pattern: DFS on Grid (Islands Problem)
- **When to use:** Count connected components on a 2D grid
- **Template:**
```python
def dfs(grid, r, c):
    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
        return
    if grid[r][c] != '1':
        return
    grid[r][c] = '0'  # mark visited by modifying grid
    dfs(grid, r+1, c)
    dfs(grid, r-1, c)
    dfs(grid, r, c+1)
    dfs(grid, r, c-1)

count = 0
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == '1':
            dfs(grid, r, c)
            count += 1
return count
```

---

## 💡 Dynamic Programming

### Pattern: 1D DP (Bottom-Up)
- **When to use:** Fibonacci-style, house robber, climbing stairs
- **Template:**
```python
dp = [0] * (n + 1)
dp[0] = base_case_0
dp[1] = base_case_1
for i in range(2, n + 1):
    dp[i] = dp[i-1] + dp[i-2]  # or whatever recurrence
return dp[n]
```

---

### Pattern: 2D DP
- **When to use:** Grid paths, edit distance, longest common subsequence
- **Template:**
```python
dp = [[0] * (cols + 1) for _ in range(rows + 1)]
for i in range(1, rows + 1):
    for j in range(1, cols + 1):
        if condition:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
return dp[rows][cols]
```

---

## 🔙 Backtracking

### Pattern: General Backtracking Template
- **When to use:** Subsets, permutations, combinations, N-Queens
- **Template:**
```python
def backtrack(start, current):
    if is_solution(current):
        result.append(current[:])
        return
    for choice in choices_from(start):
        current.append(choice)       # make choice
        backtrack(start + 1, current)
        current.pop()                # undo choice

result = []
backtrack(0, [])
return result
```

---

## 🌲 Tries

### Pattern: Build and Search a Trie
- **Template:**
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end
```

---

## ⚡ Quick Reference — "Which Pattern Is This?"

| Problem Says... | Think... |
|---|---|
| "Find pair that sums to X" | HashMap or Two Pointers |
| "Subarray with condition" | Sliding Window |
| "Sorted array, find target" | Binary Search |
| "Linked list cycle" | Fast & Slow Pointer |
| "Tree height / path" | DFS Recursion |
| "Level by level" | BFS + Queue |
| "Number of islands / connected components" | DFS on Grid |
| "Next greater element" | Monotonic Stack |
| "All subsets / permutations" | Backtracking |
| "Min/max over choices with overlapping subproblems" | Dynamic Programming |
| "Prefix search / word dictionary" | Trie |
| "Top K elements" | Heap / Priority Queue |

---

*This file grows with you. Every new pattern you discover → add it here.*
