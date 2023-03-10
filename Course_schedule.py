class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjacency_list = defaultdict(list)
        indegree = [0 for i in range(numCourses)]
        for course, prerequisite in prerequisites:
            adjacency_list[prerequisite].append(course)
            indegree[course] += 1
        
        toposort = set()
        queue = deque([index for index, each in enumerate(indegree) if each == 0])
        while queue:
            cur_course = queue.popleft()
            toposort.add(cur_course)
            for each_connection in adjacency_list[cur_course]:
                if each_connection in toposort:
                    return False
                indegree[each_connection] -= 1
                if indegree[each_connection] == 0:
                    queue.append(each_connection)
        
        if len(toposort) == numCourses:
            return True
        return False

