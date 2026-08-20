class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid_str = "".join(re.findall(r"[a-zA-Z0-9]+" , s.lower()))
        
        
        left = 0
        right = len(valid_str) - 1

        

        while left < right:
            if valid_str[left] != valid_str[right]:
                return False
            left += 1
            right -= 1

        return True