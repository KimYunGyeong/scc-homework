from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

search_movie = db.movies.find_one({'title': '월-E'})
search_star = search_movie['star']

db.movies.update_many({'star': search_star}, {'$set': {'star': '0'}})

# movies = list(db.movies.find({'star': search_star}))
# for movie in movies:
#     print(movie['title'])
