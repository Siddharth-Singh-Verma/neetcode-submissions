
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []  # indices of unresolved days

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev_i = stack.pop()
                ans[prev_i] = i - prev_i
            stack.append(i)

        return ans