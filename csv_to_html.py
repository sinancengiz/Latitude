from prettytable import prettytable

csv_file = open("cities.csv","r")
csv_file = csv_file.readlines()
line1 = csv_file[0]
line1 = line1.split(",")
line2 = csv_file[1]
line2 = line2.split(",")

x = prettytable([line1[0],line2[0]])

html_code = x.get_html_string()
html_file = open("table.html","w")
html_file = html_file.write(html_code)

print(line1)