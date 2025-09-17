from collections import defaultdict

class FoodRatings:

    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        self.food_rate_map = {food: rate for food, rate in zip(foods, ratings)}
        self.food_cuisine_map = {f: c for f, c in zip(foods, cuisines)}
        self.cuisine_food_map = defaultdict(list)
        for c, f in zip(cuisines, foods):
            self.cuisine_food_map[c].append(f)
        self.best_rating = {}
        for f, c, r in zip(foods, cuisines, ratings):
            if self.best_rating.get(c, None):
                if self.food_rate_map.get(self.best_rating.get(c)) < r:
                    self.best_rating[c] = f
                elif self.food_rate_map.get(self.best_rating.get(c)) == r:
                    if self.best_rating.get(c) > f:
                        self.best_rating[c] = f
            else:
                self.best_rating[c] = f

    def changeRating(self, food: str, newRating: int) -> None:
        self.food_rate_map[food] = newRating
        if self.food_rate_map[self.best_rating[self.food_cuisine_map[food]]] < newRating:
            self.best_rating[self.food_cuisine_map[food]] = food
        elif self.food_rate_map[self.best_rating[self.food_cuisine_map[food]]] == newRating:
            if self.best_rating[self.food_cuisine_map[food]] > food:
                self.best_rating[self.food_cuisine_map[food]] = food

            if self.best_rating[self.food_cuisine_map[food]] == food:
                max_rate = 0
                for f in self.cuisine_food_map[self.food_cuisine_map[food]]:
                    if self.food_rate_map[f] > max_rate:
                        max_rate = self.food_rate_map[f]
                        self.best_rating[self.food_cuisine_map[food]] = f
                    elif self.food_rate_map[f] == max_rate:
                        if self.best_rating[self.food_cuisine_map[food]] > f:
                            self.best_rating[self.food_cuisine_map[food]] = f

    def highestRated(self, cuisine: str) -> str:
        return self.best_rating[cuisine]


# food_ratings = FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"],
#                            ["korean", "japanese", "japanese", "greek", "japanese", "korean"],
#                            [9, 12, 8, 15, 14, 7])
#
# print(food_ratings.highestRated("korean"))
# print(food_ratings.highestRated("japanese"))
# food_ratings.changeRating("sushi", 16)
# print(food_ratings.highestRated("japanese"))
# food_ratings.changeRating("ramen", 16)
# print(food_ratings.highestRated('japanese'))

# food_ratings = FoodRatings(["cpctxzh","bryvgjqmj","wedqhqrmyc","ee","lafzximxh","lojzxfel","flhs"],["wbhdgqphq","wbhdgqphq","mxxajogm","wbhdgqphq","wbhdgqphq","mxxajogm","mxxajogm"],[15,5,7,16,16,10,13])
# food_ratings.changeRating("lojzxfel",1)
# print(food_ratings.highestRated("mxxajogm"))
# print(food_ratings.highestRated("wbhdgqphq"))
# print(food_ratings.highestRated("mxxajogm"))