from graphviz import Digraph
from graphviz import Graph

file_name = 'test1.png'
# dot = Digraph()
dot = Graph()
dot.node('A', 'A1')
dot.node('B', 'B')
dot.node('C', 'C')
dot.node('D', 'D')

dot.edges(['AB', 'AB', 'AB', 'BC', 'BA', 'CB', 'CA', 'DA', 'CD', 'BD', 'DB'])

# dot.edge('A', 'B', [] )

print(dot.source)
dot.render(file_name, view=True)



