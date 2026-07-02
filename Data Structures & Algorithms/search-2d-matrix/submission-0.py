class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        # Binary search to find the candidate row
        l, r = 0, m - 1
        while l <= r:
            mid = (l + r) // 2

            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                l = mid + 1
            else:
                r = mid - 1

        # r is the last row whose first element is <= target
        if r < 0:
            return False

        row = r

        # Optional but avoids unnecessary binary search
        if target > matrix[row][-1]:
            return False

        # Binary search within the row
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False