import numpy as np
import matplotlib.pyplot as plt
 
# data to plot
n_groups = 8


rows = []  # number of rows in the file
with open('input.csv') as file:
    rows=file.readlines();


transformed_data=[]  # is the List of List
for singlerow in rows:
    columns=singlerow.split(",") #  I have taken the rows as a string and then splitting them
    transformed_singlerow=[] #storing each element to finalList
    for column in columns:
        if '\n' in column:
            column=column.rstrip('\n') # stripping the \n component

        transformed_singlerow.append(float(column))
    transformed_data.append(transformed_singlerow)

print(transformed_data)


innerArrayLength=0
for item in transformed_data:
    innerArrayLength=len(item)
    break

columnar_trans_data=[]
for single_col_index in range(innerArrayLength):
    single_cloumn=[]
    for row in transformed_data:
        single_cloumn.append(row[single_col_index ])
    columnar_trans_data.append(single_cloumn)

print(columnar_trans_data)


hotel_112154=()
hotel_224224=()
hotel_150854=()
hotel_232962=()
hotel_584407=()


for i in range(len(columnar_trans_data)):
    if(i==0):
        hotel_112154=hotel_112154+tuple(columnar_trans_data[i])
    if(i==1):
        hotel_224224=hotel_224224+tuple(columnar_trans_data[i])
    if(i==2):
        hotel_150854=hotel_150854+tuple(columnar_trans_data[i])
    if(i==3):
       hotel_232962=hotel_232962+tuple(columnar_trans_data[i])
    if(i==4):
       hotel_584407=hotel_584407+tuple(columnar_trans_data[i])


# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.1
opacity = 0.6


rects0 = plt.bar(index-(2*bar_width), hotel_112154, bar_width,
                 alpha=opacity,
                 color='b',
                 label='hotel_112154')

rects1 = plt.bar(index - bar_width, hotel_224224, bar_width,
                 alpha=opacity,
                 color='g',
                 label='hotel_224224')

rects2 = plt.bar(index, hotel_150854, bar_width,
                 alpha=opacity,
                 color='r',
                 label='hotel_150854')

rects3 = plt.bar(index + bar_width, hotel_232962, bar_width,
                 alpha=opacity,
                 color='yellow',
                 label='hotel_232962')
rects4 = plt.bar(index+(2*bar_width), hotel_584407, bar_width,
                 alpha=opacity,
                 color='black',
                 label='hotel_584407')


plt.xlabel('Features')
plt.ylabel('Ratings Value-Out of 5')
plt.title('Comparison of Hotels with respect to all the features including sentiments')
plt.xticks(index + bar_width, ('Sentiment', 'Value', 'Rooms', 'Location', 'Cleanliness','Check In / FrontDesk','Service','Business Service'))
plt.legend()

plt.tight_layout()
plt.show()
