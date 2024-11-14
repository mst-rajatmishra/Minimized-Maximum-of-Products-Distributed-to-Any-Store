from math import ceil

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        # Binary search boundaries
        left, right = 1, max(quantities)
        
        # Function to check if a certain max x is feasible
        def can_distribute(x):
            stores_needed = 0
            for quantity in quantities:
                stores_needed += ceil(quantity / x)
            return stores_needed <= n
        
        # Binary search for the smallest valid x
        while left < right:
            mid = (left + right) // 2
            if can_distribute(mid):
                right = mid  # mid is valid, try to minimize x
            else:
                left = mid + 1  # mid is not valid, increase x
        
        return left
