class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        c = defaultdict(list)
        for s in strs:
            w = ''.join(sorted(s))
            c[w].append(s)
        return list(c.values())