class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        given_string = list(s)
        stack = []

        for index, char in enumerate(given_string):
            if char != ")":
                stack.append([index, char])
            else:
                while stack and stack[-1][1] != "(":
                    stack.pop()
                if stack and stack[-1][1] == "(":
                    stack.pop()
                else:
                    given_string[index] = ""

        while stack:
            cur_popped = stack.pop()
            if cur_popped[1] == "(":
                given_string[cur_popped[0]] = ""
        
        return "".join(given_string)


