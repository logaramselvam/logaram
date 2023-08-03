class movie:
    def __init__(self, first, second, moviedirector):
        self.firstpart = first
        self.secondpart = second
        self.director = moviedirector


obj1 = movie("Adhipurush", "methipurush", "subikyadhav")
obj2 = movie("vadachennai.1", "vadachennai-2(anbuvin ezhuchi)", "vetrimaran")


print(obj1)
print("first part -", obj1.firstpart)
print("second part -", obj1.secondpart)
print("director -", obj1.director, "\n")
print("---------------------------")


print(obj2)
print("first part -", obj2.firstpart)
print("second part -", obj2.secondpart)
print("director - ", obj2.director, "\n")
print("---------------------------")
