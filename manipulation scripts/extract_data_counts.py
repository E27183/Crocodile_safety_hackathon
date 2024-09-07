import pandas as pd

path = "../data/"
processed_path = "../data/"
output_name = "Croc survey data.csv"
name = "Crocodile_Survey_Data_2021_22.xlsx"
sheet_name = "Cleaned data"
cluster = "REGION"

data = pd.read_excel(path+name, sheet_name)
# locations = data[cluster].astype('str')

# output_identifiers = {}
# output_names_ordered = []
# output_counts = []

# for i in locations:
#     j = i.lower().strip()
#     if j in output_identifiers.keys():
#         output_counts[output_identifiers[j]] += 1
#     else:
#         output_identifiers[j] = len(output_counts)
#         output_names_ordered.append(j)
#         output_counts.append(1)

# output = pd.DataFrame({'Location': output_names_ordered, 'Count': output_counts})
data.to_csv(processed_path+output_name)
