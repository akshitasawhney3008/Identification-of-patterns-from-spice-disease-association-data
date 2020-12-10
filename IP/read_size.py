spice_count=[]
disease_count = []
biclique_count = []
my_file = open('size.out', 'r')
size_lines = my_file.readlines()
for line in size_lines:
    line.strip('\n')
    my_line = line.split(' ')
    spice_count.append(my_line[0])
    disease_count.append(my_line[1])
    biclique_count.append(int(my_line[0]) + int(my_line[1]))

# j=0
# for s in spice_count:
#     if j == 0:
#         my_spice_file = open('spice_count.txt', 'w')
#         my_spice_file.write(str(s) + '\n')
#         j = j+1
#     else:
#         my_spice_file = open('spice_count.txt', 'a')
#         my_spice_file.write(str(s) + '\n')
#
# j = 0
# for d in disease_count:
#     if j == 0:
#         my_disease_file = open('disease_count.txt', 'w')
#         my_disease_file.write(str(d))
#         j = j+1
#     else:
#         my_disease_file = open('disease_count.txt', 'a')
#         my_disease_file.write(str(d))

j = 0
for b in biclique_count:
    if j == 0:
        my_biclique_file = open('biclique_count.txt', 'w')
        my_biclique_file.write(str(b) + '\n')
        j = j+1
    else:
        my_biclique_file = open('biclique_count.txt', 'a')
        my_biclique_file.write(str(b) + '\n')