class Solution:
    def intToRoman(self, num: int) -> str:
        integers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        answer = []
        i = 0
        while num:
            answer.append((num // integers[i]) * romans[i])
            num %= integers[i]
            i += 1
        return "".join(answer)