def graph(v):
    global node_count
    if v in nodes :
        print('node is present in graph')
    else:
        node_count=node_count +1
        nodes.append(v)
        for n in graph:
            n.append(0)
        temp=[]
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)
        


nodes=[]
graph=[]
node_count=0
print("before adding nodes")
print(nodes)
print(graph)
nodes.add_node("A")
print("after adding nodes")
print(nodes)
print(graph)
