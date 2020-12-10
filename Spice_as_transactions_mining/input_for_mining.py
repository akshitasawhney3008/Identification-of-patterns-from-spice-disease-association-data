edgefile = open("Edge(disease 1-642).txt",'r')
edgeread = edgefile.readlines()
j = 0
for i in range(1,463):
    spicelist=[]
    for edge in edgeread:
        edgelist = edge.split()
        if(i == int(edgelist[1])):
            spicelist.append(edgelist[0])

    if(j == 0):
        edgewrite = open("Mining_input.txt", 'w')
        spicelist = list(set(spicelist))
        for spice in spicelist:
            edgewrite.write(str(spice) + " ")
        edgewrite.write("\n")
        j += 1
    else:
        edgewrite = open("Mining_input.txt", 'a')
        spicelist = list(set(spicelist))
        for spice in spicelist:
            edgewrite.write(str(spice) + " ")
        edgewrite.write("\n")