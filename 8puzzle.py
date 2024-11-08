8 puzzle code

class Node:
    def __init__(self, data, level, fval):
        """ Initialize the node with the data, level of the node and the calculated fvalue """
        self.data = data  # matrix
        self.level = level  # depth (g-value)
        self.fval = fval  # g+h value (f-value)

    def generate_child(self):
        """ Generate child nodes from the given node by moving the blank space
            either in the four directions {up, down, left, right} """
        x, y = self.find(self.data, '_')  # find row and col index of blank space
        val_list = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]  # 4 possibilities to move blank space
        children = []
        for i in val_list:  # make and check all children nodes
            child = self.shuffle(self.data, x, y, i[0], i[1])
            if child is not None:
                child_node = Node(child, self.level + 1, 0)
                children.append(child_node)
        return children

    def shuffle(self, puz, x1, y1, x2, y2):
        """ Move the blank space in the given direction and if the position value is out
            of limits, return None """
        if 0 <= x2 < len(self.data) and 0 <= y2 < len(self.data):
            temp_puz = self.copy(puz)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            return temp_puz
        else:
            return None

    def copy(self, root):
        """ Copy function to create a similar matrix of the given node"""
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp

    def find(self, puz, x):
        """ Specifically used to find the position of the blank space """
        for i in range(len(self.data)):
            for j in range(len(self.data)):
                if puz[i][j] == x:
                    return i, j

    def __eq__(self, other):
        """ Check if two puzzle states are equal """
        return self.data == other.data


class Puzzle:
    def __init__(self, size):
        """ Initialize the puzzle size by the specified size, open and closed lists to empty """
        self.n = size
        self.open = []  # open list to store nodes to be explored
        self.closed = []  # closed list to store already explored nodes

    def accept(self):
        """ Accepts the puzzle from the user in Jupyter Notebook as a list of lists """
        puz = []
        print(f"Enter the {self.n}x{self.n} matrix:")
        for i in range(self.n):
            # Here we can simulate the input as a list of strings to mimic 'input()' behavior in Jupyter
            row = input(f"Enter row {i+1} (space-separated): ").strip()
            puz.append(row.split())
        return puz

    def f(self, start, goal):
        """ Heuristic Function to calculate f(x) = h(x) + g(x) """
        return self.h(start.data, goal) + start.level

    def h(self, start, goal):
        """ Calculates the difference between the given puzzles (misplaced tiles heuristic) """
        temp = 0
        for i in range(self.n):  # check difference between goal and puzzle blank space or wrong data in 3*3 matrix
            for j in range(self.n):
                if start[i][j] != goal[i][j] and start[i][j] != '_':
                    temp += 1
        return temp

    def process(self):
        """ Accept Start and Goal Puzzle state """
        print("Enter the start state matrix (3x3) \n")
        start = self.accept()
        print("Enter the goal state matrix (3x3) \n")
        goal = self.accept()

        start = Node(start, 0, 0)
        start.fval = self.f(start, goal)
        self.open.append(start)

        while True:
            if not self.open:
                print("No solution exists.")
                break

            # Pop the node with the smallest f-value from the open list
            cur = self.open.pop(0)

            # Print current puzzle state
            print("\nCurrent State:")
            for row in cur.data:
                print(" ".join(row))

            # If we have reached the goal state, break out
            if self.h(cur.data, goal) == 0:
                print("\nGoal State Reached!")
                break

            # Generate children (next possible moves)
            children = cur.generate_child()
            for child in children:
                child.fval = self.f(child, goal)

                # If the child is not in the closed list, add it to the open list
                if not any(self.compare(child.data, n.data) for n in self.closed):
                    self.open.append(child)

            # Move the current node to the closed list
            self.closed.append(cur)

            # Sort the open list based on f-value (lowest f-value at the front)
            self.open.sort(key=lambda x: x.fval, reverse=False)

    def compare(self, state1, state2):
        """ Compare if two puzzle states are the same """
        for i in range(self.n):
            for j in range(self.n):
                if state1[i][j] != state2[i][j]:
                    return False
        return True


# Main function to execute the puzzle solver
puz = Puzzle(3)  # 3x3 puzzle (8-puzzle)
puz.process()
