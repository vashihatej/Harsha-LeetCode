class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        result = 0

        for i in range(1, n - 1):
            # Check if arr[i] is a peak
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:

                # Expand LEFT — how far does the uphill stretch?
                left = i
                while left > 0 and arr[left] > arr[left - 1]:
                    left -= 1

                # Expand RIGHT — how far does the downhill stretch?
                right = i
                while right < n - 1 and arr[right] > arr[right + 1]:
                    right += 1

                # Mountain length = right - left + 1
                mountain_len = right - left + 1
                result = max(result, mountain_len)

        return result
