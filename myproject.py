
# Assignment 5 - Reach Question
# Uses US flight data for February 2018, features are airport codes, departure/arrival times/delays and others.

# import librairies
import pandas as pd

def load_file(path):
    """Accepts a file path (str), loads file in the path to a Dataframe object and return the object."""
    return pd.read_csv(path)

def clean_data(dframe, in_place):
    """Accepts a dataframe, removes rows with null values and unnamed columns.  Returns a dataframe if inplace
    deletion of null rows/columns is not selected"""

    if in_place==True:
        flight_data.dropna(axis=1, how='all', inplace=in_place)
        flight_data.dropna(how='any', inplace=in_place)
        dframe.info()
        return
    else:
        flight_data.dropna(axis=1, how='all', inplace=in_place)
        flight_data.dropna(how='any', inplace=in_place)
        dframe.info()
        return dframe

def print_data_info(dframe):
    """Accepts a dataframe and outputs summary information"""

    print(f"\nQuestion 2b (Columns names):\n\n{dframe.columns}")


    print(f"\nQuestion 2b (index):\n\n{dframe.index}")


    print(f"\nQuestion 2b (dtypes):\n\n{dframe.dtypes}")


    print(f"\nQuestion 2b (shape):\n\n{dframe.shape}")


    print(f"\nQuestion 2b (info):\n");
    dframe.info()

    print(f"\nQuestion 2b (describe):\n\n{dframe.describe()}")

def check_corr(dframe):
    """Accepts a dataframe, prints correlation table"""
    print(flight_data.corr().to_string())





# Question 2a - load file and clean data

path = '/home/user/PycharmProjects/Homework 5/02_18.csv'

flight_data = load_file(path); flight_data.info()

# There are three columns that contain null values: dep_time, dep_del15 and arr_del15, which are
# the flight departure times, departure delays and arrival delays respectively.  There is also an unnamed column
# with all null values.
# To clean the data, the affected rows will be removed and the unnamed column as well.

clean_data(flight_data, in_place=True)

# There 509642 out of 520731 rows left after cleaning

# Question 2b - Compute and print information

print_data_info(flight_data)

# Question 2c - Print correlation table
check_corr(flight_data)

# Question 2d - There are no correlations over or under 0.3 or -0.3.  We can deduce that important metrics such as
# the departure delay and arrival delay are not correlated to a departure date or airport location.

