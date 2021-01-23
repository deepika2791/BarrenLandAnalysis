import collections


class Field():
    """
    Class to represent complete farm

    Attributes
    ----------
    length : int  
    width : int
    barren_land : (private) list of barren edges 
    """

    def __init__(self, length, width):
        self.length = int(length)
        self.width = int(width)
        self._barren_land = []

    @staticmethod
    def neighbors(node):
        """
        Find the points connected to a node
        Args:
            param1: (tuple) coordinate of the node
        Returns list
        """
        x = node[0]
        y = node[1]

        if x == 0 and y == 0:
            return [(x+1, y), (x, y+1)]

        if x > 0 and y == 0:
            return [(x-1, y), (x+1, y), (x, y+1)]

        if x == 0 and y > 0:
            return [(x, y-1), (x+1, y), (x, y+1)]

        if x > 0 and y > 0:
            return [(x-1, y), (x, y-1), (x, y+1), (x+1, y)]

    def _is_bad(self, node):
        """
        Check if a node is inside barren land
        Args:
            param1: The node to be checked
            param2: The list of barren edges
        Returns True or False
        """
        for point in self._barren_land:
            p1, p2 = point
            if node[0] >= p1[0] and node[0] <= p2[0] and node[1] >= p1[1] and node[1] <= p2[1]:
                    return 1
        return 0


    def _traverse(self):
        """
        Traverse all coordinates looking for connected components
        Args:
            param1: (int) The length of the graph
            param2: (int) The width of the graph
            param3: (list) The coordinates of the barren land
        Returns:
            (list) A list containing the connected components
        """
        all_coordinates = [(i, j) for i in range(self.width) for j in range(self.length)]
        visited = set()
        final = []
        queue = collections.deque()

        for point in all_coordinates:
            queue.append(point)
            fertile_area = []

            while queue:
                node = queue.popleft()

                if (node[0] < self.width and node[1] < self.length):
                    if node not in visited:
                        visited.add(node)

                        if not self._is_bad(node):
                            fertile_area.append(node)

                        child_nodes = self.neighbors(node)
                        for child_node in child_nodes:
                            if not self._is_bad(child_node):
                                queue.append(child_node)

            if fertile_area:
                final.append(fertile_area)

        return final

    @staticmethod
    def _barren_points(barren_data):
        """
        Args:
            param1:  A string containing the
            bottom left and top right corners
        Returns list of list containing int coordinates 
            of all barren lands
        """
        barr_points = []
        for data in barren_data:
            points = []
            i = 0
            data = data.split()
            while i < len(data):
                points.append((int(data[i]), int(data[i+1])))
                i +=2 
            barr_points.append(points)
        return barr_points

    def fertile_land(self, barren_data):
        """
        Function to check fertile land area
        Args:
            param1: string length of field
            param2: string width of field
            param3: string points of barren edges
        returns Sorted fertile land area
        """

        self._barren_land = self._barren_points(barren_data)
        land = self._traverse()

        if not land:
            return '0'

        total_area = [str(len(area)) for area in land]
        total_area.sort(reverse=True)
        return ' '.join(total_area)
