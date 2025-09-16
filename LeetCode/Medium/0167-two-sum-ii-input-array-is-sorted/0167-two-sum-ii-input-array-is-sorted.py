class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        freq ={}
        for i in range(0, len(numbers)):
            a = numbers[i]
            diff = target - a
            if diff in freq:
                return [freq[diff]+1, i+1]
            freq[a] = i
        # start=0
        # end=len(numbers)-1
        # while start<end:
        #     cursum=numbers[start]+numbers[end]
        #     if cursum<target:
        #         start+=1
        #     elif cursum>target:
        #         end-=1
        #     else:
        #         return[start+1, end+1]
                
            


        