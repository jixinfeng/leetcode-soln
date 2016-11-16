"""
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

Corner Cases:

Did you consider the case where path = "/../"?

In this case, you should return "/".

Another corner case is the path might contain multiple slashes '/' together,
such as "/home//foo/".

In this case, you should ignore redundant slashes and return "/home/foo".
"""
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        soln = []
        for folder in path.split('/'):
            if folder == '.' or folder == '':
                continue
            elif folder == '..':
                if len(soln) > 0:
                    soln.pop()
            else:
                soln.append(folder)
        return '/' + '/'.join(soln)

a = Solution()
print(a.simplifyPath("/home/") == "/home")
print(a.simplifyPath("/a/./b/../../c/") == "/c")
print(a.simplifyPath("/../") == "/")
print(a.simplifyPath("/home//foo/") == "/home/foo")
