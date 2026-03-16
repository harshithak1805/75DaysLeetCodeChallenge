from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group=defaultdict(list)
        for i in range(len(strs)):
            x="".join(sorted(strs[i]))
            group[x].append(strs[i])
        return list(group.values())
