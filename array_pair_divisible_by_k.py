class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        d = dict()
        for i in range(len(arr)):
            d[arr[i]%k] = d.get(arr[i]%k, 0) + 1
        #print(d.items())
        
        for val in d:
            if val == 0 or (k%2 == 0 and val == k//2):
                if d[val]%2 != 0:
                    return False
            else:
                if k-val in d:
                    if d[val] != d[k-val]:
                        return False
                else:
                    return False
        return True
