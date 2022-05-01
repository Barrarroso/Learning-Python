#David Barroso
#29/4/2022
#In this exam the data structure was a binary search tree with a date of registration of clients
#formatted as YYYY: MM: DD: HH:MM
#I had to develop a method that returns the difference of registered clients between two given years
#yearsRegistrationDiff(year1:str, year2:str)

class MyNode:
    def __init__(self, elem: int, node_left: 'MyNode' = None, node_right: 'MyNode' = None) -> None:
        self.elem = elem
        self.left = node_left
        self.right = node_right


class MyBST:
    def __init__(self) -> None:
        """creates an empty binary tree
        I only has an attribute: _root"""
        self._root = None

    def add(self, elem: int) -> None:
        if self._root is None:
            self._root = MyNode(elem)  # if tree is empty, new node will be the root
            return  # we can leave!!!

        node = self._root  # to search the place
        not_exist = True
        while not_exist and node:
            if elem < node.elem:
                if node.left is None:  # this is the place to insert it
                    node.left = MyNode(elem)
                    not_exist = False
                else:
                    node = node.left
            elif elem > node.elem:
                if node.right is None:  # this is the place to insert it
                    node.right = MyNode(elem)
                    not_exist = False
                else:
                    node = node.right
            elif elem == node.elem:
                print('duplicate elements not allowed!!', elem, node.elem)
                not_exist = False

    def remove(self, elem: object) -> None:
        self._root = self._remove(self._root, elem)

    def _remove(self, node: MyNode, elem: object) -> MyNode:
        if node is None:
            print(elem, ' not found')
            return node

        if elem < node.elem:
            node.left = self._remove(node.left, elem)
        elif elem > node.elem:
            node.right = self._remove(node.right, elem)
        else:
            # node.elem == elem, node is the node to remove!!!
            if node.left is None and node.right is None:
                # Case 1: node is a leave
                return None
            # Case 2: node only has a child, so the function has to return it
            if node.left is None:
                # It only has the right child
                return node.right
            elif node.right is None:
                # It only has the left child
                return node.left
            else:
                successor = self._minimum_node(node.right)
                node.elem = successor.elem
                node.right = self._remove(node.right, successor.elem)

        return node

    def draw(self) -> None:
        """function to draw a tree. """
        if self._root:
            self._draw('', self._root, False)
        else:
            print('tree is empty')
        print('\n')

    def _draw(self, prefix: str, node: MyNode, is_left: bool) -> None:
        if node is not None:
            self._draw(prefix + "     ", node.right, False)
            print(prefix + "|-- " + str(node.elem))
            self._draw(prefix + "     ", node.left, True)

    def yearsRegistrationDiff(self, year1: str, year2: str) -> int:
        """Receives 2 years as input parameters and returns
        an integer with the difference between the number of clients 
        registered in year1 and the number of clients registered in year2"""
        if type(year1) != str or type(year2) != str:
            raise TypeError("The parameters 'year1' and 'year2' must be strings")
        if len(year1) != 4:
            raise ValueError("The parameter 'year1' must have a length of 4")
        if len(year2) != 4:
            raise ValueError("The parameter 'year2' must have a length of 4")

        clients_year1 = self.clients_registered_in_year(year1)
        clients_year2 = self.clients_registered_in_year(year2)
        return clients_year1 - clients_year2

    def clients_registered_in_year(self, year: str) -> int:
        """Receives a year string of 4 characters, example: "2022"
        and returns the number of registered clients in that year as
        an integer"""
        return self._clients_registered_in_year(self._root, year)

    def _clients_registered_in_year(self, node: MyNode, year: str) -> int:
        # base case
        if node is None:
            return 0

        # num of registered clients in the left subtree
        registered_left = self._clients_registered_in_year(node.left, year)
        # num of registered clients in the right subtree
        registered_right = self._clients_registered_in_year(node.right, year)

        # sample node element: "202104271600"
        # we look at the first 4 characters to check if the year of register of the current node
        # is the same as the year which we are counting clients for
        if node.elem[:4] == year:
            # we add 1 to the registered clients in the left and right subtree
            return 1 + registered_left + registered_right
        else:
            # return the number of registered clients in the left and right subtree
            return registered_left + registered_right


if __name__ == "__main__":

    tree = MyBST()

    for x in ["202104271600", "202001231710", "202201230510", "202201231710", "202103031243", "201909211100",
              "202110221243", "201912031243", "202204271742", "202110031243"]:
        tree.add(x)

    tree.draw()

    print(tree.yearsRegistrationDiff("2021", "2022"))
    print(tree.yearsRegistrationDiff("2022", "2021"))
    print(tree.yearsRegistrationDiff("2021", "2020"))
    print(tree.yearsRegistrationDiff("2020", "2019"))
    print(tree.yearsRegistrationDiff("2019", "2018"))
    print(tree.yearsRegistrationDiff("2019", "2022"))
