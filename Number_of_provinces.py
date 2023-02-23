class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        neighbors = defaultdict(list)
        visited = set()
        for nodes in range(len(isConnected)):
            for index, value in enumerate(isConnected[nodes]):
                if value == 1 and index != nodes:
                    neighbors[nodes].append(index)
        number_of_provinces = len(isConnected)
        for each_node in neighbors:
            connected_nodes = self.dfs(each_node, neighbors, visited, 0)-1
            number_of_provinces -= (connected_nodes if connected_nodes > 0 else 0)
        
        return number_of_provinces

    def dfs(self, node, neighbors, visited, count):
        if node in visited:
            return 0
        visited.add(node)
        count += 1
        for each_neighbor in neighbors[node]:
            count += self.dfs(each_neighbor, neighbors, visited, 0)
        
        return count
        