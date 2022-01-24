# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def peak(self, mountain_arr, n):
        start, end = 0, n-1
        while start <= end:
            mid = (start + end)//2
            k_mid = mountain_arr.get(mid)
            k_mid1 = mountain_arr.get(mid-1) if mid-1 >= 0 else 0
            k_mid2 = mountain_arr.get(mid+1) if mid+1 < n else n-1
            #print(mid)
            if k_mid > k_mid1 and k_mid > k_mid2:
                return mid
            elif k_mid <= k_mid2:
                start = mid+1
            elif k_mid1 > k_mid:
                end = mid-1
    
    def search(self, mountain_arr, start, end, k):
        while start <= end:
            mid = (start + end)//2
            key = mountain_arr.get(mid)
            if key == k:
                return mid
            elif k > key:
                start = mid+1
            elif k < key:
                end = mid-1
        return -1
    
    def dec_search(self, mountain_arr, start, end, k):
        while start <= end:
            mid = (start+end)//2
            key = mountain_arr.get(mid)
            if key == k:
                return mid
            elif k > key:
                end = mid-1
            elif k < key:
                start = mid+1
        return -1
    
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        index = self.peak(mountain_arr, n)
        #print(index)
        res = self.search(mountain_arr, 0, index, target)
        return res if res != -1 else self.dec_search(mountain_arr, index+1, n-1, target)
