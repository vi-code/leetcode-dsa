class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {course: [] for course in range(numCourses)}

        for a, b in prerequisites:
            graph[b].append(a)
        
        NOTSEEN = 0
        VISITING = 1
        VISITED = 2
        state = [NOTSEEN] * numCourses
        def dfs(course) -> bool:
            if state[course] == VISITING:
                return False
            if state[course] == VISITED:
                return True

            state[course] = VISITING
            for n in graph[course]:
                if not dfs(n):
                    return False
            state[course] = VISITED
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
        