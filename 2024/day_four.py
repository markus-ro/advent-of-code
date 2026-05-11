from pathlib import Path
from sys import argv

def solution_star_one(character_matrix: list[list[str]]) -> int:
    def find_word_in_direction(i: int, j: int, direction: tuple[int, int], word: str):
        for k in range(len(word)):
            ni, nj = i + k * direction[0], j + k * direction[1]
            if ni < 0 or ni >= len(character_matrix): return 0
            if nj < 0 or nj >= len(character_matrix[0]): return 0
            if character_matrix[ni][nj] != word[k]: return 0
        return 1

    occurrences = 0
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1),  (1, 0),  (1, 1)]
    
    for i in range(len(character_matrix)):
        for j in range(len(character_matrix[i])):
            if character_matrix[i][j] == "X":
                for di, dj in directions:
                    occurrences += find_word_in_direction(i, j, (di, dj), "XMAS")

    return occurrences

def solution_star_two(character_matrix: list[list[str]]) -> int:
    def find_x_mas(i: int, j: int):
        if character_matrix[i][j] != "A": return 0
        if {character_matrix[i-1][j-1], character_matrix[i+1][j+1]} != {"M", "S"}: return 0
        if {character_matrix[i-1][j+1], character_matrix[i+1][j-1]} != {"M", "S"}: return 0
        return 1
    
    occurrences = 0
    for i in range(1, len(character_matrix) - 1):
        for j in range(1, len(character_matrix[i]) - 1):
            occurrences += find_x_mas(i, j)

    return occurrences

if __name__ == "__main__":
    file_content = Path(argv[1]).open().read()
    character_matrix = [list(line) for line in file_content.splitlines()]
    print("Solution Star One:", solution_star_one(character_matrix))
    print("Solution Star Two:", solution_star_two(character_matrix))