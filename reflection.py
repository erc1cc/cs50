import sys

def representative(r, c, N):
    half = N // 2

    if r < half:
        if c >= half:
            return (r, c)
        else:
            return (r, N - 1 - c)
    else:
        if c >= half:
            return (N - 1 - r, c)
        else:
            return (N - 1 - r, N - 1 - c)

def solve():
    input_data = sys.stdin.read().split()
    it = iter(input_data)
    N = int(next(it))
    U = int(next(it))
    grid = [list(next(it).strip()) for _ in range(N)]
    half = N // 2

    group_count = {}
    total_cost = 0

    for i in range(half):
        for j in range(half, N):
            cnt = 0
            cells = [
                (i, j),
                (i, N - 1 - j),
                (N - 1 - i, j),
                (N - 1 - i, N - 1 - j)
            ]
            for (r, c) in cells:
                if grid[r][c] == '#':
                    cnt += 1
            group_count[(i, j)] = cnt
            total_cost += min(cnt, 4 - cnt)

    output_lines = []
    output_lines.append(str(total_cost))
    
    for _ in range(U):
        r = int(next(it)) - 1
        c = int(next(it)) - 1
        
        rep = representative(r, c, N)
        old_cnt = group_count[rep]
        old_cost = min(old_cnt, 4 - old_cnt)
        
        if grid[r][c] == '#':
            grid[r][c] = '.'
            delta = -1
        else:
            grid[r][c] = '#'
            delta = 1
        
        new_cnt = old_cnt + delta
        group_count[rep] = new_cnt
        new_cost = min(new_cnt, 4 - new_cnt)
        
        total_cost += (new_cost - old_cost)
        output_lines.append(str(total_cost))
    
    sys.stdout.write("\n".join(output_lines))

solve()
