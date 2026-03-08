class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        #O(N*N)
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


#O(N)
"""
Build two arrays:

up[i] = number of consecutive increasing steps ending at i (going left to right)
down[i] = number of consecutive decreasing steps starting at i (going right to left)

arr  = [2, 1, 4, 7, 3, 2, 5]
index   0  1  2  3  4  5  6

up:    [0, 0, 1, 2, 0, 0, 1]
        ↑  ↑  ↑  ↑  ↑  ↑  ↑
        no 1<2 4>1 7>4 3<7 2<3 5>2
        up NO  1   2   no  no  1
                   step step

down:  [0, 0, 0, 2, 1, 0, 0]
                  ↑  ↑
                 7>3 3>2  (reading right to left)
                 and 3>2
                 so 2 steps

If both up[i] > 0 AND down[i] > 0, then i is a peak!
Mountain length at i = up[i] + down[i] + 1  (left slope + right slope


Ex Walhthrough
arr  = [2, 1, 4, 7, 3, 2, 5]
index   0  1  2  3  4  5  6

Building up[] (left to right):
  i=0: base case               up[0] = 0
  i=1: arr[1]=1 > arr[0]=2? NO  up[1] = 0
  i=2: arr[2]=4 > arr[1]=1? YES up[2] = up[1] + 1 = 1
  i=3: arr[3]=7 > arr[2]=4? YES up[3] = up[2] + 1 = 2
  i=4: arr[4]=3 > arr[3]=7? NO  up[4] = 0   ← climb broke
  i=5: arr[5]=2 > arr[4]=3? NO  up[5] = 0
  i=6: arr[6]=5 > arr[5]=2? YES up[6] = up[5] + 1 = 1

  up = [0, 0, 1, 2, 0, 0, 1]

Building down[] (right to left):
  i=6: base case                  down[6] = 0
  i=5: arr[5]=2 > arr[6]=5? NO   down[5] = 0
  i=4: arr[4]=3 > arr[5]=2? YES  down[4] = down[5] + 1 = 1
  i=3: arr[3]=7 > arr[4]=3? YES  down[3] = down[4] + 1 = 2
  i=2: arr[2]=4 > arr[3]=7? NO   down[2] = 0
  i=1: arr[1]=1 > arr[2]=4? NO   down[1] = 0
  i=0: arr[0]=2 > arr[1]=1? YES  down[0] = down[1] + 1 = 1

  down = [1, 0, 0, 2, 1, 0, 0]

Finding mountains (need both up[i] > 0 AND down[i] > 0):
  i=0: up=0, skip (also can't be peak at edges)
  i=1: up=0, down=0, skip
  i=2: up=1, down=0, skip (goes up but doesn't come down)
  i=3: up=2, down=2, MOUNTAIN! length = 2 + 2 + 1 = 5 ✓
  i=4: up=0, down=1, skip (goes down but never went up)
  i=5: up=0, down=0, skip
  i=6: up=1, skip (edge)

Result = 5 ✓

Mountain at i=3:  up=2 means "climbed 2 steps to get here" (1→4→7)
                  down=2 means "descends 2 steps from here" (7→3→2)
                  Total: [1, 4, 7, 3, 2] = 5 elements

"""

def longestMountain_updown(arr):
    n = len(arr)
    if n < 3:
        return 0

    # up[i] = how many consecutive increasing steps end at i
    # "I've been going UP for this many steps to reach i"
    up = [0] * n
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            up[i] = up[i - 1] + 1
        # else: up[i] stays 0 (the climb resets)

    # down[i] = how many consecutive decreasing steps start at i
    # "From i, I can go DOWN for this many steps"
    down = [0] * n
    for i in range(n - 2, -1, -1):  # right to left
        if arr[i] > arr[i + 1]:
            down[i] = down[i + 1] + 1
        # else: down[i] stays 0

    # A mountain at index i needs BOTH an uphill and downhill
    result = 0
    for i in range(1, n - 1):
        if up[i] > 0 and down[i] > 0:
            mountain_len = up[i] + down[i] + 1
            result = max(result, mountain_len)

    return result
