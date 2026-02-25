class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # ------------------------------------------------------------------
        # Always binary search on the smaller array
        # This keeps time complexity O(log(min(m, n)))
        # ------------------------------------------------------------------
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        total = m + n
        half = total // 2  # Number of elements that must be on LEFT side

        # Binary search boundaries for nums1 partition
        left = 0
        right = m

        while True:
            # --------------------------------------------------------------
            # i = partition index in nums1
            # j = partition index in nums2
            # We ensure:
            #     i + j = half
            # So left side has exactly half elements
            # --------------------------------------------------------------
            i = (left + right) // 2
            j = half - i

            # --------------------------------------------------------------
            # Handle edge cases carefully
            # If partition touches array boundary,
            # we use -inf or +inf so comparisons still work
            # --------------------------------------------------------------
            nums1_left_max  = nums1[i - 1] if i > 0 else float("-inf")
            nums1_right_min = nums1[i]     if i < m else float("inf")

            nums2_left_max  = nums2[j - 1] if j > 0 else float("-inf")
            nums2_right_min = nums2[j]     if j < n else float("inf")

            # --------------------------------------------------------------
            # Check if partition is correct
            # We need:
            #    left_max <= right_min (on both sides)
            # --------------------------------------------------------------
            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
                
                # -------------------------
                # If total is odd
                # Median is smallest value from right side
                # -------------------------
                if total % 2:
                    return min(nums1_right_min, nums2_right_min)
                
                # -------------------------
                # If total is even
                # Median is average of:
                #    max(left side) and min(right side)
                # -------------------------
                return (
                    max(nums1_left_max, nums2_left_max) +
                    min(nums1_right_min, nums2_right_min)
                ) / 2

            # --------------------------------------------------------------
            # If nums1_left_max is too big,
            # we moved too far right in nums1
            # So move partition LEFT
            # --------------------------------------------------------------
            elif nums1_left_max > nums2_right_min:
                right = i - 1

            # --------------------------------------------------------------
            # Otherwise,
            # we need more elements from nums1
            # So move partition RIGHT
            # --------------------------------------------------------------
            else:
                left = i + 1