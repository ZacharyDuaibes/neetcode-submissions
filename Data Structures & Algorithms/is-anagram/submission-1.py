class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # dict
        dict_s = {}
        # check if length is the same, if not = fail
        if len(s) != len(t): return False
        for i in s:
            if i in dict_s:
                dict_s[i] += 1
            else: dict_s[i] = 1
        for j in t:
            if j not in dict_s: return False
            dict_s[j] -= 1
            if dict_s[j] < 0: return False
        return True

            
