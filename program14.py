b=[[" "]*3 for _ in range(3)]
def p(): [print("|".join(r)) for r in b]; print()
def w(p): return any(all(c==p for c in r) for r in b) or any(all(b[r][i]==p for r in range(3)) for i in range(3)) or all(b[i][i]==p for i in range(3)) or all(b[i][2-i]==p for i in range(3))
def ab(mx,alpha,beta):
    if w("O"): return 1
    if w("X"): return -1
    if all(c!=" " for r in b for c in r): return 0
    if mx:
        v=-9
        for i in range(3):
            for j in range(3):
                if b[i][j]==" ":
                    b[i][j]="O"; v=max(v,ab(False,alpha,beta)); b[i][j]=" "
                    alpha=max(alpha,v); 
                    if beta<=alpha: return v
        return v
    else:
        v=9
        for i in range(3):
            for j in range(3):
                if b[i][j]==" ":
                    b[i][j]="X"; v=min(v,ab(True,alpha,beta)); b[i][j]=" "
                    beta=min(beta,v)
                    if beta<=alpha: return v
        return v
def best():
    mv,s=None,-9
    for i in range(3):
        for j in range(3):
            if b[i][j]==" ":
                b[i][j]="O"; v=ab(False,-9,9); b[i][j]=" "
                if v>s: s,mv=v,(i,j)
    return mv
while True:
    p(); r,c=map(int,input("Your move row,col:").split(",")); b[r][c]="X"
    if w("X") or all(c!=" " for r in b for c in r): p(); print("Game over"); break
    i,j=best(); b[i][j]="O"
    if w("O"): p(); print("AI wins"); break
