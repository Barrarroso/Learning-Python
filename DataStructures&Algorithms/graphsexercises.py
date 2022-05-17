class AdjacentVertex:
    """ This class allows us to represent a tuple
    with an adjacent vertex
    and the weight associated (by default None, for non-unweighted graphs)"""

    def __init__(self, vertex: object, weight: int = 1) -> None:
        self.vertex = vertex
        self.weight = weight

    def __str__(self) -> str:
        """ returns the tuple (vertex, weight)"""
        if self.weight is not None:
            return '(' + str(self.vertex) + ',' + str(self.weight) + ')'
        else:
            return str(self.vertex)


class Graph:
    def __init__(self, vertices: list, directed: bool = True) -> None:
        """ We use a dictionary to represent the graph
        the dictionary's keys are the vertices
        The value associated for a given key will be the list of their neighbours.
        Initially, the list of neighbours is empty"""
        self._vertices = {}
        for v in vertices:
            self._vertices[v] = []
        self._directed = directed

    def add_edge(self, start: object, end: object, weight: int = 1) -> None:
        if start not in self._vertices.keys():
            print(start, ' does not exist!')
            return
        if end not in self._vertices.keys():
            print(end, ' does not exist!')
            return

        # adds to the end of the list of neighbours for start
        self._vertices[start].append(AdjacentVertex(end, weight))

        if not self._directed:
            # adds to the end of the list of neighbors for end
            self._vertices[end].append(AdjacentVertex(start, weight))

    def contain_edge(self, start: object, end: object) -> int:
        """ checks if the edge (start, end) exits. It does
        not exist return 0, eoc returns its weight or 1 (for unweighted graphs)"""
        if start not in self._vertices.keys():
            print(start, ' does not exist!')
            return 0
        if end not in self._vertices.keys():
            print(end, ' does not exist!')
            return 0

        # we search the AdjacentVertex whose v is equal to end
        for adj in self._vertices[start]:
            if adj.vertex == end:
                return adj.weight

        return 0  # does not exist

    def remove_edge(self, start: object, end: object):
        """ removes the edge (start, end)"""
        if start not in self._vertices.keys():
            print(start, ' does not exist!')
            return
        if end not in self._vertices.keys():
            print(end, ' does not exist!')
            return

        # we must look for the adjacent AdjacentVertex (neighbour)  whose vertex is end, and then remove it
        for adj in self._vertices[start]:
            if adj.vertex == end:
                self._vertices[start].remove(adj)
        if not self._directed:
            # we must also look for the AdjacentVertex (neighbour)  whose vertex is end, and then remove it
            for adj in self._vertices[end]:
                if adj.vertex == start:
                    self._vertices[end].remove(adj)

    def __str__(self) -> str:
        """ returns a string containing the graph"""
        result = ''
        for v in self._vertices:
            result += '\n'+str(v)+':'
            for adj in self._vertices[v]:
                result += str(adj)+"  "
        return result

    def get_adjacents(self, v: str):
        """Add a method get_adjacents that receives a vertex v, and returns a Python list
        containing the vertices adjacents to v. The list only contains the vertices (not the
        weights)
        """

        if v not in self._vertices.keys():
            return

        result = []
        for adj in self._vertices[v]:
            result.append(adj.vertex)
        return result

    def get_origins(self, v: str):
        """Add a method, get_origins, that receives a vertex v, and that returns a Python list
        containing those vertices that are the origin of some edge whose destination is v. The
        list only contains the vertices (not the weights).
        """
        if v not in self._vertices.keys():
            return

        result = []
        for vertex in self._vertices.keys():
            for adj in self._vertices[vertex]:
                if adj.vertex == v:
                    result.append(vertex)

        return result

    def non_accessibles(self, v: str):
        """Add a method, non_accessibles, that receives a vertex v, and returns the list of
        vertices in the graph that are not accessible from v. A vertex end is not accessible from
        v if there is no path from v to this vertex
        """
        if v not in self._vertices.keys():
            return

        visited = {}
        for key in self._vertices.keys():
            visited[key] = False

        queue = []
        queue.append(v)
        visited[v] = True
        while len(queue) > 0:
            current = queue.pop(0)

            for adj in self._vertices[current]:
                if not visited[adj.vertex]:
                    queue.append(adj.vertex)
                    visited[adj.vertex] = True

        non_accessibles = []
        for vertex in visited.keys():
            if not visited[vertex]:
                non_accessibles.append(vertex)

        return non_accessibles

    def min_jumps(self, start:str, end:str):
        distances = {}
        for key in self._vertices.keys():
            distances[key] = 0

        visited = {}
        for key in self._vertices.keys():
            visited[key] = False

        queue = []
        queue.append(start)
        visited[start] = True
        while len(queue) > 0:
            current = queue.pop(0)

            for adj in self._vertices[current]:
                if not visited[adj.vertex]:
                    queue.append(adj.vertex)
                    visited[adj.vertex] = True
                    distances[adj.vertex] = distances[current] + 1

        return distances[end]


labels = ['A', 'B', 'C', 'D', 'E']
g = Graph(labels)

#https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/CPT-Graphs-directed-weighted-ex1.svg/722px-CPT-Graphs-directed-weighted-ex1.svg.png
# Now, we add the edges
g.add_edge('A', 'C', 12)  # A->(12)C
g.add_edge('A', 'D', 60)  # A->(60)D
g.add_edge('B', 'A', 10)  # B->(10)A
g.add_edge('C', 'B', 20)  # C->(20)B
g.add_edge('C', 'D', 32)  # C->(32)D
g.add_edge('E', 'A', 7)   # E->(7)A


print("Adjacent vertices to A:", g.get_adjacents('A'))
print("Origin vertices of D:", g.get_origins('D'))


print("Non accessible vertices from A:", g.non_accessibles('A'))
print("Minimum jumps to get from A to D:", g.min_jumps('A','D'))