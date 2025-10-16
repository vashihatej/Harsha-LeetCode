class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # preMap = { i:[] for i in range(numCourses)}         #this is creating a empty hashmap 
        #                                                 #which includes all the courses like {1:[],2:[],etc}
        # for crs, pre in prerequisites:
        #     preMap[crs].append(pre)
        # # a course has 3 possible states:
        # # visited -> crs has been added to output
        # # visiting -› crs not added to output, but added to cycle
        # # unvisited -> crs not added to output or cycle
        # output = []
        # visit, cycle = set(), set()  #one to make sure that the course is visited and marked completed and other is to find the cycle if it is not completed yet
        # def dfs(crs) :
        #     if crs in cycle:
        #         return False 
        #     if crs in visit:
        #         return True

        #     cycle.add(crs)
        #     for pre in preMap[crs]:
        #         if dfs(pre) == False:
        #             return False
        #     cycle.remove(crs)
        #     visit.add(crs)
        #     output.append(crs)
        #     return True                   #mark the current course also completed or can be completed as because all its pre requsites are completed means it has []

        # for crs in range(numCourses):                       #if we have two or more unconnected graphs and to make sure to cover all we run in for loop like this
        #     if dfs(crs) == False:
        #         return []
        # return output   

        # Step 1: Build adjacency list
        def dfs(src, adj, visit, path, topSort):
            # If the current node is already in recursion stack → cycle
            if src in path:
                return False  # cycle detected
            # If already fully visited → skip
            if src in visit:
                return True
            # Add node to current path
            path.add(src)
            # Explore all neighbors
            for nei in adj[src]:
                if not dfs(nei, adj, visit, path, topSort):
                    return False  # cycle propagated upward

            # Done exploring → remove from current path
            path.remove(src)
            # Mark as permanently visited
            visit.add(src)
            # Add node to topSort after all dependencies processed
            topSort.append(src)

            return True  # no cycle found in this path
    
        adj = {i: [] for i in range(numCourses)}
        for src, dst in prerequisites:
            adj[src].append(dst)

        topSort = []
        visit = set()   # permanently visited nodes (no cycle through them)
        path = set()    # current recursion stack (to detect cycles)

        # Step 2: DFS on every node
        for i in range(numCourses):
            if i not in visit:
                if not dfs(i, adj, visit, path, topSort):
                    return []  # or "Cycle detected! No valid topological order exists."
        # Step 3: reverse postorder to get topological order

        return topSort


        # output = set()
        # for crs, pre in prerequisites:
        #     preMap[crs].append(pre)                     #Updating all the courses with the prerequesites as like adjacenty list
        
        # visitset =set()                            #used to find out the cycle and return False saying you can't take all the courses
        # def dfs(crs):                               #For each courses we will do DFS on each prerequisites and if all of them returns true which means they can be completed by seeing that if they have empty array []
        #     if crs in visitset:                #if we come to a course which is already visited which means it has some prerequesite dependency then we can't complete returning False
        #         return False
        #     if preMap[crs] == []:   
        #         if crs not in output:
        #             output.add(crs)  
        #             print("hi", crs)        #base case to represent the corse can be completed
        #         return True
        #     visitset.add(crs)
        #     for pre in preMap[crs]:
        #         if not dfs(pre) : return False            #if any of the pre requsites is not completed then we will return False
        #     visitset.remove(crs)                        #to make sure that it wont simply return False as its all pre requsites are cleared that they can be completed  now we can remove this from set and next mark the crs as completed by assining [] value
        #     preMap[crs] = []
        #     print(crs)
        #     output.add(crs)

        #     return True

        # for crs in range(numCourses):               #if we have two or more unconnected graphs and to make sure to cover all we run in for loop like this
        #     if not dfs(crs) : return []
        # return list(output)


        