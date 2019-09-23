# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_csv(r'D:\work\douban\douban\resources\douban.csv', encoding="utf-8")

df_film = pd.read_csv(r'D:\work\douban\douban\resources\film.csv', encoding="utf-8")

df_director = pd.read_csv(r'D:\work\douban\douban\resources\director.csv', encoding="utf-8")

df_actor = pd.read_csv(r'D:\work\douban\douban\resources\actor.csv', encoding="utf-8")

df_types = pd.read_csv(r'D:\work\douban\douban\resources\types.csv', encoding="utf-8")

director_films = []
actor_films = []
director_actors = []
film_types = []

for index, row in df.iterrows():
    # print(row)
    film_name = row['电影名称']
    director = row['导演']
    actor = row['演员']
    types = row['类型']

    directorList = director.split('/')
    actorList = actor.split('/')
    typesList = types.split('/')
    # 获取电影ID
    filmID = df_film['index:ID'].loc[df_film['film'] == film_name].values[0]

    #  生成导演-电影关系
    for dire in directorList:
        directorID = df_director['index:ID'].loc[df_director['director'] == dire].values[0]
        director_film = [directorID, filmID, '导演', '导演']
        director_films.append(director_film)

    # 生成演员-电影关系
    for act in actorList:
        actorID = df_actor['index:ID'].loc[df_actor['actor'] == act].values[0]
        actor_film = [actorID, filmID, "出演", "出演"]
        actor_films.append(actor_film)

    # 生成导演-演员关系
    for dire in directorList:
        directorID = df_director['index:ID'].loc[df_director['director'] == dire].values[0]
        for act in actorList:
            actorID = df_actor['index:ID'].loc[df_actor['actor'] == act].values[0]
            director_actor = [directorID, actorID, '合作', '合作']
            director_actors.append(director_actor)

    # 生成电影-类型关系
    for ty in typesList:
        typeID = df_types['index:ID'].loc[df_types['types'] == ty].values[0]
        film_type = [typeID, filmID, "类型", "类型"]
        film_types.append(film_type)

# 导出导演-电影关系文件
df_director_film = pd.DataFrame(data=director_films, columns=[':START_ID', ':END_ID', 'relation', ':TYPE'])
df_director_film.to_csv(r'D:\work\douban\douban\resources\relationship_director_film.csv', index=False, encoding='utf-8_sig')

# 生成演员-电影关系
df_actor_film = pd.DataFrame(data=actor_films, columns=[':START_ID', ':END_ID', 'relation', ':TYPE'])
df_actor_film.to_csv(r'D:\work\douban\douban\resources\relationship_actor_film.csv', index=False, encoding='utf-8_sig')

# 生成导演-演员关系
df_director_actor = pd.DataFrame(data=director_actors, columns=[':START_ID', ':END_ID', 'relation', ':TYPE'])
df_actor_film.to_csv(r'D:\work\douban\douban\resources\relationship_director_actor.csv', index=False, encoding='utf-8_sig')

# 生成电影-类型关系
df_film_type = pd.DataFrame(data=film_types, columns=[':START_ID', ':END_ID', 'relation', ':TYPE'])
df_film_type.to_csv(r'D:\work\douban\douban\resources\relationship_film_type.csv', index=False, encoding='utf-8_sig')
