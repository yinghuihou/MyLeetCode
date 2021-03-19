# Definition for singly-linked list.

def main():
    a = "abcbaf"
    print(longestPalindrome(a))





# 笨方法解法
# def longestPalindrome(s):
#     if s == None:
#         return None
#     if s.strip() == "":
#         return s
#     length = 1
#     result = s[0]
#     for i in range(len(s)):
#         a = s.find(s[0])
#         b = s.rfind(s[0])
#         if a == b:
#             s = s[1:len(s)]
#             continue
#         else:
#             str1 = s[a: b + 1]
#             while a < b:
#                 if length >= len(str1):
#                     break
#
#                 if isHuiWen(str1):
#                     length = len(str1)
#                     result = str1
#
#                     break
#                 else:
#                     str1 = str1[0:len(str1) - 1]
#                     a = str1.find(str1[0])
#                     b = str1.rfind(str1[0])
#                     str1 = str1[a: b + 1]
#
#         s = s[1:len(s)]
#     return result
#
#
# def isHuiWen(string):
#     s1 = string
#     if s1 == ''.join(reversed(s1)):
#         return True
#     else:
#         return False

if __name__ == '__main__':
    main()
