class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        ans={"}":"{","]":"[",")":"("}
        for i in s:
            if i in ans:
                if stack and stack[-1]==ans[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False

            
        
