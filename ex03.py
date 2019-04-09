import numpy as np
import pandas as pd
import func
import matplotlib.pyplot as plt

df = func.getMovies()

# unstasck  :   index를 column으로 만들어 준다. / index가 2개일떄 2번째 index를 column으로 표현하여
# stack     :   stack을 사용하여 원래 모습으로 복원한다.

# r1 = pd.pivot_table(df,values='rating',index='gender', aggfunc='mean')
# r2 = r1.unstack()
# r1 = pd.pivot_table(df,values='rating', index=['gender','age'],aggfunc='mean')
# r2 = r1.unstack()
# r3 = r2.stack()

# 나이대별 성별별로 평점의 평균과 합을 출력

# r = pd.pivot_table(df,values='rating',index='gender',columns='age',aggfunc=['mean','sum'])
# r = pd.pivot_table(df,values='rating',index='age',columns='gender',aggfunc=[np.mean,np.sum])
# 만약 함수명이 오류가 발생 시 넘파이를 요규할 수도 있으므로 해당 상황 시 넘파이 사용

# 나이대별 성별 별점의 평균을 구함
r1 = pd.pivot_table(df,values='rating',index='age',columns='gender',aggfunc='mean')
# 나이대별 성별 별점의 합
r2 = pd.pivot_table(df,values='rating',index='age',columns='gender',aggfunc='sum')
# r3 = pd.merge(r1,r2)
# print(r3)

r3 = pd.concat([r1,r2],axis=1)
print(r3)
