import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules, fpgrowth
from mlxtend.preprocessing import TransactionEncoder

dataset = [
    ['milk','berad'],
    ['milk', 'apple'],
    ['bread', ' apple'],
    ['milk','bread','apple'],
    ['bread']
]

te = TransactionEncoder()
df= pd.DataFrame(te.fit_transform(dataset),columns=te.columns_)

frequent_itemsets= fpgrowth(df, min_support= 0.4, use_colnames= True)
rules = association_rules(frequent_itemsets,metric='lift', min_threshold= 1.0)

print("Frequet itemsets\n", frequent_itemsets)
print("\n Association Rules :\n", rules)