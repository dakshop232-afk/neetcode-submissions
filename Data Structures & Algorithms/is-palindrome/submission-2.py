class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans=""
        s1=s.lower()
        for ch in s1:
            if (ch>="a" and ch<="z") or (ch>="0" and ch<="9"):
                ans=ans+ch
        
        if ans==ans[::-1]:
            return True
        else:
            return False
