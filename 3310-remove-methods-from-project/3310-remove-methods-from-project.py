class Solution:
    def dfs(self, node, methods, vis):
        vis[node]=1
        for el in methods.get(node, []):
            if not vis[el]:
                self.dfs(el, methods, vis)
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        methods, vis, rem = {},[0]*n,[]
        for i in range(len(invocations)):
            methods[invocations[i][0]]=methods.get(invocations[i][0], [])
            methods[invocations[i][0]].append(invocations[i][1])
        # print(methodKeys)
        self.dfs(k, methods, vis)
        for u, v in invocations:
            if not vis[u] and vis[v]:
                return list(range(n))
        for i in range(n):
            if not vis[i]:
                rem.append(i)
        return rem
        