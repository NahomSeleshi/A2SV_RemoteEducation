class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        self.safe_nodes = []
        visited_nodes = [0 for i in range(len(graph))]
        for node in range(len(graph)):
            self.check_safe_node(node, visited_nodes, graph)
        return sorted(self.safe_nodes)


    def check_safe_node(self, cur_node, visited_nodes, graph):
        if visited_nodes[cur_node] == 1:
            return True
        if visited_nodes[cur_node] == -1:
            return False
        is_safe = True
        visited_nodes[cur_node] = -1
        for each_node in graph[cur_node]:
            is_safe = is_safe and self.check_safe_node(each_node, visited_nodes, graph)
        if is_safe:
            self.safe_nodes.append(cur_node)
            visited_nodes[cur_node] = 1
        return is_safe
        