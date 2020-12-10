import xlsxwriter
class Spice:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Disease:
    def __init__(self, id, name):
        self.id = id
        self.name = name

my_file = open('l3-recommendation.tsv','r')
lines = my_file.readlines()

spices = []
diseases = []
for line in lines:
    temp_list = line.split('\t')
    spices.append(temp_list[2])
    diseases.append(temp_list[4])

spices.pop(0)
diseases.pop(0)
spices = list(set(spices))
diseases = list(set(diseases))

spice_mapped_list = []
i = 0
for s in spices:
    spice = Spice(i, s)
    spice_mapped_list.append(spice)
    i += 1

disease_mapped_list = []
i = len(spices)
for d in diseases:
    disease = Disease(i, d)
    disease_mapped_list.append(disease)
    i += 1

j = 0
for s in spice_mapped_list:
    if j == 0:
        my_spice_file = open('Spice.txt', 'w')
        my_spice_file.write(str(s.id) + ' ' + s.name + '\n')
        j += 1
    else:
        my_spice_file = open('Spice.txt', 'a')
        my_spice_file.write(str(s.id) + ' ' + s.name + '\n')
j = 0
for d in disease_mapped_list:
    if j == 0:
        my_spice_file = open('Disease.txt', 'w')
        my_spice_file.write(str(d.id) + ' ' + d.name + '\n')
        j += 1
    else:
        my_spice_file = open('Disease.txt', 'a')
        my_spice_file.write(str(d.id) + ' ' + d.name + '\n')

edge = []
for line in lines:
    temp_list = line.split('\t')
    spice_name = temp_list[2]
    disease_name = temp_list[4]
    if spice_name == 'Spice' and disease_name == 'Disease':
        continue
    for s in spice_mapped_list:
        if s.name == spice_name:
            spice_id = s.id
    for d in disease_mapped_list:
        if d.name == disease_name:
            disease_id = d.id
    el = []
    el.append(spice_id)
    el.append(disease_id)
    edge.append(el)

j = 0
for e in edge:
    if j == 0:
        my_edge_file = open('Edge.txt', 'w')
        my_edge_file.write(str(e[0]) + ' ' + str(e[1]) + '\n')
        j += 1
    else:
        my_edge_file = open('Edge.txt', 'a')
        my_edge_file.write(str(e[0]) + ' ' + str(e[1]) + '\n')

input_list = []

mf = open('Edge.txt', 'r')
lines = mf.readlines()
for line in lines:
    temp_list = line.split()
    new_list = []
    new_list.append(int(temp_list[0]))
    new_list.append(int(temp_list[1]))
    input_list.append(new_list)

class Graph:
    def __init__(self,source, sink):
        self.source = source
        self.sink = sink

def maximum(my_ob, max_el):
    if my_ob.source > max_el:
        max_el = my_graph_ob.source
    if my_ob.sink > max_el:
        max_el = my_graph_ob.sink
    return max_el


def union(list_one , list_two):
    list_new = []
    for elt in list_one:
        list_new.append(elt)
    for elt in list_two:
        list_new.append(elt)
    return list(set(list_new))


def intersection(list_one, list_two):
    temp_list = []
    for elt_1 in list_one:
        for elt_2 in list_two:
            if elt_1 == elt_2:
                temp_list.append(elt_1)
    return temp_list


def check_absorb(star_list, my_set_list):
    d_list = []
    X1 = my_set_list[0]
    Y1 = my_set_list[1]
    for str in star_list:
        X2 = str[0]
        Y2 = str[1]
        my_intersection_list1 = intersection(X1, X2)
        my_intersection_list2 = intersection(Y1, Y2)
        my_intersection_list3 = intersection(X1, Y2)
        my_intersection_list4 = intersection(X2, Y1)

        if set(my_intersection_list1) == set(X1) and set(my_intersection_list2) == set(Y1) and len(my_intersection_list1) != 0 and len(my_intersection_list2) != 0:
            return 1, d_list
        elif set(my_intersection_list3) == set(X1) and set(my_intersection_list4) == set(Y1) and len(my_intersection_list3) != 0 and len(my_intersection_list4) != 0:
            return 1, d_list
        elif set(my_intersection_list1) == set(X2) and set(my_intersection_list2) == set(Y2) and len(my_intersection_list1) != 0 and len(my_intersection_list2) != 0:
            d_list.append(str)
        elif set(my_intersection_list3) == set(Y2) and set(my_intersection_list4) == set(X2) and len(my_intersection_list3) != 0 and len(my_intersection_list4) != 0:
            d_list.append(str)
    return 0, d_list

def remove_dup(temp_list):
    t_list=[]
    for i in range(len(temp_list)):
        l1 = temp_list[i]
        for j in range(i+1 , len(temp_list)):
            l2 = temp_list[j]
            if set(l1[0]) == set(l2[0]) and set(l1[1]) == set(l2[1]):
                if l2 not in t_list:
                    t_list.append(l2)
            elif set(l1[0]) == set(l2[1]) and set(l1[1]) == set(l2[0]):
                inv_list = []
                inv_list.append(l2[1])
                inv_list.append(l2[0])
                if inv_list in t_list:
                    t_list.append(l2)
    for t in t_list:
        if t in temp_list:
            temp_list.remove(t)
    return temp_list

def consensus(X1, X2, Y1, Y2):
    intersection_list3 = intersection(X1, Y2)
    intersection_list4 = intersection(X2, Y1)
    intersection_list1 = intersection(Y1, Y2)
    intersection_list2 = intersection(X1, X2)
    temp_set_list = []
    if (len(intersection_list1) != 0):
        union_list1 = union(X1, X2)
        set_list1 = []
        set_list1.append(union_list1)
        set_list1.append(intersection_list1)
        temp_set_list.append(set_list1)

    if (len(intersection_list2) != 0):
        union_list2 = union(Y1, Y2)
        set_list2 = []
        set_list2.append(intersection_list2)
        set_list2.append(union_list2)
        temp_set_list.append(set_list2)

    if (len(intersection_list3) != 0):
        union_list3 = union(X2, Y1)
        set_list3 = []
        set_list3.append(intersection_list3)
        set_list3.append(union_list3)
        temp_set_list.append(set_list3)

    if (len(intersection_list4) != 0):
        union_list4 = union(X1, Y2)
        set_list4 = []
        set_list4.append(union_list4)
        set_list4.append(intersection_list4)
        temp_set_list.append(set_list4)
    return temp_set_list

def check_absorb_inverse(t, star_list):
    deletion_list = []
    X2 = t[0]
    Y2 = t[1]
    for star in star_list:
        X1 = star[0]
        Y1 = star[1]
        my_intersection_list1 = intersection(X1, X2)
        my_intersection_list2 = intersection(Y1, Y2)
        my_intersection_list3 = intersection(X1, Y2)
        my_intersection_list4 = intersection(X2, Y1)
        if set(my_intersection_list1) == set(X1) and set(my_intersection_list2) == set(Y1) and len(my_intersection_list1) != 0 and len(my_intersection_list2) != 0:
            deletion_list.append(star)
        elif set(my_intersection_list3) == set(X1) and set(my_intersection_list4) == set(Y1) and len(my_intersection_list3) != 0 and len(my_intersection_list4) != 0:
            deletion_list.append(star)
    return deletion_list

print ('Getting star list')

my_graph_list =[]
for i in input_list:
    my_graph_ob = Graph(i[0],i[1])
    my_graph_list.append(my_graph_ob)

max_ele = 1
for ob in my_graph_list:
    max_ele = maximum(ob, max_ele)


star_list = []
for i in range(1,max_ele+1):
    set_list = []
    first_el_list = []
    second_el_list = []
    for in_el in my_graph_list:
        if i == in_el.source:
            second_el_list.append(in_el.sink)
        elif i == in_el.sink:
            second_el_list.append(in_el.source)
    first_el_list.append(i)
    set_list.append(first_el_list)
    set_list.append(second_el_list)
    star_list.append(set_list)

print(star_list)

print ('Maximizing bicliques')

del_list=[]
t_list=[]
for i in range (0, len(star_list)):
    X1 = star_list[i][0]
    Y1 = star_list[i][1]
    for j in range(i+1, len(star_list)):
        temp_star_list = []
        X2 = star_list[j][0]
        Y2 = star_list[j][1]
        set_list_final = consensus(X1, X2, Y1, Y2)
        for s in set_list_final:
            f, d_list = check_absorb(star_list, s)
            for d in d_list:
                del_list.append(d)
            if f == 0:
                new_X1 = s[0]
                new_X2 = s[1]
                for strel in star_list:
                    new_Y1 = strel[0]
                    new_Y2 = strel[1]
                    temp_set_list = consensus(new_X1, new_X2, new_Y1, new_Y2)
                    for t in temp_set_list:
                        f, d1_list = check_absorb(star_list, t)
                        for d in d1_list:
                            del_list.append(d)
                        if f == 0:
                            d_list = check_absorb_inverse(t, star_list)
                            for d in d_list:
                                del_list.append(d)
                            t_list.append(t)
for d in del_list:
    if d in star_list:
        star_list.remove(d)
for t in t_list:
    star_list.append(t)
star_list = remove_dup(star_list)

print ('Demapping')

spices = []

my_spice_file = open('Spice.txt', 'r')
spice_lines = my_spice_file.readlines()
for line in spice_lines:
    temp_list = line.split(' ', 1)
    spice_id_name = []
    spice_id_name.append(temp_list[0])
    spice_id_name.append(temp_list[1])
    spices.append(spice_id_name)

diseases = []
my_disease_file = open('Disease.txt', 'r')
disease_lines = my_disease_file.readlines()
for line in disease_lines:
    temp_list = line.split(' ', 1)
    disease_id_name = []
    disease_id_name.append(temp_list[0])
    disease_id_name.append(temp_list[1])
    diseases.append(disease_id_name)

demapped_list = []
for star in star_list:
    spice_name = []
    disease_name = []
    biclique = []
    for s in star[0]:
        for spice in spices:
            if str(s) == spice[0]:
                spice_name.append(spice[1])
    biclique.append(spice_name)

    for s in star[1]:
        for disease in diseases:
            if str(s) == disease[0]:
                disease_name.append(disease[1])
    biclique.append(disease_name)
    demapped_list.append(biclique)

# i = 0
# for demap in demapped_list:
#     for spice in demap[0]:
#         if i == 0:
#             my_spice_file = open('Maximal_Biclique.txt', 'w')
#             if i == len(spices) - 1:
#                 my_spice_file.write(spice + '-')
#             else:
#                 my_spice_file.write(spice + ',')
#         else:
#             my_spice_file = open('Maximal_Biclique.txt', 'a')
#             if i == len(spices) - 1:
#                 my_spice_file.write(spice + '-')
#             else:
#                 my_spice_file.write(spice + ',')
#         i += 1
#     for diseases in demap[1]:
#         j = 0
#         for disease in diseases:
#             if j == len(diseases)-1:
#                 my_spice_file = open('Maximal_Biclique.txt', 'a')
#                 my_spice_file.write(disease)
#             else:
#                 my_spice_file = open('Maximal_Biclique.txt', 'a')
#                 my_spice_file.write(disease + ',')
#             j += 1
#     my_spice_file = open('Maximal_Biclique.txt', 'a')
#     my_spice_file.write('\n')
k = 0
for demap in demapped_list:
    i = 0
    for spice in demap[0]:
        if k == 0:
            my_spice_file = open('Maximal_Biclique.txt', 'w')
            if i == len(demap[0]) - 1:
                my_spice_file.write(spice + ':')
            else:
                my_spice_file.write(spice + ',')
        else:
            my_spice_file = open('Maximal_Biclique.txt', 'a')
            if i == len(demap[0]) - 1:
                my_spice_file.write(spice + ':')
            else:
                my_spice_file.write(spice + ',')
        i += 1
        k += 1
    j = 0
    for disease in demap[1]:
        if j == len(demap[1])-1:
            my_spice_file = open('Maximal_Biclique.txt', 'a')
            my_spice_file.write(disease)
        else:
            my_spice_file = open('Maximal_Biclique.txt', 'a')
            my_spice_file.write(disease + ',')
        j += 1
    my_spice_file = open('Maximal_Biclique.txt', 'a')
    my_spice_file.write('\n')


workbook = xlsxwriter.Workbook('Maximal_Bicliques.xlsx')
worksheet = workbook.add_worksheet()
row = 0
column = 0
row1 = 0
bicliques_file = open('Maximal_Biclique _final.txt', 'r')
lines = bicliques_file.readlines()
for line in lines:
    if line.strip():
        temp_list = line.split(':')
        temp_list1 = []
        temp_list2 = []
        # print(temp_list[0])
        temp_list1 = temp_list[0].split(',')
        # print(temp_list[1])
        temp_list2 = temp_list[1].split(',')
        length = len(temp_list2)
        row = row1
        for spices in temp_list1:
            worksheet.write(row, column, spices)
            row += 1
        for diseases in temp_list2:
            worksheet.write(row1, column+1, diseases)
            worksheet.write(row1, column+2, length)
            row1 += 1

        row1 += 2
workbook.close()
print('Done')


