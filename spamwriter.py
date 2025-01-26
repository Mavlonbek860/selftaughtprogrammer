import csv

with open('mycsv.csv', 'w') as csvfile:
	spamwriter = csv.writer(csvfile, delimiter=',')
	spamwriter.writerow(['Familiya', 'Ism', 'Tugilgan Sana'])
	spamwriter.writerow(['Hudoyberdiyev', 'Mavlonbek', '1987'])
