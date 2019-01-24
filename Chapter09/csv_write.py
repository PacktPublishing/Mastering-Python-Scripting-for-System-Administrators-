import csv

write_csv = [['Name', 'Sport'], ['Andres Iniesta', 'Football'], ['AB de Villiers', 'Cricket'], ['Virat Kohli', 'Cricket'], ['Lionel Messi', 'Football']]

with open('csv_write.csv', 'w') as csvFile:
writer = csv.writer(csvFile)
    	writer.writerows(write_csv)
	print(write_csv)

