my_file = open('most-associations-each-level-negative.tsv','r')
lines = my_file.readlines()

spices = []
diseases = []
tree_num = []
count = []
for line in lines:
    temp_list = line.split('\t')
    #if temp_list[1].count(".") == 0 or temp_list[1].count(".") == 1 or temp_list[1].count(".") == 2:
    if temp_list[1].count(".") == 2:
        tree_num.append(temp_list[1])
        spices.append(temp_list[2])
        diseases.append(temp_list[4])
        count.append(temp_list[3])

tree_num.pop(0)
spices.pop(0)
diseases.pop(0)
count.pop(0)

my_out_file = open('third-level-asssociations-negative.tsv','w')
for i in range(len(tree_num)):
    my_out_file.write(str(tree_num[i]) + "\t" + str(spices[i]) + "\t" + str(count[i]) + "\t" + str(diseases[i]) + "\n")

my_out_file.close()