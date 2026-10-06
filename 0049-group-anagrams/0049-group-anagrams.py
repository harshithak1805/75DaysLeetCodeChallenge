class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ss=[]
        seen=defaultdict(list)
        for i in strs:
            ss.append("".join(sorted(i)))
        for j in range(len(strs)):
            seen[ss[j]].append(strs[j])
        return list(seen.values())