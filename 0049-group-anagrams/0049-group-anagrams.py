# [Initial Trial] 
#intuition: put each element in the dictionary and check if there's anagram(brute force)
#     
# 1. put each letter in the dictionary, put the count of each letter in the value
# 2. for other words, check if 1) length is same, 2) each letter exists in the dictionary (subtract 1 in each letter)
# 3. check if all value is 0
# 4. if so, put word into tmp array
#    if not, go to the next element and check
# 5. put tmp into ans
# edge case: if len(strs)==1 : append str to answer array

# build a function to check whether two strings are anagrams or not


# from string import ascii_lowercase
# def checkanagrams(s1:str, s2:str) -> bool:
#     dic ={}
#     if len(s1)==0 and len(s2)==0:
#         return True
#     for alphabet in ascii_lowercase:
# 	    dic[alphabet] = 0
#     if len(s1) == len(s2):
#         for c in s1:
#             dic[c] += 1
#         for c in s2:
#             dic[c] -= 1
#         for value in dic.values():
#             if value != 0 : return False
#         return True
#     else:
#         return False
# 
# 
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         chkdic = {}
#         ans =[]
#         if len(strs)==1: 
#             ans.append(strs)
#             return ans
#         for s in strs:
#             chkdic[s] = False
#         for i in range(0, len(strs)):
#             tmp =[]
#             if not chkdic[strs[i]] :
#                 tmp.append(strs[i])
#                 chkdic[strs[i]]=True
#                 for j in range(i+1, len(strs)):
#                     if not chkdic[strs[j]]:
#                         if checkanagrams(strs[i],strs[j]):
#                             tmp.append(strs[j])
#                             chkdic[strs[j]]=True
#                 ans.append(tmp)
#             
#         return ans


# [Solution]
# intuition
#     1. make a dictionary with key(anagram word),value(list of all the strings that are anagrams)
#     2. for each string, sort them and compare them to the key of dictionary
#         if same, put the string into the value of dictionary
        
class Solution:
     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            lookup = defaultdict(list)
            for s in strs:
                key = "".join(sorted(list(s)))
                lookup[key].append(s)
                
            ans =[]
            for l in lookup.values():
                ans.append(l)
            return ans


