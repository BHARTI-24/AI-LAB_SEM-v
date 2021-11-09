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
    

# iterative deepening depth first search 
    def IDDFS(self,src,target,maxDepth):
        # recursively callng for all nodes
        for i in range(maxDepth):
            if(self.DLS(src,target,i)):
                return True
        return False

    def generate_edges(self,graph):
        edges = []
      
        # for each node in graph
        for node in self.graph:
              
            # for each neighbour node of a single node
            for neighbour in self.graph[node]:
                  
                # if edge exists then append
                edges.append((node, neighbour))
        return edges
        
        
        
        
g= graph(7);

g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,3)
g.addEdge(1,4)
g.addEdge(2,5)
g.addEdge(2,6)
g.addEdge(3,7)
g.addEdge(3,8)
g.addEdge(4,9)
g.addEdge(4,10)



print(g.generate_edges(graph))


print("\n\nEnter target node to search: ")
value=input()
target=int(value)

maxDepth=4
src=0

## printing graph
node=[]
node=g.generate_edges(graph)

for x in node:
    print(x)
print("\n")


if g.IDDFS(src,target,maxDepth)== True:
    print("target => "+ value +" is reachable in GRAPH")
else:
    print("target  => "+ value +" is not reachable!!")
