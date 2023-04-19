class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1 and flowerbed[0] == 0 and n < 2:
            return True

        index = 0
        while index < len(flowerbed):
            if index == 0 and flowerbed[index] == 0 and flowerbed[index + 1] == 0:
                flowerbed[index] = 1
                n-=1
            elif index == len(flowerbed)-1 and flowerbed[index] == 0 and flowerbed[index - 1] == 0:
                flowerbed[index] = 1
                n-=1
            elif flowerbed[index] == 0 and index-1 >= 0 and index + 1 < len(flowerbed):
                if flowerbed[index-1] == 0 and flowerbed[index+1] == 0:
                    flowerbed[index] = 1
                    n-=1
            index += 1
        return n <= 0