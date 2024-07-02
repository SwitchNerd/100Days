import pandas

f = pandas.read_csv('Day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
PrimaryColor = f['Primary Fur Color']
countBlack = 0 
countCinnamon = 0
countGray = 0
for line in PrimaryColor:
    match line:
        case 'Gray':
            countGray += 1
        case 'Cinnamon':
            countCinnamon += 1
        case 'Black':
            countBlack += 1
            
print(countBlack,countCinnamon,countGray)
#Write it to another file
#squirrel_count.csv
#   Fur Color, Count
Data = {
    'Fur Color' : ['Gray','Cinnamon','Black'],
    'Count' : [countGray,countCinnamon,countBlack]
}

Data = pandas.DataFrame(Data)
Data.to_csv('Day25/squirrel_count.csv')
