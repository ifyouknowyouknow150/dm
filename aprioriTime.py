import pandas as pd
from mlxtend.frequent_patterns import apriori, fpgrowth, association_rules
from mlxtend.preprocessing import TransactionEncoder
import time

# Sample dataset
dataset = [
    ['milk', 'bread', 'nuts', 'apple'],
    ['milk', 'nuts'],
    ['milk', 'bread'],
    ['milk', 'apple']
]

# Convert transactions to DataFrame
df = pd.DataFrame(TransactionEncoder().fit_transform(dataset), columns=TransactionEncoder().fit(dataset).columns_)

# Apply Apriori and FP-Growth
for algo, func in zip(["Apriori", "FP-Growth"], [apriori, fpgrowth]):
    start = time.time()
    frequent_itemsets = func(df, min_support=0.3, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.0)
    print(f"\n{algo} Frequent Itemsets:\n", frequent_itemsets)
    print(f"Execution Time - {algo}: {time.time() - start:.5f} sec")
