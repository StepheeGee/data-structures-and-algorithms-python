class Graph:
    """
    A class representing a graph.
    """

    def __init__(self):
        """
        Initializes an empty graph.
        """
        self.vertices = {}

    def add_vertex(self, node):
        """
        Adds a new vertex to the graph.
        """
        self.vertices[node] = []

    def add_node(self, node):
        """
        Adds a new node to the graph.
        """
        self.add_vertex(node)
        return node

    def add_edge(self, start, end):
        """
        Adds a directed edge between two vertices.
        """
        self.vertices[start].append(end)

    def breadth_first(self, start_node):
        """
        Performs breadth-first traversal starting from the given node.

        Arguments:
        - start_node: The starting node for the traversal.

        Returns:
        A collection of nodes in the order they were visited.
        """
        visited = set()
        result = []
        queue = [start_node]

        while queue:
            current_node = queue.pop(0)
            if current_node not in visited:
                result.append(current_node)
                visited.add(current_node)
                queue.extend(neighbor for neighbor in self.vertices[current_node] if neighbor not in visited)

        # Display the collection
        print(result)
        return result


class Vertex:
    pass

# Example usage:
# graph = Graph()
# graph.add_node("Pandora")
# graph.add_node("Arendelle")
# graph.add_node("Metroville")
# ... (rest of the nodes)
# graph.breadth_first("Pandora")
