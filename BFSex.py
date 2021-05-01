# Experiments

# Using a Python dictionary to act as an adjacency list
graph = {
  'A' : ['B','C'],
  'B' : ['D','E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)
  print("visited",visited)
  print("queue",queue)
  
  while queue:
    s = queue.pop(0) 
    print ("*"+s) # NODE ###########
    print("visited",visited)
    print("queue",queue)
    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
        print("visited",visited)
        print("queue",queue)

# Driver Code
bfs(visited, graph, 'A')



# s = [1,2,3,4,5,6]
# print(s)
# x=s.pop(0)
# print(s)
# print(x)
# # s.append(7)
# # print(s)

# # print(graph['A'])
