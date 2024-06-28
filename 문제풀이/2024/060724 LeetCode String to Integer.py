class Solution:
    def myAtoi(self, s: str) -> int:
        pos = True
        reading = False
        num = 0
        for char in s:
            if not reading and char in [' ', '\t']:
                continue
            if not reading and char in ['-', '+']:
                pos = char == '+'
                reading = True
                continue
            if not reading and char.isdigit():
                reading = True
                num += int(char)
                continue
            if reading and char.isdigit():
                num *= 10
                num += int(char)
                continue
            else:
                if not pos:
                    num *= -1
                return sorted([-2**31, num, 2**31 - 1])[1]

        if not pos:
            num *= -1
        return sorted([-2**31, num, 2**31 - 1])[1]

    # def myAtoi(self, s: str) -> int:
    #     pos = True
    #     reading = False
    #     num = 0
    #     for char in s:
    #         match char:
    #             case " " | '\t' if not reading:
    #                 continue
    #             case "-" | "+" if not reading:
    #                 reading = True
    #                 pos = char == "+"
    #             case _ if char.isdigit():
    #                 reading = True
    #                 num *= 10
    #                 num += int(char)
    #             case _:
    #                 if not pos:
    #                     num *= -1
    #                 return sorted([-2**31, num, 2**31 - 1])[1]
    #     if not pos:
    #         num *= -1
    #     return sorted([-2**31, num, 2**31 - 1])[1]
