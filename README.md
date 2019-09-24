Neo4j生成知识图谱

```markdown
neo4j 导入csv文件数据
neo4j-admin import --mode=csv --database=userMovie.db --nodes resources\film.csv --nodes resources\director.csv --nodes resources\actor.csv --nodes resources\types.csv --relationships resources\relationship_actor_film.csv --relationships resources\relationship_director_actor.csv --relationships resources\relationship_director_film.csv --relationships resources\relationship_film_type.csv
```