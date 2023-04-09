class Solution:
    def return_indices(self, k:int, conditions:List[List[int]])->dict:
        incoming_edges = [0 for _ in range(k)]
        graph = [[] for _ in range(k)]

        for node1, node2 in conditions:
            graph[node1-1].append(node2-1)
            incoming_edges[node2-1] += 1

        queue = deque([])
        for i in range(k):
            if incoming_edges[i] == 0:
                queue.append(i)
        res = {}
        sorting_index = 0
        while queue:
            cur_node = queue.popleft()
            res[cur_node] = sorting_index
            sorting_index += 1

            for neighbor in graph[cur_node]:
                incoming_edges[neighbor] -= 1
                if incoming_edges[neighbor] == 0:
                    queue.append(neighbor)

        return res

    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        rows = self.return_indices(k, rowConditions)
        cols = self.return_indices(k, colConditions)

        if len(rows) == k and len(cols) == k:
            matrix = [[0 for _ in range(k)] for j in range(k)]
            for i in range(k):
                matrix[rows[i]][cols[i]] = i+1

            return matrix
        return []
