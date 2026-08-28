class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = defaultdict(list)
        for s in strs:
            ss = ''.join(sorted(s))
            if ss in out:
                out[ss].append(s)
            else:
                out[ss] = [s]
            
        last = []
        for k, d in out.items():
            last.append(d)
        return last