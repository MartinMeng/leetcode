class Solution(object):
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        """
        :type n: int
        :type leftChild: List[int]
        :type rightChild: List[int]
        :rtype: bool
        """
        # find root, assert no cycles
        indegree = [0] * n
        root = -1
        for i in range(0, n):
            l = leftChild[i]; r = rightChild[i]
            if l != -1:
                indegree[l] += 1
                if indegree[l] > 1: return False
            if r != -1:
                indegree[r] += 1
                if indegree[r] > 1: return False
        for i in range(0, n):
            if (indegree[i] == 0 and root != -1): return False # multiple roots for tree
            if (indegree[i] == 0): root = i

        # assert root covers whole tree
        visited = [False]*n
        def dfs(i):
            if i == -1: return;
            visited[i] = True
            l = leftChild[i]; r = rightChild[i]
            dfs(l); dfs(r)

        dfs(root)
        return False not in visited

"""
This is a good binary tree problem. really tests one's ability recognize tree only allowed to have 1 root which has in-degree of 0 and every other node has to have in-degree of 1.

every other node must have in-degree of 1.
"""
