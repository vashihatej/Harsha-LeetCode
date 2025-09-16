class Solution:
    def trap(self, height: List[int]) -> int:
        maxleft=[]
        maxright=[]
        maxlval=0
        maxrval=0
        res=0

        for i in range(0, len(height)): #construct a left max like [0,1,1,2,2,2,2,3,3,3,3,3]
            maxlval=max(maxlval, height[i])
            maxleft.append(maxlval)

        for j in range(len(height)-1, -1, -1): #construct a right max like [3,3,3,3,3,3,3,3,2,2,2,1]
            maxrval=max(maxrval, height[j])
            maxright.append(maxrval)

        maxright = maxright[::-1]      #To reverse the array as we did it calculation reversly

        for i in range(0, len(height)-1):
            if min(maxleft[i], maxright[i]) - height[i] >=0:    #here it will be like min(0,3)-0 = 0 water can be stored at 0th position
                res += min(maxleft[i], maxright[i]) - height[i]

        return res
