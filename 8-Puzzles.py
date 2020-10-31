from eight_puzzle import EightPuzzle

def heur(puzzle, item_total_calc, total_calc):
    t = 0
    for row in range (3):
        for col in range (3):
            val = puzzle.peek (row, col) - 1
            target_col = val % 3
            target_row = val / 3
            if target_row < 0:
                target_row = 2

            t += item_total_calc (row, target_row, col, target_col)

    return total_calc (t)

def h_manhattan(puzzle):
    return heur (puzzle,
                 lambda r, tr, c, tc: abs (tr - r) + abs (tc - c),
                 lambda t: t)


def h_default(puzzle):
    return 0


def main():
    p = EightPuzzle()
    p.shuffle(20)
    print(p)

    path, count = p.solve(h_manhattan)
    path.reverse ()
    for i in path:
        print (i)

main ()