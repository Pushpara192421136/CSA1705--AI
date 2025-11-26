def nq(n):
    R=[]; b=[-1]*n
    def valid(r,c):
        for i in range(r):
            if b[i]==c or abs(b[i]-c)==r-i: return False
        return True
    def dfs(r):
        if r==n: R.append(b.copy()); return
        for c in range(n):
            if valid(r,c):
                b[r]=c; dfs(r+1); b[r]=-1
    dfs(0); return R

for sol in nq(8):
    for r in range(8):
        print(' '.join('Q' if sol[r]==c else '-' for c in range(8)))
    print()
 
