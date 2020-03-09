# THIS SCRIPT WILL READ IN UK PASSENGER NUMBERS FROM THE CAA DATA SETS 2006-2018 AND PLOT
# THE GROWTH OR DECLINE FOR ANY ENTERED AIRPORT
import os
import pandas as pd
import glob
import matplotlib.pyplot as plt
import numpy as np

print('\nThis script will chart total passenger numbers at the desired UK airport from 2006 to 2018...\n')

path = os.path.join(input("Enter or paste location of directory with CAA data: \n"))
airport = input('Enter desired UK airport: ').upper()
years = [*range(2006, 2019, 1)]
totalPax = []
search_values = [airport]

# THIS READS EACH INDIVIDUAL CSV FILE IN THE SPECIFIED PATH AND JOINS THEM INTO ONE DATA FRAME
# !! IMPORTANT !! ALL COLUMNS MUST BE IDENTICAL
all_files = glob.glob(os.path.join(path, "*.csv"))
df_from_each_file = (pd.read_csv(f) for f in all_files)
df = pd.concat(df_from_each_file, ignore_index=True)

df2 = df[df.rpt_apt_name.str.match(airport)]  # THIS FUNCTION RETURNS ANY ROW IN THE DATA FRAME WITH MATCHING KEYWORD
for row in range(0, len(df2)):
    df3 = df2.iloc[row]['total_pax_fw_tp']
    totalPax.append(df3)

res1 = plt.plot(years, totalPax, color='#1C6EA4', linestyle='dashed', marker='o', markerfacecolor='r')

ax = plt.gca()
ax.xaxis.set_ticks(np.arange(2006, 2019, 1))
ax.set_xlabel('Years', labelpad=10, style='oblique', fontsize=12)
ax.set_ylabel('Passengers', labelpad=10, style='oblique', fontsize=12)
ax.set_title('Passenger Numbers for {} Airport, 2006-2018'.format(airport), pad=10, style='italic')
ax.tick_params(axis='both', which='major', labelsize=8)
# ax.set_ylim([0, 20000000]) # OPTION TO SET Y AXIS LIMITS

plt.xticks(rotation=70)
plt.ticklabel_format(style='plain')
plt.tick_params(axis='both', which='major', pad=10)
plt.tight_layout()
plt.show()
