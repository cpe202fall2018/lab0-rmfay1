def weight_on_planets():
   # write your code here
   weight = int(input("What do you weigh on Earth? "))

   print("\n\nOn Mars you would weigh", weight * 0.38, "pounds.")
   print("On Jupiter you would weigh", weight * 2.34, "pounds.")
   
   
if __name__ == '__main__':
   weight_on_planets()