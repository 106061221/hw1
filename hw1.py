# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '106061221.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
target_data = list(filter(lambda item: \
item['PRES'] != '-99.000' \
and item['PRES'] != '-999.000' \
, data))
#target_data = list(filter(lambda item: item['station_id'] == 'C0G640', target_data))
target_data = list(filter(lambda item: \
item['station_id']=='C0A880' \
or item['station_id']=='C0F9A0' \
or item['station_id']=='C0G640' \
or item['station_id']=='C0R190' \
or item['station_id']=='C0X260' \
, target_data))
sum=[0,0,0,0,0]
count=[0,0,0,0,0]
for item in (target_data):
   if item['station_id']=='C0A880':
      sum[0]=sum[0]+float(item['PRES'])
      count[0]+=1
   if item['station_id']=='C0F9A0':
      sum[1]=sum[1]+float(item['PRES'])
      count[1]+=1
   if item['station_id']=='C0G640':
      sum[2]=sum[2]+float(item['PRES'])
      count[2]+=1
   if item['station_id']=='C0R190':
      sum[3]=sum[3]+float(item['PRES'])
      count[3]+=1
   if item['station_id']=='C0X260':
      sum[4]=sum[4]+float(item['PRES'])
      count[4]+=1
print("[['C0A880', ",end='')
if count[0]==0:
   print("'None'",end='')
else:
   ans=sum[0]/count[0]
   print(ans,end='')

print("], ['C0F9A0', ",end='')
if count[1]==0:
   print("'None'",end='')
else:
   ans=sum[1]/count[1]
   print(ans,end='')

print("], ['C0G640', ",end='')
if count[2]==0:
   print("'None'",end='')
else:
   ans=sum[2]/count[2]
   print(ans,end='')

print("], ['C0R190', ",end='')
if count[3]==0:
   print("'None'",end='')
else:
   ans=sum[3]/count[3]
   print(ans,end='')

print("], ['C0X260', ",end='')
if count[4]==0:
   print("'None'",end='')
else:
   ans=sum[4]/count[4]
   print(ans,end='')
print("]]")
# Retrive ten data points from the beginning.
#target_data = data[:10]
#=======================================

# Part. 4
#=======================================
# Print result

#========================================