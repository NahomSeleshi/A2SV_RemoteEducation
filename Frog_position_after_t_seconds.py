class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:

        adjacency_list = defaultdict(list)
        visited_nodes = set()
        for node1, node2 in edges:
            adjacency_list[node1].append(node2)
            adjacency_list[node2].append(node1)
            
        queue = deque([[1, 1, 0]])
        while queue:
            for i in range(len(queue)):
                cur_node, cur_prob, cur_time = queue.popleft()
                visited_nodes.add(cur_node)
                if cur_node == target and cur_time == t:
                    return cur_prob
                next_level_elements = len(adjacency_list[cur_node])
                for each_node in adjacency_list[cur_node]:
                    if each_node in visited_nodes:
                        next_level_elements -= 1
                    elif cur_time + 1 <= t:
                        queue.append([each_node, cur_prob/next_level_elements, cur_time+1])
                if not next_level_elements and cur_time + 1 <= t:
                    queue.append([cur_node, cur_prob, cur_time + 1])
        return 0
                