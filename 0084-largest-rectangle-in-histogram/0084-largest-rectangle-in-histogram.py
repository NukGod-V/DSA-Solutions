class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #ind , high
        largest = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                ind, high = stack.pop()
                largest = max(largest,high * (i - ind))
                start = ind
            stack.append((start,h))
        for i, h in stack:
            largest = max(largest,h * (len(heights) - i))
        return largest