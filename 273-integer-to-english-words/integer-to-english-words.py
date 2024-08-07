class Solution:
    def numberToWords(self, num: int) -> str:
        a = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        b = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        c = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        def helper(num: int) -> str:
            if num == 0:
                return "Zero"
            elif num < 10:
                return a[num]
            elif num < 20:
                return b[num - 10]
            elif num < 100:
                return c[num // 10] + ("" if num % 10 == 0 else " " + helper(num % 10))
            elif num < 1000:
                return a[num // 100] + " Hundred" + ("" if num % 100 == 0 else " " + helper(num % 100))
            elif num < 1000000:
                return helper(num // 1000) + " Thousand" + ("" if num % 1000 == 0 else " " + helper(num % 1000))
            elif num < 1000000000:
                return helper(num // 1000000) + " Million" + ("" if num % 1000000 == 0 else " " + helper(num % 1000000))
            else:
                return helper(num // 1000000000) + " Billion" + ("" if num % 1000000000 == 0 else " " + helper(num % 1000000000))

        if num == 0:
            return "Zero"
        else:
            return helper(num)
