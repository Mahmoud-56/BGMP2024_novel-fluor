#!/usr/bin/env python


import pandas as pd
import os 




blue_csv_files = csv_files = [
            '/projects/bgmp/shared/groups/2024/novel-fluor/shared/dat/NF_results/BLUE/09_final_output/m64047_230308_062131.ccs.0--0-final.csv',
            '/projects/bgmp/shared/groups/2024/novel-fluor/shared/dat/NF_results/BLUE/09_final_output/m64047_230308_062131.ccs.1--1-final.csv',
            '/projects/bgmp/shared/groups/2024/novel-fluor/shared/dat/NF_results/BLUE/09_final_output/m64047_230308_062131.ccs.2--2-final.csv',
            '/projects/bgmp/shared/groups/2024/novel-fluor/shared/dat/NF_results/BLUE/09_final_output/m64047_230308_062131.ccs.3--3-final.csv',
            '/projects/bgmp/shared/groups/2024/novel-fluor/shared/dat/NF_results/BLUE/09_final_output/m64047_230308_062131.ccs.4--4-final.csv',
            '/projects/bgmp/shared/groups/2024/novel-fluor/shared/dat/NF_results/BLUE/09_final_output/m64047_230308_062131.ccs.5--5-final.csv',
            '/projects/bgmp/shared/groups/2024/novel-fluor/shared/dat/NF_results/BLUE/09_final_output/m64047_230308_062131.ccs.6--6-final.csv',
            '/projects/bgmp/shared/groups/2024/novel-fluor/shared/dat/NF_results/BLUE/09_final_output/m64047_230308_062131.ccs.7--7-final.csv',
            '/projects/bgmp/shared/groups/2024/novel-fluor/shared/dat/NF_results/BLUE/09_final_output/m64047_230308_062131.ccs.8--8-final.csvv'
]            


red_csv_files = csv_files = [
            '/projects/bgmp/shared/groups/2024/novel-fluor/shared/dat/NF_results/RED/09_final_output/m64047_230306_210601.ccs.0--0-final.csv',
            '/projects/bgmp/shared/groups/2024/novel-fluor/shared/dat/NF_results/RED/09_final_output/m64047_230306_210601.ccs.1--1-final.csv',
            '/projects/bgmp/shared/groups/2024/novel-fluor/shared/dat/NF_results/RED/09_final_output/m64047_230306_210601.ccs.2--2-final.csv',
            '/projects/bgmp/shared/groups/2024/novel-fluor/shared/dat/NF_results/RED/09_final_output/m64047_230306_210601.ccs.3--3-final.csv',
            '/projects/bgmp/shared/groups/2024/novel-fluor/shared/dat/NF_results/RED/09_final_output/m64047_230306_210601.ccs.4--4-final.csv',
            '/projects/bgmp/shared/groups/2024/novel-fluor/shared/dat/NF_results/RED/09_final_output/m64047_230306_210601.ccs.5--5-final.csv',
            '/projects/bgmp/shared/groups/2024/novel-fluor/shared/dat/NF_results/RED/09_final_output/m64047_230306_210601.ccs.6--6-final.csv',
            '/projects/bgmp/shared/groups/2024/novel-fluor/shared/dat/NF_results/RED/09_final_output/m64047_230306_210601.ccs.7--7-final.csv',
            '/projects/bgmp/shared/groups/2024/novel-fluor/shared/dat/NF_results/RED/09_final_output/m64047_230306_210601.ccs.8--8-final.csv'
]


dataframes1 = [] 

dataframes2 = [] 

for file in red_csv_files:
    if os.path.exists(file):
        df = pd.read_csv(file, header=None) #Assume no header 
        dataframes1.append(df)
    else:
        print(f"{file} does not exist")

#Combine df together 

combined_df = pd.concat(dataframes1, ignore_index=True)

combined_df.to_csv('redreads_combined_final_output.csv', index=False, header=False)



for file in blue_csv_files:
    if os.path.exists(file):
        df = pd.read_csv(file, header=None) #Assume no header 
        dataframes2.append(df)
    else:
        print(f"{file} does not exist")

#Combine df together 

combined_df = pd.concat(dataframes2, ignore_index=True)

combined_df.to_csv('bluereads_combined_final_output.csv', index=False, header=False)


print("Combined") 



