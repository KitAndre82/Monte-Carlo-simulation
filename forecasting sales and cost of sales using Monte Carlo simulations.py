'''FORECASTING USING MONTE CARLO SIMULATION
Suppose you are required to forecast sales revenue, cost of sales, and gross profit.
You could use historical data and calculate the average rate of growth/ decline per year and make projections based on that.
But this can yield misleading results due to the flaw of averages.
You could use linear regression if you are able to establish a linear relationship between your variables. 
Another way would be to use Monte Carlo simulations.
This is basically running iterations using predetermined inputs to produce different outputs and then
using the distribution of these outputs to determine the expected outputs. 
In the scenario above, historical data can be used to determine the standard deviation (SD) of actual
performance from its mean over time. This SD can then be represented as a percentage of the mean actual performance.
Below is how you could approach it using Python. This can be done using spreadsheets as well.
Python is my choice of tool for such tasks because of how feasible it is to add complex logic to the model.
'''


import pandas as pd
import numpy as np
import seaborn as sns
import random
import matplotlib.pyplot as plt

# Set the style for seaborn plots
sns.set_style('whitegrid')



def simulate_sales_and_cost(units_per_pdt, price_list, std_dev, COS_sales_ratio, num_simulations):
    ''' Function uses Monte Carlo analysis to simulate sales revenue and cost of sales. 
        It accepts 5 parameters:
        1: units_per_pdt: These are the units of the products projected to be sold. 
           They are stored in a list.
        2. price_list: These are the prices per unit of product. These are also stored in a list.
        3. std_dev: This is derived from historical data. It is the standard deviation of actual 
           performance from its mean.
        4. COS_sales_ratio: This is also derived from historical data. It is average COS to sales ratio.
        5. num_simulations: The number of Monte Carlo simulations.
        
        The function returns a dataframe of mean sales and COS which follow a normal distribution.
        It also plots a histogram of the distribution of the mean sales and COS.
    '''
    
    # Function to calculate cost of sales
    def calc_COS(sales):
        return sales * COS_sales_ratio

    # Define a list to keep all the results from each simulation that we want to analyze
    sim_results = []

    # Loop for the simulations
    for i in range(num_simulations):
        # Choose random inputs for the sales targets and percent to target
        sales_targets = [num_pdts * price for num_pdts, price in zip(units_per_pdt, price_list)]
        total_sales_target = sum(sales_targets)
        
        # Generate random sales projections within 2 standard deviations of total_sales_target
        start = int(total_sales_target - (2 * std_dev * total_sales_target))
        end = int(total_sales_target + (2 * std_dev * total_sales_target))
        sales_projections = random.sample(range(start, end+1), int(num_simulations*0.001))
        
        # Generate sales targets 
        sales_projections_sim = np.random.choice(sales_projections, num_simulations)
        
        # Build the dataframe based on the inputs and number of reps
        df = pd.DataFrame(index=range(num_simulations), data={'Sales': sales_projections_sim})
                                                              
        # Calculate cost of sales
        df['COS'] = df['Sales'].apply(calc_COS)
       
        # We want to track sales, and cost of sales over all the simulations
        sim_results.append([df['Sales'].mean().round(2),
                            df['COS'].mean().round(2)])

    # Convert simulation results to DataFrame
    results_df = pd.DataFrame(sim_results, columns=['Sales', 'COS'])
    
    # Create subplots
    fig, ax = plt.subplots(1, 2)

    # Plot histograms of sales and cost of sales
    results_df['Sales'].plot(kind='hist', title='Sales Distribution', ax=ax[0])
    results_df['COS'].plot(kind='hist', title='Cost of Sales Distribution', ax=ax[1])

    # Show the plots
    plt.show()
    
    return results_df

def limits(df):
    '''
    Accepts a simulated dataframe of sales and COS and prints a 
       confidence interval for projected sales.
       
    The function returns lower and upper limits of projected sales and COS.   
    '''
    
    lower_limit_sales = df['Sales'].mean() - (2 * df['Sales'].std())

    upper_limit_sales = df['Sales'].mean() + (2 * df['Sales'].std())


    lower_limit_sales_formatted = '{:,}'.format(round(lower_limit_sales,2))
    upper_limit_sales_formatted = '{:,}'.format(round(upper_limit_sales,2))

    print("Lower Limit Sales:", lower_limit_sales_formatted)
    print("Upper Limit Sales:", upper_limit_sales_formatted)
    
    lower_limit_COS = df['COS'].mean() - (2 * df['COS'].std())

    upper_limit_COS = df['COS'].mean() + (2 * df['COS'].std())


    lower_limit_COS_formatted = '{:,}'.format(round(lower_limit_COS,2))
    upper_limit_COS_formatted = '{:,}'.format(round(upper_limit_COS,2))

    print("Lower Limit COS:", lower_limit_COS_formatted)
    print("Upper Limit COS:", upper_limit_COS_formatted)
    
    
    return lower_limit_sales, upper_limit_sales,lower_limit_COS, upper_limit_COS

def projected_sales(pdt_nums,price_list,COS_sales_ratio):
    ''' Accepts 3 parameters; products units list, the price list and COS_sales_ratio and returns projected sales and COS'''
    projected_sales = 0
    for pdts, price in zip(pdt_nums,price_list):
        projected_sales += pdts*price   
    return projected_sales, projected_sales*COS_sales_ratio

# Storing dataframe of means of simulated means and COS in a variable called results 
results = simulate_sales_and_cost(pdt_nums, price_list, std_dev, COS_sales_ratio, num_simulations)


print('Projected sales: ', '{:,}'.format(round(projected_sales(pdt_nums,price_list,COS_sales_ratio)[0],2)))
print('Projected COS: ', '{:,}'.format(round(projected_sales(pdt_nums,price_list,COS_sales_ratio)[1],2)))

# Printing lower and upper limits of projected sales and COS
print('Upper and lower limits of projected sales and COS: ')
limits(results)




