from sys import argv
from pathlib import Path

class StorageLayout:
    def __init__(self, in_layout, copy=True):
        self._height = len(in_layout)
        self._width = len(in_layout[0].strip())
        self._layout = [x for x in in_layout] if copy else in_layout

    def __call__(self, row, col):
        if row < 0 or col < 0:
            return 0
        
        if row >= self._height\
            or col >= self._width:
            return 0
        
        return 1 if self._layout[row][col] == "@" else 0

    def check_accessible(self, row, col):
        adjacent_rolls = 0
        adjacent_rolls += self(row-1, col-1)
        adjacent_rolls += self(row+1, col+1)

        adjacent_rolls += self(row, col-1)
        adjacent_rolls += self(row-1, col)

        adjacent_rolls += self(row, col+1)
        adjacent_rolls += self(row+1, col)

        adjacent_rolls += self(row+1, col-1)
        adjacent_rolls += self(row-1, col+1)

        if self(row, col) and adjacent_rolls < 4:
            return True

    def remove_accessible(self):
        new_layout = []
        removed = 0
        for r in range(self._height):
            new_row = ""
            for c in range(self._width):
                if self.check_accessible(r, c):
                    removed += 1
                    new_row += "."
                else:
                    new_row += "@" if self(r, c) else "."
            
            new_layout.append(new_row)


        t = StorageLayout(new_layout, copy=False)
        return removed, t

def solution_star_one(storage: StorageLayout):
    accessible_rolls, _ = storage.remove_accessible()
    return accessible_rolls

def solution_star_two(storage: StorageLayout):
    storage_iter = storage
    total_removed = 0

    while True:
        removed, storage_iter = storage_iter.remove_accessible()
        total_removed += removed
        if removed == 0: break

    return total_removed

if __name__ == "__main__":
    printing_storage = Path(argv[1]).open().readlines()
    storage = StorageLayout(printing_storage)
    
    print("Solution Star One:", solution_star_one(storage))
    print("Solution Star Two:", solution_star_two(storage))
