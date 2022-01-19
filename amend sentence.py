class Solution:

    def amendSentence(self, s):
        start, n = 0, len(s)
        res = ''
        for i in range(n-1):
            if (s[i].islower() and s[i+1].isupper()) or (s[i].isupper() and s[i+1].isupper()): 
                res = res + ' ' + s[start:i+1].lower()
                start = i+1
        res = res + ' ' + s[start:n].lower()
        return res.strip()
