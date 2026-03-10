import bisect
class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id=0
        self.history=[[(0,0)] for i in range(length)]

    def set(self, index: int, val: int) -> None:
        self.history[index].append((self.snap_id, val))

    def snap(self) -> int:
        self.snap_id+=1
        return self.snap_id-1

    def get(self, index: int, snap_id: int) -> int:
        arr= self.history[index]
        #Finding Right Bisect
        l=0
        r=len(arr)-1
        right=0
        while l<=r:
            mid=(l+r)//2
            if arr[mid][0] <= snap_id:
                l=mid+1
                right=mid
            else:
                r=mid-1
        return arr[right][1]



import bisect

class SnapshotArray:

    def __init__(self, length: int):
        """
        We maintain a change-history for every index.

        Instead of storing the entire array for every snapshot (which would be
        O(n * number_of_snaps) memory), we only store the moments when a value
        actually changes.

        For each index we store:
            [(snap_id, value), (snap_id, value), ...]

        Example for index 0:
            [(0,0), (0,5), (2,7)]

        Meaning:
            snapshot 0 -> value 5
            snapshot 1 -> value 5
            snapshot 2 -> value 7

        The first entry (0,0) represents the initial state of the array.
        """
        self.data = [[(0, 0)] for _ in range(length)]
        self.snap_id = 0


    def set(self, index: int, val: int) -> None:
        """
        Record the change at this index for the current snapshot id.

        Instead of updating a real array, we append the change into the
        history list for that index.

        Why this works:
        Snapshots only represent points in time. Values between snapshots
        do not change unless 'set' is called.

        Therefore storing only the change points is enough to reconstruct
        the value for any snapshot.
        """
        self.data[index].append((self.snap_id, val))


    def snap(self) -> int:
        """
        Taking a snapshot simply means advancing the global snapshot counter.

        We DO NOT copy the array here. That would be expensive.

        Instead, the snapshot id acts as a timestamp. Any 'set' operations
        performed before this will belong to this snapshot.

        Example:
            set(0,5)
            snap() -> snapshot 0

        Now future changes will belong to snapshot 1.
        """
        self.snap_id += 1
        return self.snap_id - 1


    def get(self, index: int, snap_id: int) -> int:
        """
        We need to return the value at 'index' when snapshot 'snap_id' was taken.

        The history list for that index looks like:
            [(snap_id, value), (snap_id, value), ...]

        The key observation:
        We want the MOST RECENT value whose snap_id <= requested snap_id.

        Example history:
            [(0,0), (0,5), (2,7)]

        Query:
            get(index, 1)

        Valid entries:
            (0,0)
            (0,5)

        The latest one is (0,5), so answer = 5.

        To find this efficiently we use binary search.

        bisect_right finds the insertion point for (snap_id, +∞),
        meaning it finds the first element with snap_id greater than the
        requested one. The previous element is the correct answer.
        """

        arr = self.data[index]

        # Find insertion position for (snap_id, infinity)
        # This ensures we move past all entries with snap_id <= requested
        i = bisect.bisect_right(arr, (snap_id, float('inf'))) - 1

        # The value stored at that position is the value of the array
        # at the requested snapshot
        return arr[i][1]