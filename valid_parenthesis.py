class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []
        if len(s) < 2:
            return False
        for each in s:
            if each == '[' or each == '{' or each == '(':
                my_stack.append(each)
            else:
                if not my_stack:
                    return False
                cur_pair = my_stack.pop() + each
                if cur_pair != "()" and cur_pair != "{}" and cur_pair != "[]":
                    return False
        return len(my_stack) == 0