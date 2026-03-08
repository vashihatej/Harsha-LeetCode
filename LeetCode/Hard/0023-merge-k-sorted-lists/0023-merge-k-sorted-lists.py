# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        while len(lists) > 1:
            listnodes = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                #merging two two lists at time until we have only one list 
                listnodes.append(self.mergeLists(l1, l2))
            lists = listnodes
        return lists[0]

    def mergeLists(self, list1, list2):
        temp = ListNode()
        tail = temp
        while list1 and list2:
            if list1.val<list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next=list2
                list2=list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        else:
            tail.next = list2
        return temp.next


# import heapq

# def mergeKLists_heap(lists):
#     # Dummy node acts as a "fake head" so we don't have to
#     # handle the first node as a special case.
#     # At the end, dummy.next points to the real merged list.
#     dummy = ListNode(0)
#     current = dummy  # 'current' is the tail of our result list; we keep appending to it

#     # Our min-heap will store tuples of (node_value, tiebreaker, node).
#     #
#     # Why tuples? Python's heapq sorts by the first element (node_value),
#     # which is exactly what we want — always pop the smallest value.
#     #
#     # Why a tiebreaker? If two nodes have the SAME value, Python tries to
#     # compare the second element. If we stored the node directly there,
#     # Python would crash because ListNode doesn't support '<'.
#     # A unique integer as tiebreaker guarantees no two tuples are "equal"
#     # before reaching the node, so Python never tries to compare nodes.
#     heap = []

#     # STEP 1: Push the FIRST node (head) of each list into the heap.
#     #
#     # After this loop, the heap contains at most K items — one from each list.
#     # This is the "look at the top card of every pile" step.
#     for i, head in enumerate(lists):
#         if head:  # skip empty lists
#             heapq.heappush(heap, (head.val, i, head))
#             # Using 'i' (0, 1, 2, ...) as the initial tiebreaker since
#             # each list index is unique at this point.

#     # 'idx' is our tiebreaker counter going forward.
#     # We start from len(lists) so it doesn't collide with the 0..K-1
#     # values we already used above.
#     idx = len(lists)

#     # STEP 2: Repeatedly pop the smallest node and push its successor.
#     #
#     # This is the core loop:
#     #   - Pop gives us the globally smallest node among all K "fronts"
#     #   - We attach it to our result list
#     #   - If that node has a next, we push it so the heap stays updated
#     #
#     # The heap always holds at most K nodes (one per list), so each
#     # push/pop is O(log K). We do this N times total → O(N log K).
#     while heap:
#         val, _, node = heapq.heappop(heap)  # get the node with smallest value

#         # Attach this node to the end of our merged result list
#         current.next = node
#         current = current.next  # move the tail pointer forward

#         # If the list this node came from still has more nodes,
#         # push the next node into the heap.
#         # This replaces the node we just removed — keeping one
#         # representative from each active list in the heap.
#         if node.next:
#             idx += 1  # fresh unique tiebreaker so no collisions ever happen
#             heapq.heappush(heap, (node.next.val, idx, node.next))

#     # dummy was our fake head. dummy.next is where the real list starts.
#     return dummy.next