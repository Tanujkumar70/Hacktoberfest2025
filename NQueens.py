def solve_n_queens(n: int):
    res = []
    cols, diag1, diag2 = set(), set(), set()
    board = [["."] * n for _ in range(n)]

    def backtrack(r: int):
        if r == n:
            res.append(["".join(row) for row in board])
            return
        for c in range(n):
            if c in cols or (r - c) in diag1 or (r + c) in diag2:
                continue
            cols.add(c); diag1.add(r - c); diag2.add(r + c)
            board[r][c] = "Q"
            backtrack(r + 1)
            board[r][c] = "."
            cols.remove(c); diag1.remove(r - c); diag2.remove(r + c)

    backtrack(0)
    return res


def count_n_queens(n: int) -> int:
    """
    Return the number of solutions using bitmasks (fast).
    Columns, main- and anti-diagonals encoded as bitsets.
    """
    full = (1 << n) - 1

    def dfs(cols: int, d1: int, d2: int) -> int:
        if cols == full:
            return 1
        free = full & ~(cols | d1 | d2)
        total = 0
        while free:
            bit = free & -free
            free -= bit
            total += dfs(
                cols | bit,
                (d1 | bit) << 1 & full,
                (d2 | bit) >> 1
            )
        return total

    return dfs(0, 0, 0)

if __name__ == "__main__":
    n = 4
    sols = solve_n_queens(n)
    print(f"{n}-Queens: {len(sols)} solutions\n")
    for i, b in enumerate(sols, 1):
        print(f"Solution {i}:")
        print("\n".join(b))
        print()

    print("Count via bitmasks:", count_n_queens(n))