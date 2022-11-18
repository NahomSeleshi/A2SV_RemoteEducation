class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        queue = deque([each for each in students])
        cir_sandwich, sqr_sandwich = 0,0
        sandwich_index = 0
        for each in students:
            if each == 1:
                sqr_sandwich += 1
            else:
                cir_sandwich += 1
        while queue:
            n = len(queue)
            cur_student = queue.popleft()
            if (sandwiches[sandwich_index] == 1 and cir_sandwich == n) or (sandwiches[sandwich_index] == 0 and sqr_sandwich == n):
                break
            if cur_student == 1 and sandwiches[sandwich_index] == 1:
                sandwich_index += 1
                sqr_sandwich -= 1
            elif cur_student == 0 and sandwiches[sandwich_index] == 0:
                sandwich_index += 1
                cir_sandwich -= 1
            else:
                queue.append(cur_student)
                
        return cir_sandwich + sqr_sandwich