class Graph: 
    def __init__(self,edges):
        self.edges = edges
        self.graph_dict = {}
        # same logic to convert self.edges to self.graph_dict (list to dictionary)
        for i in self.edges:
            self.graph_dict[i[0]] = []
        for i in self.graph_dict.keys():
            for j in self.edges:
                if i == j[0]:
                    self.graph_dict[i].append(j[1])
        
    def get_paths(self,start,end,path=[]):
        # takes start and end and return all the paths. 
        path = path + [start]
        if start == end:
            return [path]
        elif start  not in self.graph_dict.keys():
            return "No Route Available"
        paths = list()  # all possible paths.
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node,end,path)
                for p in new_paths:
                    paths.append(p)
        return paths

    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return path

        if start not in self.graph_dict:
            return None

        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp

        return shortest_path
    
routes1 = [
        ("Mumbai","Pune"),
        ("Mumbai", "Surat"),
        ("Surat", "Bangaluru"),
        ("Pune","Hyderabad"),
        ("Pune","Mysuru"),
        ("Hyderabad","Bangaluru"),
        ("Hyderabad", "Chennai"),
        ("Mysuru", "Bangaluru"),
        ("Chennai", "Bangaluru")
]

routes2 = [
    ("Mumbai", "Paris"),
    ("Mumbai", "Dubai"),
    ("Paris", "Dubai"),
    ("Paris", "New York"),
    ("Dubai", "New York"),
    ("New York", "Toronto"),
]

graph_routes = Graph(routes2)
print(graph_routes.graph_dict)
print("Paths between Mumbai and New York are ",graph_routes.get_paths("Mumbai","New York"))
print("Shortest Paths between Mumbai and New York are ",graph_routes.get_shortest_path("Mumbai","New York"))

"""
# MY LOGIC TO CONVERT TUPLES TO DICTIONARY . 
def list_to_dictionary(routes):  
        dic =  {}
        for i in routes:
            dic[i[0]] = []
        for i in dic.keys():
            for j in routes:
                if i == j[0]:
                    dic[i].append(j[1])
        return dic
"""
 
