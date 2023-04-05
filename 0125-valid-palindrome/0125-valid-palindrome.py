
#edge case: if string is empty or length is 1, return true
#intuition: remove spaces, non-alphanumeric characters, convert to lowercase -> check if the letter is same in both sides
#
#1. remove non-alphanumeric characters, space
#2. convert to lowercase
#3. check from each side(start & end pointer)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s)-1
        s1,s2="",""
        s = s.lower()
        if len(s)==0: return True
        if len(s)==1: return True
        while start<len(s)-1 and end > 0:
            if s[start].isalpha() == False and s[start].isnumeric()==False:
                start +=1
            if s[end].isalpha() == False and s[end].isnumeric() == False:
                end -=1

            if (s[start].isalpha()==True or s[start].isnumeric()==True) and (s[end].isalpha()==True or s[end].isnumeric()==True):
                s1 += s[start]
                s2+= s[end]
                if s[start]==s[end]:
                    start +=1
                    end -=1
                else: 
                    return False
        print(s1,s2)
        if s1==s2:
            return True
        else:
            return False
        
               