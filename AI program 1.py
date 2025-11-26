from heapq import heappush, heappop
goal = [[1,2,3],[4,5,6],[7,8,0]]

def h(s): return sum(abs(i-(v-1)//3)+abs(j-(v-1)%3) for i in range(3) for j in range(3) if (v:=s[i][j])!=0)
def nbs(s):
    i,j=[(x,y) for x in range(3) for y in range(3) if s[x][y]==0][0]
    res=[]
    for x,y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
        if 0<=x<3 and 0<=y<3:
            t=[r[:] for r in s];t[i][j],t[x][y]=t[x][y],t[i][j];res.append(t)
    return res

def solve(s):
    pq=[(h(s),0,s,[])];seen=set()
    while pq:
        f,g,s,p=heappop(pq)
        if s==goal: return p+[s]
        t=tuple(sum(s,[]))
        if t in seen: continue
        seen.add(t)
        for nb in nbs(s): heappush(pq,(g+1+h(nb),g+1,nb,p+[s]))

start=[[1,2,3],[4,0,6],[7,5,8]]
for k,s in enumerate(solve(start)):
    print(f"Step {k}:");[print(r) for r in s];print()
   
