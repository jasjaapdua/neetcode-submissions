class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        left, right = 0, m - 1

        candidate_row = None

        while left <= right:
            print(left, right)
            middle = (left + right) // 2
            
            candidate_row = matrix[middle]

            if target >= candidate_row[0] and target <= candidate_row[-1]:
                break
            
            elif target < candidate_row[0]:
                right = middle - 1

            elif target > candidate_row[-1]:
                left = middle + 1
        
        print(candidate_row)
        left, right = 0, n - 1

        while left <= right:
            middle = (left + right) // 2

            candidate = candidate_row[middle]

            if target == candidate:
                return True
            
            elif target > candidate:
                left = middle + 1

            elif target < candidate:
                right = middle - 1
        
        return False