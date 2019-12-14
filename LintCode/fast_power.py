class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # write your code here
        res = 1
        while(n > 0):
            if n % 2 != 0:
                res *= a % b
            a *= (a%b)
            n = int(n / 2)
        
        return res % b