class Solution:
    def oddEvenList(self, head):
        """
        We rearrange nodes by POSITION (not value).

        Idea:
        Maintain two separate chains:
            - Odd index nodes
            - Even index nodes

        Then connect odd chain to even chain at the end.
        """

        if not head or not head.next:
            return head

        # odd starts at first node
        odd = head

        # even starts at second node
        even = head.next

        # Save head of even list (important!)
        evenHead = even

        # Traverse until even or even.next becomes None
        while even and even.next:

            # Link current odd to next odd
            odd.next = even.next
            odd = odd.next

            # Link current even to next even
            even.next = odd.next
            even = even.next

        # Attach even list after odd list
        odd.next = evenHead

        return head
"""
        PROBLEM:
        Group all nodes at odd indices together,
        followed by nodes at even indices.
        
        IMPORTANT:
        - Indexing is based on POSITION (1-based index)
        - NOT based on node value
        - Must preserve relative order
        - O(n) time and O(1) space

        -------------------------------------------------------
        EXAMPLE WALKTHROUGH
        -------------------------------------------------------

        Input:
            1 → 2 → 3 → 4 → 5

        Positions:
            1   2   3   4   5
            O   E   O   E   O

        Goal:
            Odd index nodes first → 1 → 3 → 5
            Even index nodes next → 2 → 4

        Final:
            1 → 3 → 5 → 2 → 4

        -------------------------------------------------------
        STEP-BY-STEP POINTER MOVEMENT
        -------------------------------------------------------

        Initial:
            odd = 1
            even = 2
            evenHead = 2 (we save this to attach later)

            1 → 2 → 3 → 4 → 5

        -------------------------------
        Iteration 1:
        -------------------------------

        odd.next = even.next
                 = 3
        odd = 3

        even.next = odd.next
                  = 4
        even = 4

        Structure now:

            Odd chain: 1 → 3
            Even chain: 2 → 4
            Remaining: 5

        -------------------------------
        Iteration 2:
        -------------------------------

        odd.next = even.next
                 = 5
        odd = 5

        even.next = odd.next
                  = None
        even = None

        Structure now:

            Odd chain: 1 → 3 → 5
            Even chain: 2 → 4

        -------------------------------
        Final Step:
        -------------------------------

        Attach even list after odd list:

            odd.next = evenHead

        Final List:
            1 → 3 → 5 → 2 → 4

        -------------------------------------------------------
        WHY THIS WORKS
        -------------------------------------------------------

        We are NOT creating new nodes.
        We are just rewiring existing next pointers.

        Odd pointer always jumps over even node.
        Even pointer always jumps over odd node.

        So two separate chains naturally form.
        """