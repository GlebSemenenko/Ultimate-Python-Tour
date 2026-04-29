import string
class Solution:
    def isPalindrome(self, s: str) -> bool:

        if len(s) == 1 or len(s) == 0: return True

        s = s.upper()
        s = s.replace(" ", "")
        s = s.replace("!", "")
        s = s.replace(".", "")
        s = s.replace(",", "")
        s = s.replace(":", "")
        f = 0
        l = len(s) -1

        while f < l:
            if s[f] != s[l]:
                return False
            else:
                f += 1
                l -= 1
        return True

if __name__ == "__main__":
    sol = Solution()
    test1 = "A man, a plan, a canal: Panama"
    test2 = "aaaaaa"
    print(sol.isPalindrome(test1))
    print(sol.isPalindrome(test2))




