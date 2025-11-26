from collections import deque

def water_jug(x, y, target):
    visited = set()
    q = deque([(0, 0)])  # (jug1, jug2)

    while q:
        a, b = q.popleft()
        if (a, b) in visited:
            continue
        visited.add((a, b))
        print(a, b)
        if a == target or b == target:
            print("Reached target!")
            return
        q.extend([
            (x, b), 
            (a, y),  
            (0, b), 
            (a, 0), 
            (a - min(a, y - b), b + min(a, y - b)), 
            (a + min(b, x - a), b - min(b, x - a))   
        ])
water_jug(4, 3, 2)
