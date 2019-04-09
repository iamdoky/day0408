# Data폴더의 users, movies, rating 파일을 읽어들여 하나의 데이터프레임으로 만들어봅니다.

import numpy as np
import pandas as pd

movies = pd.read_csv('../ml-1m/movies.dat', sep="::", engine='python', header=None,names=['movie_id', 'title', 'genre'])
users = pd.read_csv('../ml-1m/users.dat', sep="::", engine='python', header=None, names=['user_id', 'gender', 'age', 'job', 'addr'])
ratings = pd.read_csv('../ml-1m/ratings.dat', sep="::", engine='python', header=None,names=['user_id', 'movie_id', 'rating', 'time'])
df = pd.merge(pd.merge(movies, ratings), users)
print(df.head(1))
# help(pd.merge)
# scores = pd.read_csv('../Data/scores.csv')
# print(scores)
# print(type(scores))
