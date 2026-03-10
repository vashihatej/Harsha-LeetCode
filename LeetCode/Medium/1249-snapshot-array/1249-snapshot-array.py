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



# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)