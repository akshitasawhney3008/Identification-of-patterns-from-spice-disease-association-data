association_set_file = open('out_25_1.txt','r')
disease_file = open("Disease(149-610).txt", 'r')
association_set_read = association_set_file.readlines()
disease_file_read = disease_file.readlines()
associationset_list = []
for association_sets in association_set_read:
    string = ''
    association_set_list = association_sets.split('#')
    association_set = association_set_list[0].split("==>")
    for association in association_set[0].split(" "):
        if association != ' ':
            for disease in disease_file_read:
                disease_list = disease.split(" ",1)
                if association.rstrip(" ") == disease_list[0]:
                    string += disease_list[1].rstrip('\n')
                    string += ";"
    string = string.rstrip(";") + " ==> "
    for association in association_set[1].split(" "):
        if association != ' ':
            for disease in disease_file_read:
                disease_list = disease.split(" ",1)
                if association.rstrip(" ") == disease_list[0]:
                    string += disease_list[1].rstrip('\n')
                    string += ";"
    string = string.rstrip(";") + ", "+ association_set_list[1] + ", " + association_set_list[2]
    associationset_list.append(string)

write_associationsets = open("out(.25-1)demap.txt", 'w')
for associations in associationset_list:
    write_associationsets.write(associations)

