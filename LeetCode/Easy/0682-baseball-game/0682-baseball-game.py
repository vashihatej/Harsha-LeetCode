class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        stack = []
        
        for op in operations:
            
            if op == "+":
                # Sum of last two scores
                stack.append(stack[-1] + stack[-2])
            
            elif op == "D":
                # Double last score
                stack.append(2 * stack[-1])
            
            elif op == "C":
                # Remove last score
                stack.pop()
            
            else:
                # Add new score
                stack.append(int(op))
        
        return sum(stack)