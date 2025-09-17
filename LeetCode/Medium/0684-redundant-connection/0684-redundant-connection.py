class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
#here first we will have parents sent to all nodes as themself and rank  will be equal to 1 for all the nodes as there wont be any children and according the array which is the edges of tree we will take one at a time and check for those two nodes do we have common root parents if we have means those two are connected by some path and part of the tree already so adding the current edge will lead to create cycle or extra path so we will return these edge(means nodes) if we came across this case if not means the two nodes are not connected and should be added to tree to do that we will check whose rank is heigher and rank is here like the number of childrens it contains because we need to add one node to another which has higher number of childrens or higher rank and when we add the rank of the parent node to which we added should be increased with the rank of the adding node and update the parent of that node like for ex edges = [[1,2],[1,3],[2,3]] so first rank = [1,1,1] parent = [1,2,3] so for first edge we will check if they have common parent as they dont have we will add one node as a child to another so rank = [2,1,1] and [1,1,2] so for node 1 the rank has been increased as now it has the child node2 and node2 s parent is node1 now next for edge [1,3]. it will be like rank [3,1,1] and. par = [1,1,1] as we add the node 3 also as a child to node 1 and for edge [2,3] ass for both node2 and node3 3 has common root parent we will return this pair
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)
        #To find the root parent of the node
        def find(n):       
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p
        # return False if cant complete
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:       #if they have common parent
                return False
            else:               #we will check for which node we can add the other node as a children 
                if rank[p1] > rank[p2]:
                    par[p2] = p1            #update the parent for child node
                    rank[p1] += rank[p2]     #update the rank of parent node
                else:
                    par[p1] = p2
                    rank[p2] += rank[p1]
            return True
        for n1, n2 in edges: 
            if not union(n1, n2): 
                return [n1, n2]