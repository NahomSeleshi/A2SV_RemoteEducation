class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjacency_list = defaultdict(list)
        indegree = [0 for i in range(numCourses)]
        for course, prerequisite in prerequisites:
            adjacency_list[prerequisite].append(course)
            indegree[course] += 1
        
        toposort = []
        visited_courses = set()
        queue = deque([index for index, each in enumerate(indegree) if each == 0])
        while queue:
            cur_course = queue.popleft()
            toposort.append(cur_course)
            visited_courses.add(cur_course)
            for each_connection in adjacency_list[cur_course]:
                if each_connection in visited_courses:
                    return []
                indegree[each_connection] -= 1
                if indegree[each_connection] == 0:
                    queue.append(each_connection)
        
        if len(toposort) == numCourses:
            return toposort
        return []