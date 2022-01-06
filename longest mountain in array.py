class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 3:
            return 0
        if arr == sorted(arr) or arr[::-1] == sorted(arr):
            return 0
        res, start, end = 0, 0, 0
        for i in range(1, n-1):
            start, end = i, i
            if arr[i-1] < arr[i] and arr[i+1] < arr[i]:
                while start > 0 and arr[start-1] < arr[start]:
                    start = start-1
                while end < n-1 and arr[end+1] < arr[end]:
                    end = end+1
                res = max(res, end-start+1)
        return 0 if res < 3 else res
