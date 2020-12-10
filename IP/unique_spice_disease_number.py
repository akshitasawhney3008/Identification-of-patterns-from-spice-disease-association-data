my_file = open('l3-recommendation.tsv', 'r')
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
print("Unique spices: ", len(spices))
print("Unique diseases: ", len(diseases))
my_f = open('Edge.txt', 'r')
print("Unique associations: ", len(my_f.readlines()))

my_biclique_file = open('Maximal_Biclique_final_mod.txt', 'r')
count = 0
max1 = 0
max2 = 0
spice_ranking = []
my_lines = my_biclique_file.readlines()
for line in my_lines:
    if line.strip():
        count += 1
        temp_list = line.split(':')
        temp_list1 = []
        temp_list2 = []
        temp_list1 = temp_list[0].split(',')
        temp_list1 = list(set(temp_list1))
        temp_list2 = temp_list[1].split(',')
        temp_list2 = list(set(temp_list2))
        if len(temp_list1) > max1:
            max1 = len(temp_list1)
            my_list1 = temp_list2
            my_temp_list = temp_list1
        if len(temp_list2) > max2:
            max2 = len(temp_list2)
            my_list2 = temp_list1
            my_temp_list2 = temp_list2

print("Total Maximal_Bicliques: ", count)
print("Spices with max ranking: ", my_list2, "mapped with", max2, "diseases", "they are", my_temp_list2)
# print("Diseases with max ranking: ",my_list1 , "mapped with", max1 , "spices" "they are", my_templist )

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
my_dict = {}
for i in range (len(diseases)):
    flag = 0
    for key, value in my_dict.items():
        if diseases[i] == key:
            flag = 1
            value.append(spices[i])
    if flag == 0:
        temp_list3 = []
        temp_list3.append(spices[i])
        my_dict[diseases[i]] = temp_list3

j = 0
for k, v in my_dict.items():
    if j == 0:
        my_ranking_file = open('Disease_ranking.txt', 'w')
        my_ranking_file.write(str(k) + ': ' + str(len(v)) + ';' + str(v) + '\n')
        j += 1
    else:
        my_ranking_file = open('Disease_ranking.txt', 'a')
        my_ranking_file.write(str(k) + ': ' + str(len(v)) + ';' + str(v) + '\n')

my_dict = {}
for i in range (len(spices)):
    flag = 0
    for key, value in my_dict.items():
        if spices[i] == key:
            flag = 1
            value.append(diseases[i])
    if flag == 0:
        temp_list3 = []
        temp_list3.append(diseases[i])
        my_dict[spices[i]] = temp_list3

j = 0
for k, v in my_dict.items():
    if j == 0:
        my_ranking_file = open('Spice_associated_with_diseases.txt', 'w')
        my_ranking_file.write(str(k) + ': ' + str(len(v)) + ';' + str(v) + '\n')
        j += 1
    else:
        my_ranking_file = open('Spice_associated_with_diseases.txt', 'a')
        my_ranking_file.write(str(k) + ': ' + str(len(v)) + ';' + str(v) + '\n')
