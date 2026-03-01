from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # ------------------------------------------
        # Helper function to find leftmost position
        # ------------------------------------------
        def findFirst():
            l, r = 0, len(nums) - 1
            index = -1

            while l <= r:
                mid = (l + r) // 2

                if nums[mid] == target:
                    index = mid      # record potential answer
                    r = mid - 1      # move left to find earlier occurrence
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1

            return index

        # ------------------------------------------
        # Helper function to find rightmost position
        # ------------------------------------------
        def findLast():
            l, r = 0, len(nums) - 1
            index = -1

            while l <= r:
                mid = (l + r) // 2

                if nums[mid] == target:
                    index = mid      # record potential answer
                    l = mid + 1      # move right to find later occurrence
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1

            return index

        return [findFirst(), findLast()]



        # USING LEFT AND RIGHT BISECT
        #  # -------------------------------------------------
        # # Find first element >= target  (bisect_left logic)
        # # -------------------------------------------------
        # def bisect_left():
        #     lo, hi = 0, len(nums)

        #     while lo < hi:
        #         mid = (lo + hi) // 2

        #         if nums[mid] >= target:
        #             hi = mid
        #         else:
        #             lo = mid + 1

        #     return lo

        # # -------------------------------------------------
        # # Find first element > target  (bisect_right logic)
        # # -------------------------------------------------
        # def bisect_right():
        #     lo, hi = 0, len(nums)

        #     while lo < hi:
        #         mid = (lo + hi) // 2

        #         if nums[mid] > target:
        #             hi = mid
        #         else:
        #             lo = mid + 1

        #     return lo

        # left = bisect_left()

        # # 🔥 Important: verify target exists
        # if left == len(nums) or nums[left] != target:
        #     return [-1, -1]

        # # right boundary is one before first > target
        # right = bisect_right() - 1

        # return [left, right]