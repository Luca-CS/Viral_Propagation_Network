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
