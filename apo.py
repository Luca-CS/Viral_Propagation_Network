from fonctionsutiles import *
import matplotlib.pyplot as plt

l0 = [638779430]
l1 = [953043456]
l2 = [650889385]
l3 = [144265898]
    
for index,row in post_df.iterrows() :
    if row.id_post_origin in l0 :
        l0.append(row.id_post)
    if row.id_post_origin in l1 :
        l1.append(row.id_post)
    if row.id_post_origin in l2 :
        l2.append(row.id_post)
    if row.id_post_origin in l3 :
        l3.append(row.id_post)

#calcul du kpi par post originel 

def kpi(liste):
    kpi,views,likes,comments,reposts,clicks,donations = 0,0,0,0,0,0,0
    
    for id in liste:
        row = post_df[post_df['id_post']==id]
        views += int(row['views'])
        likes += int(row['likes'])
        comments += int(row['comments'])
        reposts += int(row['reposts'])
        clicks += int(row['link_clicks'])
        if str(row['donation_tag'])=='TRUE':
            donations += 1
    
    kpi = views/251167 + likes/68109 + comments/12730 + reposts/3043 + clicks/320 + donations/31
    return kpi

X = [0,1,2,3]
Y = [kpi(l0),kpi(l1),kpi(l2),kpi(l3)]
print(Y)
plt.scatter(X,Y)
plt.show()
        
        
        
