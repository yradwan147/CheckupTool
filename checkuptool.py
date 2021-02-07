import re, os, openpyxl, pprint
names = []
names_d = []
pubTitles = []
path1 = "C:\\Users\\Yousef Radwan\\Desktop\\pub\\All\\"
path2 = "C:\\Users\\Yousef Radwan\\Desktop\\pub\\Need checks\\"

entry = re.compile(r'''[A-Za-z-,.0-9’ ()'‐]+\s\s?''')
E = input("Enter Publications: ")
E.split("  ")
print(E)

#test = re.findall(entry, E)
#print(test)
#for groups in entry.findall(E):
#    pubName = groups[:-2]
#    names.append(pubName)

###for z in names: print (z)
###print('Opening workbook...')
###wb = openpyxl.load_workbook('scopus-all-NU-june-21018.xlsx')
##sheet = wb.get_sheet_by_name('scopus')
##row_count = sheet.max_row
##print('Reading rows...')
##for row in range(2, row_count + 1):
##    title = sheet['B' + str(row)].value
##    pubTitles.append(title)
##    
##for publication in names:
##    if publication in pubTitles:
##        print(publication)
##        print("Found and skipped")
##    else:
##        os.rename(path1 + publication + ".pdf" , path2 + publication + ".pdf")
##        print(publication)
##        print ("UnFound and Moved")
