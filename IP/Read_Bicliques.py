import xlsxwriter

workbook = xlsxwriter.Workbook('Maximal_Bicliques_Withcountofdiseases.xlsx')
worksheet = workbook.add_worksheet()
row = 0
column = 0
row1 = 0
bicliques_file = open('Maximal_Biclique_l3.txt', 'r')
lines = bicliques_file.readlines()
for line in lines:
    if line.strip():
        temp_list = line.split(':')
        temp_list1 = []
        temp_list2 = []
        # print(temp_list[0])
        temp_list1 = temp_list[0].split(',')
        temp_list1 = list(set(temp_list1))
        # print(temp_list[1])
        temp_list2 = temp_list[1].split(',')
        temp_list2 = list(set(temp_list2))
        length2 = len(temp_list2)
        row = row1
        for spices in temp_list1:
            worksheet.write(row, column, spices)
            row += 1
        for diseases in temp_list2:
            worksheet.write(row1, column+1, diseases)
            worksheet.write(row1, column + 2, length2)
            row1 += 1
        worksheet.write(row1, column + 2, length2)
        row1 += 1
        worksheet.write(row1, column + 2, length2)
        row1 += 1
workbook.close()

# for line in lines:
#     if line.strip():
#         temp_list = line.split(':')
#         temp_list1 = []
#         temp_list2 = []
#         # print(temp_list[0])
#         temp_list1 = temp_list[0].split(',')
#         # print(temp_list[1])
#         temp_list2 = temp_list[1].split(',')
#
#         for ele in temp_list1:
#             for