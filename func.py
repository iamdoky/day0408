import pandas as pd


# 3개의 파일을 하나의 DataFrame으로 반환하는 함수
def getMovies():
    movies = pd.read_csv('../ml-1m/movies.dat', sep="::", engine='python', header=None,names=['movie_id', 'title', 'genre'])
    users = pd.read_csv('../ml-1m/users.dat', sep="::", engine='python', header=None,names=['user_id', 'gender', 'age', 'job', 'addr'])
    ratings = pd.read_csv('../ml-1m/ratings.dat', sep="::", engine='python', header=None,names=['user_id', 'movie_id', 'rating', 'time'])
    df = pd.merge(pd.merge(movies, ratings), users)
    return df

# 평가 수가 500건 이상인 영화제목을 내림차순으로 반환하는 함수
def get_movie_500():
    df = getMovies()
    title_cnt = pd.pivot_table(df, values='rating', index='title', aggfunc='count')
    title_500 = title_cnt[title_cnt['rating'] >= 500]
    title_500_sort = title_500.sort_values(by='rating', ascending=False)
    return title_500_sort