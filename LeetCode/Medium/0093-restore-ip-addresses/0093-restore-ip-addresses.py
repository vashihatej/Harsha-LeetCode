class Solution:
    def restoreIpAddresses(self, s: str):
        result = []
        
        # ---------------------------------------------------
        # Backtracking function
        # index = current position in string
        # path = list of collected IP segments
        # ---------------------------------------------------
        def backtrack(index, path):
            
            # ------------------------------------------------
            # If we already have 4 parts like[255]
            # ------------------------------------------------
            if len(path) == 4:
                # Valid only if entire string is consumed
                if index == len(s):
                    result.append(".".join(path))
                return
            
            # ------------------------------------------------
            # Try segment lengths 1 to 3
            # ------------------------------------------------
            for length in range(1, 4):
                
                # If segment exceeds string length → stop
                if index + length > len(s):
                    break
                
                segment = s[index:index+length]
                
                # ------------------------------------------------
                # Rule 1: No leading zeros
                # "01" is invalid but "0" is valid
                # ------------------------------------------------
                if segment[0] == '0' and length > 1:
                    continue
                
                # ------------------------------------------------
                # Rule 2: Value must be <= 255
                # ------------------------------------------------
                if int(segment) > 255:
                    continue
                
                # Valid segment → recurse
                backtrack(index + length, path + [segment])
        
        backtrack(0, [])
        return result

"""
------------------------------------------------------------
Example Walkthrough:

Input:
    s = "25525511135"

Goal:
    Place 3 dots to form 4 valid IP segments.

Start:
    backtrack(0, [])

Try segments starting at index 0:

1️⃣ Take "2"
    path = ["2"]
    backtrack(1, ["2"])

    Continue trying:
        "5" → ["2","5"]
        "5" → ["2","5","5"]
        ...
    This path eventually fails because segments become invalid
    or we don't end exactly at string length with 4 parts.

2️⃣ Take "25"
    path = ["25"]
    backtrack(2, ["25"])
    This branch also eventually fails.

3️⃣ Take "255"
    path = ["255"]
    backtrack(3, ["255"])

    Now at index 3:

    Try next segment:

    1️⃣ "2"
    2️⃣ "25"
    3️⃣ "255"  ← valid

    path = ["255","255"]
    backtrack(6, ["255","255"])

    Now at index 6:

    Try:
        "1"
        "11"
        "111"

    Take "11":
        path = ["255","255","11"]
        backtrack(8, ["255","255","11"])

    Now at index 8:

    Try:
        "1"
        "13"
        "135" ← valid

    path = ["255","255","11","135"]

    Now:
        len(path) == 4
        index == len(s)

    So we add:
        "255.255.11.135"

Backtracking continues to explore other valid splits,
like:
    "255.255.111.35"

Final Output:
[
 "255.255.11.135",
 "255.255.111.35"
]
------------------------------------------------------------

Key Backtracking Idea:
- Try 1–3 digit segments
- Validate each segment
- Recurse deeper
- Stop when 4 segments formed
- Only accept if full string is consumed
------------------------------------------------------------
"""