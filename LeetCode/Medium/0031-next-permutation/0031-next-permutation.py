class Solution:
    def nextPermutation(self, nums):
        """
        Rearranges nums into the next lexicographically greater permutation.
        Modifies the array in-place.
        """

        n = len(nums)

        # ============================================================
        # ✅ Step 1: Find the first decreasing element from the right
        #
        # Scan from right → left.
        #
        # Find first index i such that:
        #       nums[i] < nums[i+1]
        #
        # This index is called the "pivot".
        #
        # Why?
        # Because everything to the right of i is in descending order.
        #
        # Example 1:
        # nums = [1,2,3]
        #
        # From right:
        # 3 > nothing
        # 2 < 3  ✅ pivot = index 1
        #
        # Example 2:
        # nums = [3,2,1]
        #
        # From right:
        # 2 > 1
        # 3 > 2
        #
        # No such i exists.
        #
        # That means the array is completely descending.
        # So it's the LAST permutation.
        # Answer → reverse entire array.
        # ============================================================

        pivot = -1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot = i
                break

        # ============================================================
        # ✅ Step 2: Find the next bigger element to swap
        #
        # If pivot exists:
        #
        # From right side again, find first element j such that:
        #
        #       nums[j] > nums[pivot]
        #
        # Swap them.
        #
        # Why search from right?
        #
        # Because the right side is descending.
        # So the first element greater than nums[pivot]
        # is the SMALLEST possible greater value.
        #
        # Example:
        # nums = [2,3,1]
        #
        # Step 1 → pivot = 0 (value = 2)
        #
        # From right:
        # 1 <= 2
        # 3 > 2  ✅ swap with 3
        #
        # After swap:
        # [3,2,1]
        # ============================================================

        if pivot != -1:
            for j in range(n - 1, pivot, -1):
                if nums[j] > nums[pivot]:
                    nums[pivot], nums[j] = nums[j], nums[pivot]
                    break

        # ============================================================
        # ✅ Step 3: Reverse the suffix
        #
        # After swapping, everything to the right of pivot
        # is still in descending order.
        #
        # To get the NEXT permutation (smallest increase),
        # we must make that suffix as SMALL as possible.
        #
        # So we reverse it.
        #
        # Example continued:
        # After swap:
        # [3,2,1]
        #
        # Suffix after pivot index 0 → [2,1]
        #
        # Reverse suffix:
        # [1,2]
        #
        # Final result:
        # [3,1,2]
        # ============================================================

        left = pivot + 1
        right = n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


    # ============================================================
    # 🔥 Full Example Walkthrough
    #
    # nums = [1,2,3]
    #
    # Step 1:
    # pivot = 1 (because 2 < 3)
    #
    # Step 2:
    # swap 2 and 3 → [1,3,2]
    #
    # Step 3:
    # reverse suffix after index 1
    # suffix = [2]
    # no change
    #
    # Final → [1,3,2]
    #
    # ------------------------------------------------------------
    #
    # nums = [3,2,1]
    #
    # Step 1:
    # no pivot found (completely descending)
    #
    # Step 2:
    # skip
    #
    # Step 3:
    # reverse whole array → [1,2,3]
    #
    # Final → [1,2,3]
    # ============================================================