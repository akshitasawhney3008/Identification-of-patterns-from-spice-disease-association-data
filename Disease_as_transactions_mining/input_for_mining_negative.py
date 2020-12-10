edgefile = open("Edge_negative.txt",'r')
edgeread = edgefile.readlines()
j = 0
for i in range(1,149):
    diseaselist=[]
    for edge in edgeread:
        edgelist = edge.split()
        if(i == int(edgelist[0])):
            diseaselist.append(edgelist[1])

    if(j == 0):
        edgewrite = open("Mining_input_negative.txt", 'w')
        diseaselist = list(set(diseaselist))
        for spice in diseaselist:
            edgewrite.write(str(spice) + " ")
        edgewrite.write("\n")
        j += 1
    else:
        edgewrite = open("Mining_input_negative.txt", 'a')
        diseaselist = list(set(diseaselist))
        for spice in diseaselist:
            edgewrite.write(str(spice) + " ")
        edgewrite.write("\n")