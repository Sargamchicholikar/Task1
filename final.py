import pandas as pd

df = pd.read_csv("Input1.csv")
#Print befor merging 
print(df)
grouped = df.groupby(["Team_Name"])
merged = grouped.agg(lambda x: '|'.join(x))
merged = merged.reset_index()

merged.to_csv("Input1.csv", index=False)
#Print after merging
print(grouped)

#Second OutPut

df1=pd.read_csv("Input2.csv")

# displaying unsorted data frame
print("\nBefore sorting:")
print(df1)
  
# sort data frame
df1.sort_values(by=["total_statements","total_reasons"], 
                    axis=0,
                    ascending=[False,False], 
                    inplace=True)
  
# displaying sorted data frame
print("\nAfter sorting:")
print(df1)
