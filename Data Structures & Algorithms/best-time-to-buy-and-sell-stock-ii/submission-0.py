from typing import List
from functools import lru_cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @lru_cache(None)
        def util(i: int, holding: int) -> int:
            if i == n:
                return 0

            # do nothing
            best = util(i + 1, holding)

            if holding:
                # sell
                best = max(best, prices[i] + util(i + 1, 0))
            else:
                # buy
                best = max(best, -prices[i] + util(i + 1, 1))

            return best

        return util(0, 0)
