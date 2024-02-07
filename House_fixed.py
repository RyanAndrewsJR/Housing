import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

# Define the plot_comparison function
def plot_comparison(type, data1, x_data1, y_data1, data2, x_data2, y_data2):
    """
    Function to compare data from two datasets using Seaborn and Matplotlib.

    Parameters:
        type (str): Type of plot ('scatter', 'line', 'bar', etc.).
        data1 (pd.DataFrame): First dataset.
        x_data1 (str): Column name for x-axis data in dataset 1.
        y_data1 (str): Column name for y-axis data in dataset 1.
        data2 (pd.DataFrame): Second dataset.
        x_data2 (str): Column name for x-axis data in dataset 2.
        y_data2 (str): Column name for y-axis data in dataset 2.
    """
    if type == 'scatter':
        sns.scatterplot(data=data1, x=x_data1, y=y_data1)
        sns.scatterplot(data=data2, x=x_data2, y=y_data2)
        plt.xlabel('Year')
        plt.ylabel(y_data1)  # Assuming y_data1 and y_data2 are the same for consistency
        plt.legend(labels=['Trilogy Price/SqFt', 'Governemnt House Price Index\n Riverside county'])
        plt.title('Comparison of {} between two datasets'.format(y_data1))
        plt.show()
    if type == 'displot':
        sns.displot(data=data1, x=x_data1, y=y_data1)
        sns.displot(data=data2, x=x_data2, y= y_data2)
        plt.show()
    # Add other plot types as needed

# Read data
census_data = pd.read_csv('/Users/ryanquinnandrews/Desktop/stats/HPI_master.csv')
tril_data = pd.read_csv('/Users/ryanquinnandrews/Desktop/stats/triltrend.csv')

# Filter Census data
house_data_riv = census_data[census_data['place_id'].str.contains('40140')]

# Convert 'Closed Date' to datetime format and extract year
tril_data['Year'] = pd.to_datetime(tril_data['Closed Date'], infer_datetime_format=True).dt.year

# Extract year from 'yr' in House_data_Riv
house_data_riv['Year'] = pd.to_datetime(house_data_riv['yr'], format='%Y').dt.year

# Get common years between tril_data and house_data_riv
common_years = set(tril_data['Year']).intersection(set(house_data_riv['Year']))

# Filter tril_data and house_data_riv to include only common years
tril_data_common = tril_data[tril_data['Year'].isin(common_years)]
house_data_riv_common = house_data_riv[house_data_riv['Year'].isin(common_years)]

# Call the function with the merged dataset and appropriate x and y data
plot_comparison('scatter', tril_data_common, 'Year', 'Sold Price/SqFt', house_data_riv_common, 'Year', 'index_nsa')


#create function with year argument and plot by years

#Combine data sets 

#out of date working with new data set (for the better)





























