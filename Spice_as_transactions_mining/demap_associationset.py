association_set_file = open('mining_out.txt','r')
spice_file = open("Spice(463-610).txt", 'r')
association_set_read = association_set_file.readlines()
spice_file_read = spice_file.readlines()
associationset_list = []
for association_sets in association_set_read:
    string = ''
    association_set_list = association_sets.split('#')
    association_set = association_set_list[0].split("==>")
    for association in association_set[0].split(" "):
        if association:
            for spice in spice_file_read:
                spice_list = spice.split(" ", 1)
                if association.rstrip(" ") == spice_list[0]:
                    string += spice_list[1].rstrip('\n')
                    string += ";"
                    break
    string = string.rstrip(";") + " ==> "
    for association in association_set[1].split(" "):
        if association:
            for spice in spice_file_read:
                spice_list = spice.split(" ", 1)
                if association.rstrip(" ") == spice_list[0]:
                    string += spice_list[1].rstrip('\n')
                    string += ";"
                    break
    string = string.rstrip(";") + ", "+ association_set_list[1] + ", " + association_set_list[2]
    associationset_list.append(string)

write_associationsets = open("out(.09-1).txt", 'w')
for associations in associationset_list:
    write_associationsets.write(associations)

