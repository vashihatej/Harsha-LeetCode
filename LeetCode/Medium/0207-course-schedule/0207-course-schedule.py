class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # preMap = { i : [] for i in range(numCourses)}         #this is creating a empty hashmap 
        #                                                 #which includes all the courses like {1:[],2:[],etc}

        # for crs, pre in prerequisites:
        #     preMap[crs].append(pre)                     #Updating all the courses with the prerequesites as like adjacenty list
        
        # visitset =set()                            #used to find out the cycle and return False saying you can't take all the courses
        # def dfs(crs):                               #For each courses we will do DFS on each prerequisites and if all of them returns true which means they can be completed by seeing that if they have empty array []
        #     if crs in visitset:                #if we come to a course which is already visited which means it has some prerequesite dependency then we can't complete returning False
        #         return False
        #     if preMap[crs] == []:             #base case to represent the corse can be completed
        #         return True
            
        #     visitset.add(crs)
        #     for pre in preMap[crs]:
        #         if dfs(pre) == False:
        #              return False            #if any of the pre requsites is not completed then we will return False
        #     visitset.remove(crs)                        #to make sure that it wont simply return False as its all pre requsites are cleared that they can be completed  now we can remove this from set and next mark the crs as completed by assining [] value
        #     preMap[crs] = []

        #     return True

        # for crs in range(numCourses):               #if we have two or more unconnected graphs and to make sure to cover all we run in for loop like this
        #     if dfs(crs) == False:
        #         return False
        # return True

        premap = {}

        for i in range(numCourses):
            premap[i]=[]
        for cor, pre in prerequisites:
            premap[cor].append(pre)
        
        visited=set()

        def dfs(crs, premap):
            if crs in visited:
                return False
            if premap[crs] == []:
                return True
            visited.add(crs)
            for i in premap[crs]:
                if dfs(i, premap)==False:
                    return False
            visited.remove(crs)
            premap[crs] = []
            return True


        for crs in range(numCourses):
            if dfs(crs, premap)==False:
                return False
        return True

