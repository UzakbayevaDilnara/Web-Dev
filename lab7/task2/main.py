from models import Car, Bike

def main():
    car1 = Car("Toyota", 2020, 120, 4)
    bike1 = Bike("BMX", 2022, 40, "sport")

    vehicles = [car1, bike1]

    for v in vehicles:
        print(v)              
        print(v.move())      
        print(v.stop())
        print("-----")

if __name__ == "__main__":
    main()
