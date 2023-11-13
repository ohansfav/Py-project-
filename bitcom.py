
import random as R
from collections import Counter

#for monday, the given colours ArithmeticError    
monday = ['GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE',
         'PINK', 'BLUE', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE',
        'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN']

tuesday = ['ARSH', 'BROWN', 'GREEN', 'BROWN', 'BLUE', 
            'BLUE', 'BLEW', 'PINK', 'PINK', 'ORANGE', 'ORANGE', 
            'RED', 'WHITE', 'BLUE', 'WHITE', 'WHITE', 'BLUE', 'BLUE', 'BLUE']

wednesday = ['GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 
             'RED', 'YELLOW', 'ORANGE', 'RED', 'ORANGE', 'RED', 
             'BLUE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'WHITE', 'WHITE']

thursday = ['BLUE', 'BLUE', 'GREEN', 'WHITE', 'BLUE', 'BROWN', 'PINK', 
            'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE', 
            'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN']
friday = ['GREEN', 'WHITE', 'GREEN', 'BROWN', 'BLUE', 'BLUE', 'BLACK', 
          'WHITE', 'ORANGE', 'RED', 'RED', 'RED', 'WHITE', 'BLUE', 
          'WHITE', 'BLUE', 'BLUE', 'BLUE', 'WHITE']




combine_days = monday + tuesday + wednesday + thursday + friday

#For probability
combine_days = monday + tuesday + wednesday + thursday + friday
color_counts = Counter(combine_days)
total_count = len(combine_days)
color_probability = {color: count / total_count for color, count in color_counts.items()}

#for color probaliltiy 
print("color probability: ")
for color, probability in color_probability.items():
    print(f"{color}: {probability}")
    
# ///////////////////////////

mean_color = max(set(combine_days), key=combine_days.count)
print('\nThe mean color is\n', mean_color)

Counter = Counter(combine_days)
most_common = Counter.most_common(9)

print('\nmost color worn throughtout the week is\n', most_common[0])

print('\nAll colors and number of times they appear\n', most_common)





