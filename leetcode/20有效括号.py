
class Solution(object):

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def is_match(string1, string2):
            if string1 == '(' and string2 == ')':
                return True
            elif string1 == '{' and string2 == '}':
                return True
            elif string1 == '[' and string2 == ']':
                return True
            else :
                return False

        def palindrome():
            middle_length = int(len(s) / 2)
            split1 = s[0:middle_length]
            split2 = s[middle_length:length][::-1]
            for index, string in enumerate(split1):
                if is_match(string, split2[index]):
                    continue
                else:
                    return False
            return True

        length = len(s)
        if length % 2 != 0:
            return False
        if length == 2:
            return is_match(s[0], s[1])
        s1, s2 = [], []
        for index, string in enumerate(s):
            s1.append(string) if index % 2 == 0 else s2.append(string)
        for index, string in enumerate(s1):
            if is_match(string, s2[index]):
                continue
            else:
                return palindrome()
        return True



s = Solution()
print(s.isValid("([)]"))
