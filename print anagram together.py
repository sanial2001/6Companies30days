class Solution:
    def groupAnagrams(self, strs):
        d = dict()
        for val in strs:
            key = tuple(sorted(val))
            d[key] = d.get(key, []) + [val]

        return d.values()


if __name__ == '__main__':
    print(Solution().groupAnagrams(strs=['']))
