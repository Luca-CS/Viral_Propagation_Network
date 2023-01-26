from fonctionsutiles import *
import numpy as np
import matplotlib.pyplot as plt
import math as ma

l0 = [638779430]
l1 = [953043456]
l2 = [650889385]
l3 = [144265898]

for index, row in post_df.iterrows():
    if row.id_post_origin in l0:
        l0.append(row.id_post)
    if row.id_post_origin in l1:
        l1.append(row.id_post)
    if row.id_post_origin in l2:
        l2.append(row.id_post)
    if row.id_post_origin in l3:
        l3.append(row.id_post)


# import exponential

# Using exponential() method
gfg = 100*np.random.exponential(1/6, 10000)

count, bins, ignored = plt.hist(gfg, 14, density=True)
plt.show()
