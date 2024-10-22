class Car:
    def __init__(self, modelname, year, mileagekmpl):
        self.modelname = modelname
        self.year = year
        self.mileagekmpl = mileagekmpl
    
    def output(self):
        print("The", self.year, self.modelname, "is the newest car on the market with the most demanded features. It can go up to", self.mileagekmpl, "kmpl")

BMW = Car("Series 3", 2024, 200)

BMW.output()