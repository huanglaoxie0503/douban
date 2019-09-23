# -*- coding: utf-8 -*-
import pandas as pd


df = pd.read_csv(r"D:\work\douban\douban.csv", encoding="utf-8")

df_film = df["电影名称"]
df_director = df["导演"]
df_actor = df['演员']
df_types = df['类型']

filmID, directorID, actorID, typesID = [], [], [], []

"""
获得电影、导演、演员、类型的集合，方便ID编码
"""

# 获取电影的列表、数量、df表
filmList = list(df_film)
film_cnt = len(filmList)
df_film_name = pd.DataFrame(data=filmList, columns=['fileName'])

# 获取不重复导演的列表、数量、df表
directorList = []
for dire in df_director:
    directorList.extend(dire.split('/'))
directorList = list(set(directorList))
director_cnt = len(directorList)
df_director_name = pd.DataFrame(data=directorList, columns=['directorName'])

# 获取不重复的演员列表，数量、df表
actorList = []
for act in df_actor:
    actorList.extend(act.split('/'))
actorList = list(set(actorList))
actor_cnt = len(actorList)
df_actor_name = pd.DataFrame(data=actorList, columns=['actorName'])

# 获取不重复类型的列表、数量、df表
typesList = []
for ty in df_types:
    typesList.extend(ty.split('/'))
typesList = list(set(typesList))
types_cnt = len(typesList)
df_types_name = pd.DataFrame(data=typesList, columns=['typesName'])


"""
    生成电影、导演、演员、类型的ID
"""
# 生成电影ID
for i in range(10001, 10001 + film_cnt):
    filmID.append(i)
df_film_ID = pd.DataFrame(data=filmID, columns=['filmID'])

# 生成导演ID
for i in range(20001, 20001 + director_cnt):
    directorID.append(i)
df_director_ID = pd.DataFrame(data=directorID, columns=['directorID'])

# 生成演员ID
for i in range(30001, 30001 + actor_cnt):
    actorID.append(i)
df_actor_ID = pd.DataFrame(data=actorID, columns=['actorID'])

# 生成类型ID
for i in range(40001, 40001 + types_cnt):
    typesID.append(i)
df_types_ID = pd.DataFrame(data=typesID, columns=['typesID'])

"""
拼接结点数据
"""
# 拼接电影表
film = pd.concat([df_film_ID, df_film_name], axis=1)
film['label'] = '电影'

# 拼接导演表
director = pd.concat([df_director_ID, df_director_name], axis=1)
director['label'] = '导演'

# 拼接演员表
actor = pd.concat([df_actor_ID, df_actor_name], axis=1)
actor['label'] = '演员'

# 拼接类型表
types = pd.concat([df_types_ID, df_types_name], axis=1)
types['label'] = '类型'

"""
生成结点文件
"""
# 生成电影节点文件
film.columns = ['index:ID', 'film', ':LABEL']
film.to_csv('film.csv', index=False, encoding="utf-8_sig")

# 生成导演节点文件
director.columns = ['index:ID', 'director', ':LABEL']
director.to_csv('director.csv', index=False, encoding="utf-8_sig")

# 生成演员节点文件
actor.columns = ['index:ID', 'actor', ':LABEL']
actor.to_csv('actor.csv', index=False, encoding="utf-8_sig")

# 生成类型节点文件
types.columns = ['index:ID', 'types', ':LABEL']
types.to_csv('types.csv', index=False, encoding="utf-8_sig")


# 读取以上生成的结点文件
# df = pd.read_csv('douban.csv', encoding="utf-8")
