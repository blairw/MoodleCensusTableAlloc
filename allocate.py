from numpy import number
import pandas as pd
from random import randint

# Ingest the class roll from Moodle
df_moodle_roll = pd.read_csv("moodle.csv")

# Extract relevant columns from the roll only
df_students = df_moodle_roll[["Username", "First name", "Surname"]]

# Rename columns because otherwise how will I know that "Username" is zID?
renaming_pattern = {
    "Username": "zID",
    "First name": "Firstname"
}
df_students = df_students.rename(columns=renaming_pattern)

# Remove tutors from the class roll
df_tutors_list = pd.read_csv("tutor_list.csv")
tutors_list = df_tutors_list["tutor_zID"].tolist()
df_students = df_students.loc[~ df_students["zID"].isin(tutors_list)]

# Set up BCP2011 and GCP2016 columns
df_students["AllocatedBCP2011"] = "TBC"
df_students["AllocatedGCP2016"] = "TBC"

# Ingest the Mapping File
df_census_tables = pd.read_csv("2011BCP_2016GCP_Mapping rev03.csv")

# How many census tables do we have?
number_of_census_tables = len(df_census_tables.index)

# Time to assign!
for roll_index, roll_row_data in df_students.iterrows():
    selected_table_set_id = randint(0, number_of_census_tables - 1)
    selected_table_set_data = df_census_tables.iloc[selected_table_set_id]

    label_for_2011 = selected_table_set_data["2011 BCP Table"] + " " + selected_table_set_data["2011 name"]
    label_for_2016 = selected_table_set_data["2016 GCP Table"] + " " + selected_table_set_data["2016 name"]

    roll_row_data["AllocatedBCP2011"] = label_for_2011
    roll_row_data["AllocatedGCP2016"] = label_for_2016


# Done, show results
print(df_students)
df_students.to_csv("allocation_results.csv")