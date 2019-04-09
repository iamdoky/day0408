import pandas as pd
from day0408 import func

df = func.getMovies()

# 영화별 투표건 수를 출력
title_cnt = pd.pivot_table(df,values='rating', index='title',aggfunc='count')

# 평가 건수가 100개 이상인 영화제목 출력
# rating_100 = title_cnt['rating'] >= 100
title_500 = title_cnt[title_cnt['rating'] >= 500]

# 평가 건수가 500개 이상인 영화제목을 내림차순
title_500_sort = title_500.sort_values(by = 'rating', ascending = False)
print(title_500_sort)




