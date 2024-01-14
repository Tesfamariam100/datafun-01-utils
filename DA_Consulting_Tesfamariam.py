"""
This module provides an introductory byline for a hypothetical data analytics consulting company.
"""

import statistics

# Company information/defining variables
company_name = "Tesfamariam Data Analytics Consulting LTD"
year_founded = 2023
revenue = 200000.0
expenses = 100000.0
is_profitable = True

#Defining formatted strings
revenue_str = f"${revenue}"
expenses_str = f"${expenses}"
profit_str = f"${revenue-expenses}"

#Calculating descriptive statistics
data = [revenue, expenses]
mean = statistics.mean(data)
stdev = statistics.stdev(data)

#Defining byline string
byline = f"{company_name} was founded in {year_founded}. " \
         f"is it profitable? {is_profitable}. " \
         f"revenue:{revenue_str}. " \
         f"expenses:{expenses_str}. " \
         f"profit:{profit_str}. " \
         f"mean:{mean}. " \
         f"standard develation:{stdev}."
         
def main():
    #Conditional script execution
    print(byline)
    
if __name__ == '__main__':
    main()

