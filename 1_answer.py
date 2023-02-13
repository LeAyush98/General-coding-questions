class Jar:
    N = 10
    K = 5
    def __init__(self, M) -> None:
        if M > Jar.N: print("INVALID INPUT")
        else: self.M = M
    def remaining(self):
        Jar.N -= self.M  
        if self.M > Jar.K:
            Jar.N += self.M  
        return (Jar.N)
M = int(input())    

jar = Jar(M)


if M < Jar.N:
    print(f"NUMBER OF CANDIES SOLD: {M}")
    print(f"NUMBER OF CANDIES REMAINING: {jar.remaining()}")
else: print(f"NUMBER OF CANDIES REMAINING: {Jar.N}")  
