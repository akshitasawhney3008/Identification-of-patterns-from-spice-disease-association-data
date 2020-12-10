import itertools
import random
import math

iterations = 100

file_association_rules = open('out(.09-1).txt', 'r')
rule_lines = file_association_rules.readlines()

sd_dict = {}
file_spice_to_disease = open('Spice_disease.tsv', 'r')
sd_lines = file_spice_to_disease.readlines()
for sd_line in sd_lines:
    temp = sd_line.split('\t')
    if temp[1] in sd_dict:
        list_of_diseases = sd_dict.get(temp[1])
        list_of_diseases.append(temp[3].strip())
        list_of_diseases = list(set(list_of_diseases))
        sd_dict[temp[1]] = list_of_diseases
    else:
        list_of_diseases = []
        list_of_diseases.append(temp[3].strip())
        sd_dict[temp[1]] = list_of_diseases

i = 0
dp_dict = {}
dp_list = []
file_disease_to_phyto = open('Disease_to_phytochemical.tsv', 'r')
dp_lines = file_disease_to_phyto.readlines()
for dp_line in dp_lines:
    if i != 0:
        temp = dp_line.split('\t')
        if temp[4] in dp_dict:
            list_of_phyto = dp_dict.get(temp[4])
            list_of_phyto.append(temp[2].strip())
            dp_list.append(temp[2].strip())
            list_of_phyto = list(set(list_of_phyto))
            dp_dict[temp[4]] = list_of_phyto
        else:
            list_of_phyto = []
            list_of_phyto.append(temp[2].strip())
            dp_list.append(temp[2].strip())
            dp_dict[temp[4]] = list_of_phyto
    i += 1
dp_list = list(set(dp_list))

j = 0
sp_dict = {}
file_spice_to_phyto = open('Spice_to_phytochemical.tsv', 'r')
sp_lines = file_spice_to_phyto.readlines()
for sp_line in sp_lines:
    if j != 0:
        temp = sp_line.split('\t')
        if temp[0] in sp_dict:
            list_of_phyto = sp_dict.get(temp[0])
            list_of_phyto.append(temp[1].strip())
            list_of_phyto = list(set(list_of_phyto))
            sp_dict[temp[0]] = list_of_phyto
        else:
            list_of_phyto = []
            list_of_phyto.append(temp[1].strip())
            sp_dict[temp[0]] = list_of_phyto
    j += 1

def get_phtochemical_count_after_mapping_to_spices(spices, phyto_list):
    list_to_be_returned = []
    for phyto in phyto_list:
        flag = 0
        for spice in spices:
            if spice in sp_dict:
                p_list = sp_dict.get(spice)
                if phyto not in p_list:
                    flag = 1
                    break
            else:
                flag = 1
                break
        if flag == 0:
            list_to_be_returned.append(phyto)
    return list_to_be_returned

#def get_phtochemical_count_after_mapping_to_spices(spices, phyto_list):
#    list_to_be_returned = []
#    for phyto in phyto_list:
#        for spice in spices:
#            if spice in sp_dict:
#                p_list = sp_dict.get(spice)
#                if phyto in p_list:
#                    list_to_be_returned.append(phyto)
#            else:
#                break
#    return list_to_be_returned

count = 0
zscore_list = []
for line in rule_lines:
    temp_list = line.split(' ==> ')
    temp_list_lhs = temp_list[0].split(';')
    temp_list_rhs = temp_list[1].split(', SUP')[0].split(';')
    spices = temp_list_lhs + temp_list_rhs

    all_diseases = []
    phytochemicals_from_diseases = []

    for spice in spices:
        all_diseases.append(sd_dict.get(spice))
    all_diseases = list(set(list(itertools.chain.from_iterable(all_diseases))))
    for disease in all_diseases:
        if disease in dp_dict:
            extracted_phytochemical_list = dp_dict[disease]
            for pc in extracted_phytochemical_list:
                phytochemicals_from_diseases.append(pc)
    phytochemicals_from_diseases = list(set(phytochemicals_from_diseases))

    # ZScore calculation
    mapped_phyto = get_phtochemical_count_after_mapping_to_spices(spices, phytochemicals_from_diseases)
    biological_count = len(mapped_phyto)
    number_of_random_samples = len(phytochemicals_from_diseases)

    rand_list = []
    for k in range(0, iterations):
        phytochemicals_from_random_pick = []
        while len(phytochemicals_from_random_pick) != number_of_random_samples:
            phytochemicals_from_random_pick.append(random.choice(dp_list))
            phytochemicals_from_random_pick = list(set(phytochemicals_from_random_pick))
        mapped_random_phyto = get_phtochemical_count_after_mapping_to_spices(spices, phytochemicals_from_random_pick)
        rand_list.append(len(mapped_random_phyto))
    list_sum = 0
    for elt in rand_list:
        list_sum += int(elt)
    mean = list_sum*1.0/iterations

    numerator = 0
    for elt in rand_list:
        numerator += (elt-mean)*(elt-mean)
    denominator = iterations-1
    std = math.sqrt(numerator*1.0/denominator)
    if std != 0:
        zscore = ((biological_count - mean)*1.0)/std
    else:
        zscore = 0
    zscore_list.append(zscore)
    count += 1
    print(str(count) + ' ' + str(zscore))


output_file = open('Zscore.txt', 'w')
for zs in zscore_list:
    output_file.write(str(zs) + '\n')
print('Done')