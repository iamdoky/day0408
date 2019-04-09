import func
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df =func.getMovies()

# 성별 별로 별점의 평균을 알고 싶다.
# gender_mean = df.pivot_table(values='rating',index='gender')
# gender_mean2 = df.pivot_table(values='rating',index='gender',aggfunc='mean')
# gender_sum = df.pivot_table(values='rating',index='gender',aggfunc='sum')
# gender_max = df.pivot_table(values='rating',index='gender',aggfunc='max')
# gender_min = df.pivot_table(values='rating',index='gender',aggfunc='min')

# 나이별로 별점의 평균을 출력해 봅니다.
# age_mean = df.pivot_table(values='rating',index='age',aggfunc='mean')

# 나이대별, 성별별로 rating의 평군을 다음과 같이 보여주세요.
# age_mean_gendr = pd.pivot_table(df,values='rating',index='age',columns='gender',aggfunc='mean')
# gender_mean_age = pd.pivot_table(df,values='rating',index='gender',columns='age',aggfunc='mean')

# 인덱스를 수정하여 차트로 출력
# r = pd.pivot_table(df,values='rating',index='age',columns='gender',aggfunc='mean')
# r.index = ['udner 18','18~24','25~34','35~44','45~49','50~5','56+']
# print(r)
# r.plot()
# r.plot(kind='bar')
# plt.show()

# r = pd.pivot_table(df,values='rating', index='gender', aggfunc='mean')
# r = pd.pivot_table(df,values='rating', index='gender', aggfunc='mean', columns='age')
# r = pd.pivot_table(df,values='rating', index='gender', aggfunc='mean', columns='gender')
# r = pd.pivot_table(df,values='rating', index=['age','gender'],aggfunc='mean')
# r2 = pd.pivot_table(df,values='rating', index=['gender','age'],aggfunc='mean')
# print(r)
# print(r2)


# help(pd.pivot_table)

# 직업별 성별 나이대별 평균 평점을 알려주세요. 단 결측치는 0으로 채워주세요.
# r = pd.pivot_table(df,values='rating',index=['gender','job','age'], aggfunc='mean')
# r = pd.pivot_table(df,values='rating',index=['gender','age'],columns='job', aggfunc='mean',fill_value=0)
# print(r)

# r = pd.pivot_table(df,values='rating',index=['job','age'],columns='gender', aggfunc='mean',fill_value=0)
# r = pd.pivot_table(df,values='rating',index=['age','job'],columns='gender', aggfunc='mean',fill_value=0)
# r = pd.pivot_table(df,values='rating',index=['age','gender'],columns='job', aggfunc='mean',fill_value=0)
# pivot table 시에 어떤 것은 index와 column으로 지정되지 않았지만 항목의 개수가 많을 것을 column으로 하는 것이 가독성이 좋다.

# r = pd.pivot_table(df,values='rating', index='gender',columns='age',aggfunc='mean')
r = pd.pivot_table(df,values='rating', index='age',columns='gender',aggfunc='mean')
print(r)

# 행과 열을 바꿔주는 함수 unstack() :  column ---> 첫번쨰 index가 되었음.
r3 = r.unstack()
print(r)

