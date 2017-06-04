import matplotlib.pyplot as plt
import numpy as np

objects=('room',	'staff'	,'location'	,'service',	'breakfast'	,'clean'	,'walk',	'place'	,'bed',	'help')
y_pos=np.arange(len(objects))
frequency=[14820,5301,4639,3859,3123,3041,2958,2857,2834,2678]
plt.bar(y_pos,frequency,align='center',alpha=0.5)
plt.xticks(y_pos,objects)
plt.ylabel("frequency of words")
plt.xlabel("words")
plt.title("Importance of words in decreasing order using sentiment analysis")

plt.show()
