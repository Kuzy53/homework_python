class Matrix():
    def __init__(self, m):
        n = 1
        for i in range(1, len(m)):
            if len(m[0]) == len(m[i]):
                n += 1
        if n == len(m):
            self.m = m
        else:
            print("Не Решаемо!!!")
        self.m = m
    def transpose(self):
        new_m = [[] for _ in self.m [0]]
        for i in range(len(self.m[0])):
            for j in range(len(self.m)):
                new_m[i].append(self.m[j][i])
        self.m = new_m
        return self.m

m1 = Matrix([[5, 8, 9], [2, 6, 1], [3, 3, 5]])
print(m1.transpose())