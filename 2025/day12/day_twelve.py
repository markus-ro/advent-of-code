from pathlib import Path
from sys import argv

class Present:
    def __init__(self, present_id, present_ascii):
        self.present_id = present_id
        self.present_ascii = present_ascii
        self.size = "".join(present_ascii).count("#")
    
    def __str__(self):
        return f"Present({self.present_id=}, {self.present_ascii=}, {self.size=})"

    def __repr__(self):
        return str(self)

class Tree:
    def __init__(self, width, height, presents):
        self.width = width
        self.height = height
        self.presents = presents
    
    def __str__(self):
        return f"Tree({self.width=}, {self.height=}, {self.presents=})"
    
    def __repr__(self):
        return str(self)

def solution_star_one(trees, presents):
    fitting_trees = 0
    for tree in trees:
        tree_area, presents_area = tree.width * tree.height, 0
    
        for i, count in enumerate(tree.presents):
            presents_area += presents[i].size * count
        
        if tree_area >= presents_area:
            fitting_trees += 1
    return fitting_trees

if __name__ == "__main__":
    input_data = Path(argv[1]).open().readlines()
    presents = dict()
    trees = []

    for i in range(len(input_data)):
        cur_line = input_data[i].strip()
        if cur_line == "": continue

        if cur_line[1] == ":":
            present_id = int(cur_line[0])
            present_ascii = [input_data[i + 1].strip(), input_data[i + 2].strip(), input_data[i + 3].strip()]
            presents[present_id] = Present(present_id, present_ascii)
        elif cur_line[2] == "x":
            size, p_ids = cur_line.split(":")
            width, height = size.strip().split("x")
            tree_presents = [int(x) for x in p_ids.strip().split(" ")]
            trees.append(Tree(int(width), int(height), tree_presents))

    print("Solution Star One:", solution_star_one(trees, presents))

    print("Solution Star Two:", "Merry Christmas!")

