class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        dicts={}
        dictt={}

        for i in range(len(s)):
            if s[i] in dicts:
              dicts[s[i]]=dicts[s[i]]+1
            else:
                dicts[s[i]]=1
            
            if t[i] in dictt:
                dictt[t[i]]=dictt[t[i]]+1
            else:
                dictt[t[i]]=1

        return dicts==dictt