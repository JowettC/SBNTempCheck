import json
import csv



class Person:
  def __init__(self, name, unit):
    self.name = name
    self.unit = unit
    self.submitted = 0
    self.missed = ""
    self.status = " "

# always change this 


people = []
dataSet = json.load(open('data.json'))
# print(data[0]["name"])
allDates=[]
for data in dataSet:
    if data.get('month') <10:
        if data.get('date') < 10:
            date = "0" + str(data.get('date'))+"0"+str(data.get('month'))+str(data.get('year'))[2:]+"-"+data.get('session')
        else: 
            date = str(data.get('date'))+"0"+str(data.get('month'))+str(data.get('year'))[2:]+"-"+data.get('session') 
    else:
        if data.get('date') < 10:
            date = "0" +str(data.get('date'))+str(data.get('month'))+str(data.get('year'))[2:]+"-"+data.get('session')
        else:
            date = str(data.get('date'))+str(data.get('month'))+str(data.get('year'))[2:]+"-"+data.get('session')

    if (date not in allDates):
        allDates.append(date)
totalsubmitted = len(allDates) 
with open('NR.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    names = ''
    add =''
    count = 0
    # adding units
    for row in csv_reader:
        for i in range(len(row)):
            if i > 1:
                people.append(Person(row[i],row[1]))
                
# inserting status
with open('DB.csv') as csv_file:
    csv_reader2 = csv.reader(csv_file, delimiter=',')
    for row in csv_reader2:
        for person in people:
            if person.name.strip() == row[0].strip():
                person.status = row[1].strip()

for indiv in people:
    allDates_cp =[]
    text =""
    for date in allDates:
        allDates_cp.append(date)
    for data in dataSet:
        if data.get('name').strip() == indiv.name.strip():
            indiv.submitted += 1
            if data.get('month') <10:
                if data.get('date') < 10:
                    date = "0" + str(data.get('date'))+"0"+str(data.get('month'))+str(data.get('year'))[2:]+"-"+data.get('session')
                else: 
                    date = str(data.get('date'))+"0"+str(data.get('month'))+str(data.get('year'))[2:]+"-"+data.get('session') 
            else:
                if data.get('date') < 10:
                    date = "0" +str(data.get('date'))+str(data.get('month'))+str(data.get('year'))[2:]+"-"+data.get('session')
                else:
                    date = str(data.get('date'))+str(data.get('month'))+str(data.get('year'))[2:]+"-"+data.get('session')

            if date in allDates_cp:
                allDates_cp.remove(date)
    for date in allDates_cp:
        text += date +", "
    indiv.missed = text
fields = ["Section","Name","status","Number of Missed Entries","Dates of Missed Entries"]
rows = []
filename = "TemptTakingMisses.csv"
print ("done")
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    for person in people:
        row = []
        row.append(person.unit)
        row.append(person.name)
        row.append(person.status)
        row.append(len(allDates) - person.submitted)
        row.append(person.missed)
        rows.append(row)
    csvwriter.writerows(rows)
