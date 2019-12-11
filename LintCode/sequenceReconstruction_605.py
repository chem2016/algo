class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def __init__(self):
        pass
    def sequenceReconstruction(self, org, seqs):
        # write your code here
        graph = self.build_graph(seqs)
        topo_order = self.topo_sorting(graph)
        
        return topo_order == org
        
    def build_graph(self, seqs):
        # build a graph base on the seqs logic
        # {1: (0), 2: (1), 3: (1)}
        graph = {}
        for seq in seqs:
            for num in seq:
                if not num in graph:
                    graph[num] = set()
        
        for seq in seqs:
            for i in range(1, len(seq)):
                graph[seq[i-1]].add(seq[i]) 
        
        return graph
        
    def topo_sorting(self, graph):
        # get indegree from graph
        indegree = self.get_indegree(graph)
        queue = []
        for key, value in indegree.items():
            if value == 0:
                queue.append(key)
        topo_order = []
        while len(queue):
            if len(queue) > 1:
                return None
            node = queue.pop()
            topo_order.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        # check if there is extra element in seqs but not in org
        if len(graph) == len(topo_order):
            return topo_order
        
        return None
        
    def get_indegree(self, graph):
        indegree = {node: 0 for node in graph}
        for node in graph:
            for neighbor in graph[node]:
                indegree[neighbor] += 1
        
        return indegree
        
            