#Matthew Smith-Kennedy ms11ag


def runKruskal(self, edgelist, nodecount):
        edgelist.sort(key=returnweight)
        count = 0
        setlist =[]
        edgelist[count].selected =True
        count+=1
        setlist.append(set())
        setlist[0].add(edgelist[0])
        setcount = 1

        while count < len(edgelist):
            foundfirst = False
            foundsecond = False
            discard = False
            save1 = -1
            save2 = -1
            for j in range(0,setcount):

                for i in setlist[j]:
                    if i.Vertex2 == edgelist[count].Vertex1:
                        foundfirst = True
                        save1 =j
                    if i.Vertex2 == edgelist[count].Vertex2:
                        foundsecond = True
                        save2 = j
                    if i.Vertex1 == edgelist[count].Vertex1:
                        foundfirst = True
                        save1 = j
                    if i.Vertex1 == edgelist[count].Vertex2:
                        foundsecond = True
                        save2 = j
            if foundfirst is True and foundsecond is True and save1 == save2:
                discard = True
            else:
                if foundfirst and foundsecond:
                    if save1 < save2:
                        setlist[save1] = setlist[save1].union(setlist[save2])
                        setlist[save1].add(edgelist[count])
                        setlist[save2].clear()
                        edgelist[count].selected = True
                    else:    #if save2 > save1
                        setlist[save2] = setlist[save2].union(setlist[save1])
                        setlist[save1].clear()
                        setlist[save2].add(edgelist[count])
                        edgelist[count].selected = True
                else:
                    if foundfirst and not foundsecond:
                        setlist[save1].add(edgelist[count])
                        edgelist[count].selected = True
                    if not foundfirst and foundsecond:
                        setlist[save2].add(edgelist[count])
                        edgelist[count].selected = True
            if not foundfirst and not foundsecond:
                edgelist[count].selected=True
                setlist.append(set())
                setlist[setcount].add(edgelist[count])
                setcount+=1
            count+=1
        return


def returnweight(value):
    return value.weight



