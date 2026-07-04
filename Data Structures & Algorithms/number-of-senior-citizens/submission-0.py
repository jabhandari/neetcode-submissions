class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res=0
        for i in details:
            ten=ord(i[11])-ord("0")
            one=ord(i[12])-ord("0")
            age=one+ten*10
            if age>60:
                res+=1
        return res