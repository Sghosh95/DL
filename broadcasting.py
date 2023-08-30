"""calculate calories percentage in 4 fruits define in columns : see the matrix"""
import numpy as np

fruit_calories=np.array([[56,0,4.4,68],
                         [1.2,104.0,52.0,8.0],
                         [1.9,135,99.0,0.9]])
#calories in four furits:
#         apple mango guava papaya
# chydrate
# protein
# vitamin

print(fruit_calories)
print(fruit_calories.shape)

total_cal=fruit_calories.sum(axis=0)
print(total_cal)

#percent of calories
cal_percent= 100*fruit_calories/total_cal.reshape(1,4)
print(cal_percent)
