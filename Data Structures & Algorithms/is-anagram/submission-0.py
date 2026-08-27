class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = sorted(s)
        ts = sorted(t)
        print(ts,ss)
        if ss == ts:
            return True
        else:
            return False
        