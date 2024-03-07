# Monte-Carlo-simulation
##  Forecasting Sales and Cost of Sales with Monte Carlo Simulation

### Overview

This repository contains Python code for simulating sales revenue and cost of sales using Monte Carlo simulation techniques. Monte Carlo simulation is a powerful method for forecasting outcomes by running iterations with predetermined inputs to produce different outputs. This approach is particularly useful when historical data is available to determine the standard deviation of actual performance from its mean over time.

### Purpose

The purpose of this project is to demonstrate how Monte Carlo simulation can be applied to forecast sales revenue and cost of sales. By leveraging historical data, we can estimate the standard deviation and average ratio of cost of sales to sales, allowing us to simulate various scenarios and understand the potential distribution of outcomes.

### Key Features

Simulation Function: The simulate_sales_and_cost function accepts input parameters such as units projected to be sold per product, price list, standard deviation, cost of sales ratio, and the number of simulations. It returns a DataFrame of mean sales and cost of sales, along with histograms visualizing the distribution of simulated data.

Projection Function: The projected_sales function calculates the projected sales revenue and cost of sales based on provided product units, price list, and cost of sales ratio.

Confidence Interval Calculation: The limits function calculates and prints the lower and upper limits of projected sales and cost of sales, providing insights into the potential range of outcomes.
