#Matthew Smith-Kennedy ms11ag


class Edge (object):
    Vertex1 = int
    Vertex2 = int
    weight = int
    extra = int
    selected = False

    def __repr__(self):
        return ("V1:  " + str(self.Vertex1) + "  V2:  " +str(self.Vertex2)+ "  W:  "+ str(self.weight)+ "  SEL:  "+ str(self.selected))

