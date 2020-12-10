class Spice:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Disease:
    def __init__(self, id, name):
        self.id = id
        self.name = name


my_file = open('level-3-asssociations.tsv','r')
lines = my_file.readlines()

spices = []
diseases = []
for line in lines:
    temp_list = line.split('\t')
    spices.append(temp_list[1])
    diseases.append(temp_list[3])

# spices.pop(0)
# diseases.pop(0)
spices = list(set(spices))
diseases = list(set(diseases))



spice_mapped_list = []
i = 1
for s in spices:
    spice = Spice(i, s)
    spice_mapped_list.append(spice)
    i += 1


disease_mapped_list = []
i = len(spices) + 1
for d in diseases:
    disease = Disease(i, d)
    disease_mapped_list.append(disease)
    i += 1

j = 0
for s in spice_mapped_list:
    if j == 0:
        my_spice_file = open('Spice(1-148).txt', 'w')
        my_spice_file.write(str(s.id) + ' ' + s.name + '\n')
        j += 1
    else:
        my_spice_file = open('Spice(1-148).txt', 'a')
        my_spice_file.write(str(s.id) + ' ' + s.name + '\n')
j = 0
for d in disease_mapped_list:
    if j == 0:
        my_spice_file = open('Disease(149-610).txt', 'w')
        my_spice_file.write(str(d.id) + ' ' + d.name + '\n')
        j += 1
    else:
        my_spice_file = open('Disease(149-610).txt', 'a')
        my_spice_file.write(str(d.id) + ' ' + d.name + '\n')

edge = []
for line in lines:
    temp_list = line.split('\t')
    spice_name = temp_list[1]
    disease_name = temp_list[3]
    if spice_name == 'Spice' and disease_name == 'Disease':
        continue
    for s in spice_mapped_list:
        if s.name == spice_name:
            spice_id = s.id
            break
    for d in disease_mapped_list:
        if d.name == disease_name:
            disease_id = d.id
            break
    el = []
    el.append(spice_id)
    el.append(disease_id)
    edge.append(el)

j = 0
for e in edge:
    if j == 0:
        my_edge_file = open('Edge(spice 1-148).txt', 'w')
        my_edge_file.write(str(e[0]) + ' ' + str(e[1]) + '\n')
        j += 1
    else:
        my_edge_file = open('Edge(spice 1-148).txt', 'a')
        my_edge_file.write(str(e[0]) + ' ' + str(e[1]) + '\n')

