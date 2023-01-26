from fonctionsutiles import *
import matplotlib.pyplot as plt

post_df = readcsv('data/instagram_posts_0911_1111.csv')
print(post_df)
sumviews = post_df['views'].sum()
sumlikes = post_df['likes'].sum()
sumcomments = post_df['comments'].sum()
sumreposts = post_df['reposts'].sum()
sumlinks = post_df['link_clicks'].sum()
sumdonations = post_df['donation_tag'].sum()

print([sumviews,sumlikes,sumcomments,sumreposts,sumlinks,sumdonations])

plt.plot([sumviews,sumlikes,sumcomments,sumreposts,sumlinks,sumdonations])
plt.show()

def get_kpi(post_id):
    row = post_df[post_df['id_post']==post_id]
    if str(row['donation_tag'])=='TRUE':
        don = 1
    else : 
        don = 0
    kpi = int(row['views'])/251167 + int(row['likes'])/68109 + int(row['comments'])/12730 + int(row['reposts'])/3043 + int(row['link_clicks'])/320 + don/31
    return kpi

print(get_kpi(953043456))