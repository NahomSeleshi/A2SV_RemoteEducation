from sortedcontainers import SortedList
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_dict = defaultdict(list)
        self.cuisine_dict = defaultdict(SortedList)
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_dict[food] = [rating, cuisine]
            self.cuisine_dict[cuisine].add([-rating, food])

    def changeRating(self, food: str, newRating: int) -> None:
        cur_rating, cur_cuisine = self.food_dict[food]
        self.food_dict[food] = [newRating, cur_cuisine]
        self.cuisine_dict[cur_cuisine].remove([-cur_rating, food])
        self.cuisine_dict[cur_cuisine].add([-newRating, food])

       
    def highestRated(self, cuisine: str) -> str:
        return self.cuisine_dict[cuisine][0][1]
                    
                    

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)