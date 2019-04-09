import numpy as np
import pandas as pd

scores = pd.read_csv('../Data/scores.csv')

# 각 학생별 과목의 평균을 구하여 출력

scores.index = scores['name']
del scores['class']
del scores['name']
# print(scores)
# print(scores.mean(axis=1))
# print(scores[['kor','eng','mat','bio']].mean(axis=1))

# scores 데이터프레임에 각 학생별 평균을 계산하여 컬럼을 추가
scores['avg'] = scores[['kor','eng','mat','bio']].mean(axis=1)
print(scores)

