import typing as tp
import pathlib
import random

import pprint as pp


def display(grid: list):
    """Красивый вывод поля"""
    interval = int(len(grid) ** 0.5)
    out = [[] for i in range(len(grid))]
    for y in range(len(grid)):
        for x in range(len(grid)):
            out[y].append(grid[y][x])
            if (x + 1) % interval == 0 and x + 1 != len(grid):
                out[y].append("|")
        out[y] = " ".join(out[y])
    cross_line = "-" * interval * 2 + "+" + \
        ("-" * interval * 2 + "-" + "+") * (interval - 2) + "-" * interval * 2
    for i in range(len(grid)):
        print(out[i])
        if (i + 1) % interval == 0:
            print(cross_line)


def create_grid(puzzle: str) -> tp.List[tp.List[str]]:
    digits = [c for c in puzzle if c in "123456789."]
    grid = group(digits, 9)
    return grid


def read_sudoku(path: tp.Union[str, pathlib.Path]) -> tp.List[tp.List[str]]:
    """ Прочитать Судоку из указанного файла """
    path = pathlib.Path(path)
    with path.open() as f:
        puzzle = f.read()
    return create_grid(puzzle)


T = tp.TypeVar("T")


def group(values: tp.List[T], n: int) -> tp.List[tp.List[T]]:
    """
    Сгруппировать значения values в список, состоящий из списков по n элементов

    >>> group([1,2,3,4], 2)
    [[1, 2], [3, 4]]
    >>> group([1,2,3,4,5,6,7,8,9], 3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    out = []
    for i in range(0, len(values), n):
        out.append(values[i:i + n])
    return out


def get_row(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """ Возвращает все значения для номера строки, указанной в pos

    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """

    row, col = pos
    return grid[row]

def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """ Возвращает все значения для номера столбца, указанного в pos

    >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    ['2', '.', '8']
    >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    """

    row, col = pos
    return [i[col] for i in grid]

def get_block(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """ Возвращает все значения из квадрата, в который попадает позиция pos

    >>> grid = read_sudoku('puzzle1.txt')
    >>> get_block(grid, (0, 1))
    ['5', '3', '.', '6', '.', '.', '.', '9', '8']
    >>> get_block(grid, (4, 7))
    ['.', '.', '3', '.', '.', '1', '.', '.', '6']
    >>> get_block(grid, (8, 8))
    ['2', '8', '.', '.', '.', '5', '.', '7', '9']
    """
    row, col = pos
    y, x = range_coord(row), range_coord(col)
    out = []
    for i in y:
        for j in x:
            out.append(grid[i][j])
            
    return out
    
def range_coord(coord: int):
    if 0 <= coord <= 2:
        out = range(0, 3)
    if 2 < coord <= 5:
        out = range(3, 6)
    if coord > 5:
        out = range(6, 9)
    return out

def solve(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.List[tp.List[str]]]:
    free_points = []
    for y in range(len(grid)):
        for x in range(len(grid)):
            if grid[y][x] == ".":
                free_points.append((y, x))

    return perm_points(grid.copy(), free_points)

def perm_points(grid: list, free_points: list):
    if not free_points:
        return grid

    point = free_points[0]
    y, x = point
    row_values = set(get_row(grid, point))
    col_values = set(get_col(grid, point))
    block_values = set(get_block(grid, point))

    used = row_values | col_values | block_values
    used.discard('.')

    possible = set(map(str, range(1,10))) - used

    for value in possible:
        grid[y][x] = value
        solution = perm_points(grid, free_points[1:])
        if solution is not None:
            return solution
        grid[y][x] = '.'

    return None

def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    """ Если решение solution верно, то вернуть True, в противном случае False """
    for row in solution:
        if len(set(row)) != len(solution):
            return False
        
    for x in range(len(solution)):
        if len(set([solution[y][x] for y in range(len(solution))])) != len(solution):
            return False
    
    for x in range(0, len(solution), interval := int(len(solution) ** 0.5)):
        for y in range(0, len(solution), interval):
            block = []
            for i in range(interval):
                block += solution[y + i][x:x + interval]
            if len(set(block)) != len(solution):
                return False
    return True

def generate_sudoku(N: int) -> tp.List[tp.List[str]]:
    """ Генерация судоку заполненного на N элементов
    >>> grid = generate_sudoku(40)
    >>> sum(1 for row in grid for e in row if e == '.')
    41
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(1000)
    >>> sum(1 for row in grid for e in row if e == '.')
    0
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(0)
    >>> sum(1 for row in grid for e in row if e == '.')
    81
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    """
    grid = solve([['.' for _ in range(9)] for _ in range(9)])
    if N >= 81:
        return grid
    positions = [(i, j) for i in range(9) for j in range(9)]
    random.shuffle(positions)
    for pos in positions:
        if sum(1 for row in grid for e in row if e != '.') <= N:
            break
            
        y, x = pos
        temp = grid[y][x]
        grid[y][x] = '.'
        
        temp_grid = [row[:] for row in grid]
        solution = solve(temp_grid)

        if solution is not None:
            continue
        else:
            grid[y][x] = temp
    
    return grid
        

if __name__ == "__main__":
    from pprint import pprint as pp
    grid = read_sudoku('puzzle1.txt')
    display(grid)
    solution = solve(grid)
    display(solution)
    check = check_solution(solution)
    print("Solution is correct" if check else "Ooops")