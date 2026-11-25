class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        x = 0
        bits = bin(num2).count("1")

        # Take set bits from num1, starting from the highest bit
        for i in range(31, -1, -1):
            if bits > 0 and (num1 & (1 << i)):
                x |= (1 << i)
                bits -= 1

        # If more set bits are needed, take the lowest available bits
        for i in range(32):
            if bits > 0 and not (x & (1 << i)):
                x |= (1 << i)
                bits -= 1

        return x
