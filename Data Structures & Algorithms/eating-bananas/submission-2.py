class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        randommax = 999999999999999
        result = randommax
        def get_hours(k: int):
            hours = [
                math.ceil(pile / k) for pile in piles
            ]
            print(hours)
            return sum(hours)
        
        left, right = 1, max(piles)

        while left <= right:
            middle = (left + right) // 2
            hours = get_hours(middle)

            rate_is_valid = hours <= h

            if rate_is_valid:
                result = min(result, middle)
                right = middle - 1

            else:
                left = middle + 1
        
        # if result == randommax:
        #     return max(piles)
        return result
