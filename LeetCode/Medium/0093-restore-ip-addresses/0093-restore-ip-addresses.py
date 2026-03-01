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
            # If we already have 4 parts
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