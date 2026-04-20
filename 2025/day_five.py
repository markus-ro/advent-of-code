from sys import argv
from pathlib import Path

class IngredientDatabase:
    def __init__(self):
        self.ranges = []
    
    def add_range(self, start, end):
        self.ranges.append(range(start, end + 1))

    def is_in_range(self, _id, exclude_range = None):
        for _range in self.ranges:
            if _range == exclude_range:
                continue
            if _id in _range:
                return _range
        return None

    def is_fresh(self, ingredient_id):
        return self.is_in_range(ingredient_id) != None
    
    def __len__(self):
        return len(self.ranges)
    
    def __str__(self):
        t = sorted(self.ranges, key=lambda x: x.start)
        t = sorted(t, key=lambda x: x.stop)
        return str("\n".join([str(x) for x in t]))

def setup_database(puzzle_data):
    datatbase = IngredientDatabase()

    for i, line in enumerate(puzzle_data):
        if line.strip() == "":
            ingredient_ids = [int(x) for x in puzzle_data[i + 1:]]
            break

        _range = [int(x) for x in line.strip().split("-")]
        datatbase.add_range(_range[0], _range[1])
    
    return datatbase, ingredient_ids

def solution_star_one(datatbase, ingredient_ids):
    fresh = 0
    for _id in ingredient_ids:
        if datatbase.is_fresh(_id):
            fresh += 1
    
    return fresh

def solution_star_two(datatbase):
    sorted_ranges = sorted(datatbase.ranges, key=lambda x: x.start)

    merged_ranges = [sorted_ranges[0]]
    for _range in sorted_ranges[1:]:
        if _range.start > merged_ranges[-1].stop:
            merged_ranges.append(_range)
            continue
        
        merged_ranges[-1] = range(merged_ranges[-1].start,
                                  max(_range.stop, merged_ranges[-1].stop))

    return sum(len(x) for x in merged_ranges)

if __name__ == "__main__":
    puzzle_data = Path(argv[1]).open().readlines()
    datatbase, ingredient_ids = setup_database(puzzle_data)

    print("Solution Star One:", solution_star_one(datatbase, ingredient_ids))
    print("Solution Star Two:", solution_star_two(datatbase))