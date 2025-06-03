import pandas as pd

products = ['apples', 'grape','bananas','lemons']
prices = [150,140,130,120]

sale_seriers = pd.Series(prices,index=products)
print(sale_seriers)

print(sale_seriers['grape'])

total_sales = sale_seriers.sum()
print(total_sales)

data ={
    "Name" : ["leon", "dion", "edin"],
    "Age"  : [30,27,19],
    "City" : ["Prishtin", "Gilan", "Gjakov"],
}

df=pd.DataFrame(data)
print(df)

#df = pd.read_csv(cs.csv)
#df = pd.to_csv("dion", index=False)

best_selling_products = sale_seriers.idxmax()
print(f"Best selling products:{best_selling_products}")