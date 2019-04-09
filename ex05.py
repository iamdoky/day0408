import pandas as pd
from day0408 import func

df = func.getMovies()
cnt_500 = func.get_movie_500()

# 평가한 사람이 500명 이상인 영화중에 성별별로 영화별로 평균을 출력
# a = pd.pivot_table(df,values='rating',index='title',columns='gender',aggfunc='mean')
# b = a.loc[cnt_500.index]
# b['diff'] = (b['F'] - b['M']).abs()     # 절대값을 구하는 abs() 함수.
# c = b.sort_values(by = "diff", ascending=False)

# # 남자가 더 좋아하는 영화 5개
# a = pd.pivot_table(df,values='rating',index='title',columns='gender',aggfunc='mean')
# b = a.loc[cnt_500.index]
# b['mdiff'] = b['M']-b['F']
# c = b.sort_values(by = 'mdiff', ascending=False)
#
# # 여자가 더 좋아하는 영화 5개
# a = pd.pivot_table(df,values='rating',index='title',columns='gender',aggfunc='mean')
# b = a.loc[cnt_500.index]
# b['fdiff'] = b['F']-b['M']
# c = b.sort_values(by = 'mdiff', ascending=False)

# 남여 호불호가 없는 영화 5개
# a = pd.pivot_table(df,values='rating',index='title',columns='gender',aggfunc='mean')
# b = a.loc[cnt_500.index]
# b['fav'] = (b['F'] - b['M']).abs()
# c = b.sort_values(by = 'fav')

# 남여 모두 가장 좋아하는 영화 5개
a = pd.pivot_table(df,values='rating',index='title',columns='gender',aggfunc='mean')
b = a.loc[cnt_500.index]
b['fmadd'] = b['F'] + b['M']
c = b.sort_values(by = 'fmadd', ascending=False)
print(c.head())


