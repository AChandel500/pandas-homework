
# Assignment 5 - Advanced question

# import librairies
import pandas as pd

# Load the insurance.csv in a DataFrame using pandas. Explore the dataset using functions like to_string(), columns,
# index, dtypes, shape, info() and describe(). Use this DataFrame for the following exercises.

path='/home/user/PycharmProjects/Homework 5/insurance.csv'
insurance_data = pd.read_csv(path)

# Question 2: The 'to_string' function allows all the data to be viewed in the console as it returns a string containing
# all data. Useful for creating a reference copy of the data

print(f"\nQuestion 2 (to_string):\n\n{insurance_data.to_string()}")

# Question 2: the 'columns' function returns an index object consisting of column names, useful for extracting column
# identifiers for column 'indexing' or referencing to access data

print(f"\nQuestion 2 (columns):\n\n{insurance_data.columns}")

# Question 2: 'index' is a Dataframe attribute containing the index (row) identifiers for the dataframe, also for referencing
# to access the data
print(f"\nQuestion 2 (index):\n\n{insurance_data.index}")

# Question 2: The 'dtypes' function returns a Series containing the data types of each column of the dataframe, useful for
# identifying the type of data in a field and converting if required

print(f"\nQuestion 2 (dtypes):\n\n{insurance_data.dtypes}")

# Question 2: The 'shape' function returns a tuple containing the dimensions of the dataframe

print(f"\nQuestion 2 (shape):\n\n{insurance_data.shape}")

# Question 2: The 'info' function groups by column to summarize information about the data, such as names, non-null value
# count, data types and data type count.  It also displays the memory footprint of the data.

print(f"\nQuestion 2 (info):\n"); insurance_data.info()

# Question 2: Describe groups by column to summarize value count, mean, standard deviation and minimum and maximum
# values.  Presents useful information at a glance about data characteristics.

print(f"\nQuestion 2 (describe):\n\n{insurance_data.describe()}")

# Question 3: Print column 'age' only

print (f"\nQuestion 3:\n\n{insurance_data['age'].to_string()}")

# #Question 4: Print age, children and charges only

print(f"\nQuestion 4:\n\n{insurance_data[['age', 'children', 'charges']].to_string()}")

# Question 5: Print only the first 5 lines and only the columns age,children and charges

print(f"\nQuestion 5:\n\n{insurance_data.head()[['age','children','charges']]}")

#Question 6: Average, minimum and maximum charges

print(f"\nQuestion 6:\n")
print(f"The mean, minimum and maximum of the charges field are:\n\n"
      f"Mean:\n{insurance_data[['charges']].mean(skipna=True)[0]}\n\n"
      f"Min:\n"
      f"{insurance_data[['charges']].min(skipna=True)[0]}\n\n"
      f"Max:\n{insurance_data[['charges']].max(skipna=True)[0]}\n\n" )

#Question 7: Age, sex, smoker status of person who paid 10797.3362

print(f"Question 7:\n")
print(f"The age, gender and smoker status of the person who paid 10797.3362 is:\n\n"
      f"{insurance_data[insurance_data.charges==10797.3362][[ 'age','sex','smoker']]}\n")

#Question 8: Age of the person who paid the maximum charge

print(f"\nQuestion 8:\n")
print(f"The age of the person who paid the maximum charge is:\n\n"
      f"{insurance_data[insurance_data.charges==insurance_data[['charges']].max(skipna=True)[0]][['age']]}\n")

#Question 9: How many insured people do we have for each region? Assuming children are insured as dependents.

print(f"\nQuestion 9:\n")
for value in insurance_data['region'].unique():

      insured_per_region = insurance_data[insurance_data.region == value].count().age + insurance_data[insurance_data.region == value].sum().children

      print(f"In the {value} there are: {insured_per_region} insured people.\n" )


#Question 10: How many insured people are children?  Assuming children are insured as dependents.
# Otherwise the answer is zero (no policy holders under 18)

print(f"\nQuestion 10:")

total_insured_children = insurance_data[['children']].sum()
print(f"\nThere are {total_insured_children} insured children.\n")

# Question 11: What do you expect to be the correlation between charges and age, bmi and children?
# Answer: Charges will be higher with age and bmi will be higher with more children.

# Question 12: Using the method corr(), check if your assumptions were correct.

print(f"\n{insurance_data.corr()}")
print("\nWe can see that the correlation between age and charges is high at 0.299008 and between bmi"
      " and children is actually low at 0.012759.\n")

