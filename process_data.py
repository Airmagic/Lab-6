# this is to be used to work with the csv file
import csv


mammoth_data = []

# opening the file so it can be read
with open('pbdb_data.csv', 'r') as csvfile:
    
#     reading the file
    reader = csv.reader(csvfile)

#     reading the columns in the document
    columns = reader.__next__()
    
#     this is to pull the data out of the document
    for row in reader:

        name = row[9]
        abd = row[22]
        abd_unit = row[23]
        lat = float(row[25])
        lng = float(row[24])
        state = row[27]
        county = row[28]
        comment = row[32]
        
#         binding the data that was pulled out
        mammoth_data.append([name, abd, abd_unit, lat, lng, state, county, comment])

# making a document or overwriting document to write the data that we have collected
with open('mammoth_data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(['name','abd', 'abd_unit', 'lat','lng','state','county','comment'])
    writer.writerows(mammoth_data)
