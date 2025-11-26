from collections import deque
def valid(m, c): 
    return 0 <= m <= 3 and 0 <= c <= 3 and (m==0 or m>=c)
def solve():
    start, goal = (3,3,1), (0,0,0)
    q = deque([(start, [])])
    moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]
    while q:
        (mL, cL, b), path = q.popleft()
        if (mL, cL, b) == goal:
            for s in path + [goal]: print(s)
            return
        for dm, dc in moves:
            if b: new = (mL-dm, cL-dc, 0)
            else: new = (mL+dm, cL+dc, 1)
            if valid(*new[:2]) and valid(3-new[0], 3-new[1]):
                q.append((new, path + [(mL, cL, b)]))
solve()
