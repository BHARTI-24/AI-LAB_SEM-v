from collections import defaultdict

class graph:
    def __init__(self,vertices):
        self.v= vertices
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def DLS(self,src,target,maxDepth):
        if src==target:
            return True
        if maxDepth<=0:
            return False

        for i in self.graph[src]:
            if(self.DLS(i,target,maxDepth-1)):
                return True
        return False

    def IDDFS(self,src,target,maxDepth):

        for i in range(maxDepth):
            if(self.DLS(src,target,i)):
                return True
        return False

g= graph(7);

g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,3)
g.addEdge(1,4)
g.addEdge(2,5)
g.addEdge(2,6)

target=6
maxDepth=2
src=0

if g.IDDFS(src,target,maxDepth)== True:
    print("target is reachable")
else:
    print("target is not reachable")
