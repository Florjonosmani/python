import pandas as pd
from numpy.ma.core import product

product['Apples','Bananas','Oranges','Grapes','Pineaples']

sales =[150,200,160,90,60]


sales_series = pd.Series(sales, index =product)
print(sales_series)

print(sales_series['Grapes'])

total_series = sales_series.sum()
print(total_series)

best_selling_product = sales_series.idxmax()
print(f"Best selling product: {best_selling_product}")