class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for i in range(numCourses)]
        in_d = [0] * numCourses
        total = 0

        for a, b in prerequisites:
            graph[b].append(a)
            in_d[a] += 1
        queue = deque([])
        for cour in range(numCourses):
            if in_d[cour] == 0:
                queue.append(cour)
        while queue:
            cur = queue.popleft()
            for i in graph[cur]:
                in_d[i] -= 1
                if in_d[i] == 0:
                    queue.append(i)
            total += 1
        return total == numCourses
                
            