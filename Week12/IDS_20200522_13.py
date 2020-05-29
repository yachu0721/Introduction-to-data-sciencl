avengers = ["The Avengers", "Avengers: Age of Ultron", "Avengers: Infinity War", "Avengers: Endgame"]
for idx, movie in enumerate(avengers):
    print("第 {} 部上映的復仇者聯盟是:{}".format(idx+1, movie))
print("-----------------------")
years = [2012, 2015, 2018, 2019]
for year, movie in zip(years, avengers):
    print("{}上映的年份是{}".format(movie, year))