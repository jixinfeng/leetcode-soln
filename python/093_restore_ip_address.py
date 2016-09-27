"""
Given a string containing only digits, restore it by returning all possible
valid IP address combinations.

For example:
    Given "25525511135",

    return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
"""
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if s is None:
            return []
        if len(s) < 4:
            return []
        self.soln = []
        self.ipBlockSearch(s, 0, '')
        return self.soln
    
    def ipBlockSearch(self, s, block, ip):
        if block > 3 or len(s) > 3 * (4 - block) or s == '':
            return
        elif block == 3:
            if len(s) > 1 and s[0] == '0':
                return
            elif int(s) > 255:
                return
            else:
                self.soln.append(ip + s)
        else:
            for i in range(min(len(s), 3)):
                if i == 2 and int(s[:i + 1]) > 255:
                    return
                elif i > 0 and s[0] == '0':
                    return 
                else:
                    self.ipBlockSearch(s[i + 1:], block + 1, ip + s[:i + 1] + '.')

a = Solution()
print(a.restoreIpAddresses('0000'))
print(a.restoreIpAddresses('010010'))
print(a.restoreIpAddresses('123456789'))
print(a.restoreIpAddresses('25525511135'))

"""
Non-recursive 3 layer forloop with pruning
    def restoreIpAddresses(self, s):
        if s is None:
            return []
        if len(s) < 4:
            return []
        length = len(s)        
        soln = []
        for i in range(1, length - 2):
            a1 = s[:i]
            if int(a1) > 255:
                continue
            elif a1 != '0' and a1[0] == '0':
                continue
            for j in range(i + 1, length - 1):
                a2 = s[i:j]
                if int(a2) > 255:
                    continue
                elif a2 != '0' and a2[0] == '0':
                    continue
                for k in range(j + 1, length):
                    a3, a4 = s[j:k], s[k:]
                    if int(a3) > 255 or int(a4) > 255:
                        continue
                    elif a3 != '0' and a3[0] == '0':
                        continue
                    elif a4 != '0' and a4[0] == '0':
                        continue
                    soln.append(s[:i]+'.'+s[i:j]+'.'+s[j:k]+'.'+s[k:])
        return soln
"""
