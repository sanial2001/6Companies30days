class Solution:
    def __init__(self):
        self.phone = ['_', '0', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    
    def solve(self, digits):
        if len(digits) == 0:
            return ['']
        ans = []
        ch = int(digits[0])
        rem = self.solve(digits[1:])
        match = self.phone[ch]
        for i in range(len(match)):
            for j in range(len(rem)):
                ans.append(match[i] + rem[j])
        return ans
    
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        return self.solve(digits)
