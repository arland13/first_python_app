import json
import random

class Car():

    wheels = 4

    def __init__(self,id, brand,model,year,colour = "Black",speed=0,fuel=100,health=100,distance=0,max_speed=220):
        self.id = id
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed
        self.fuel = fuel
        self.health = health
        self.distance = distance
        self.max_speed = max_speed
        self.colour = colour
class Car_mechanics:

    def __init__(self,filename="Cars_json"):
        self.filename = filename
        self.cars = []
        self.money = 100000000000
        self.pair_cost = 200000

    def add_car(self):
        if not self.cars:
            new_id = 1
        else:
                new_id = max(c.id for c in self.cars)+1

        car = Car(new_id, brand_input, model_input, year_input)
        self.cars.append(car)
        mechanics.save_car()

    def list_cars(self):
           
           for c in self.cars:
               print(f"Car id    : {c.id}")
               print(f"Brand     : {c.brand}")
               print(f"Model     : {c.model}")
               print(f"Year      : {c.year}")
               print(f"Speed     : {c.speed} km/h")
               print(f"Fuel      : {c.fuel} L")
               print(f"Health    : {c.health}")
               print(f"Distance  : {c.distance} km")
               print(f"Max Speed : {c.max_speed}")
               print(("_")*20)

    def search_car(self):

        for c in self.cars:
            if search_input == c.id:
                print(f"Brand     : {c.brand}")
                print(f"Model     : {c.model}")
                print(f"Year      : {c.year}")
                print(f"Speed     : {c.speed} km/h")
                print(f"Fuel      : {c.fuel} L")
                print(f"Health    : {c.health}")
                print(f"Distance  : {c.distance} km")
                print(f"Max Speed : {c.max_speed}")

    def acc_car(self,car_id,acc_value):

        for c in self.cars:
            if c.id == car_id:
                c.speed += acc_value

                if c.speed >= c.max_speed:
                    c.speed = c.max_speed
                    print("reached speed limit (220 km/h)")

                print(f"Car_id {c.id}({c.brand} {c.model}) New speed: {c.speed} km/h")
                return True

        print("Car id not found")
        return False

    def brake_car(self,car_id,brake_value):

        for c in self.cars:
            if car_id == c.id:
                c.speed -= brake_value

                if c.speed <= 0:
                    c.speed = 0
                    print("car already stopped!")

                mechanics.save_car()
                print(f"Car_id {c.id} ({c.brand} {c.model}) New speed: {c.speed} km/h")
                return True
            
        print("car id not found!")
        return False
        
    def distance_car(self,car_id,dist_value):

        for c in self.cars:
            max_distance = c.fuel * 10

            if c.fuel == 0:
                c.fuel = 0
                print("fuel is empty, cant travel anymore!")
                return
             
            if c.id == car_id:
                if dist_value > max_distance:
                    print(f"can't travel that far, max distance = {max_distance}")
                    return None

                c.distance  += dist_value
                fuel_lost = dist_value//10
                c.fuel -= fuel_lost

                health_lost = dist_value//50
                c.health -= health_lost
                print("car has been drived!")
                print(f"Car_id {c.id} ({c.brand} {c.model}, mileage: {c.distance}, fuel: {c.fuel}, health: {c.health})")
                return True
            
        print("car id not found!")
        return False
    
    
    def repair_car(self,car_id):

        for c in self.cars:
            if c.id == car_id:
                new_health = c.health + 20
                if new_health > 100:
                    c.health = 100
                    print("in perfect condition!")
                    print(f"Car {c.id} ({c.brand} {c.model}, Health : {c.health})")
                    return True
                else:
                    c.health += 20
                    print("car has repaired!")
                    print(f"Car_id {c.id} ({c.brand} {c.model}, Health : {c.health})")
                    return True
            
        print("car id not found")
        return False
    
    def refuel(self,car_id):

        for c in self.cars:
            if c.id == car_id:
                if c.fuel + 30 > 100:
                    c.fuel = 100
                    print("fuel is full, ready to go!")
                    print(f"Car{c.id} ({c.brand} {c.model}), fuel = {c.fuel} ")
                    return True
                else:
                    c.fuel +=30 
                    print("fuel has been filled, ready to go!")
                    print(f"Car {c.id} ({c.brand} {c.model}, fuel = {c.fuel})")
                    return True

        print("car id not found")
        return False
    
    def get_age(self,car_id):
        for c in self.cars:
            if c.id == car_id:
                age_cars = 2025 - c.year
                print(f"Car {c.id} ({c.brand} {c.model})")
                print(f"age = {age_cars} years")

    def car_crash(self,car_id):
        for c in self.cars:
            if c.id == car_id:
                c.health = max(0, c.health - random.randint(1,100))
                print(f"Car {c.id} ({c.brand} {c.model}), has been crash")
                print(f"Health : {c.health}")

    def car_upgrade(self,car_id):
        for c in self.cars:
            if c.id == car_id:
                c.max_speed += 50
                print(f"Car {c.id} ({c.brand} {c.model}, has been upgraded!)")
                print(f"Max Speed : {c.max_speed}")

    def car_paint(self,car_id,colour_input):
        for c in self.cars:
            if c.id == car_id:
                c.colour = colour_input
                print(f"Car {c.id} ({c.brand} {c.model}, has been painted)")
                print(f"Colour : {c.colour}")

    def car_race(self,car_id1,car_id2):
        for c in self.cars:
            if c.id == car_id1:
                print(f"Car ID {c.id}, {c.brand} {c.model}. speed = {c.speed}")
        for c in self.cars:
            if c.id == car_id2:
                print(f"Car ID {c.id}, {c.brand} {c.model}. speed = {c.speed}")

    def car_service(self,car_id):
        for c in self.cars:
            if c.id == car_id:
                self.money -= self.pair_cost
                money = f"{self.money:,.2f}"
            if c.id == car_id:
                c.health = 100
                c.fuel = 100
                print(f"Car {c.id} ({c.brand} {c.model}, has been restored)")
                print(f"Account Balance : Rp{money} ")

    def save_car(self):

        with open(self.filename, "w") as file:
            data = []

            for c in self.cars:
                data.append({
                    "id": c.id,
                    "brand": c.brand,
                    "model": c.model,
                    "year" : c.year,
                    "speed" : c.speed,
                    "fuel" : c.fuel,
                    "health" : c.health
                })
            json.dump(data, file)
            print("car entry updated!")

    def load_car(self):

        try:
            with open(self.filename, "r") as file:
                content = file.read().strip()

                if not content:
                    self.cars = []
                    return

                data = json.loads(content)

                self.cars = []
                for item in data:
                    car = Car(item["id"], item["brand"], item["model"], item["year"], item["speed"], item["fuel"], item["health"])
                    self.cars.append(car)

        except FileNotFoundError:
            self.cars = []

        print("acces curent task!")

if __name__ == "__main__":
    mechanics = Car_mechanics()
    mechanics.load_car()
    print("'honk' to Beep! Beep!")
    print("'crash' when you feel angry!!")
    print("'upgrade' my car, my precious")
    print("gonna 'paint' my car to look cooler")
    print("'let 'race' to prove who is the best")
    print("let 'service' the car")
    print("test change commit")

    while True:
        user_input = input("input command: (add/list/search/acc/brake/dist/repair/refuel/age)").strip().lower()
        if user_input == "add":

            brand_input = input("input brand of the car: ")
            model_input = input("input model of the car: ")

            while True:
                try:
                    year_input = int(input("input year of the car: "))
                    print("car inputed!")
                    break
                except ValueError:
                    print("invalid year!")
            mechanics.add_car()
        
        elif user_input == "list":

            if not mechanics.cars:
                print("no car entry yet!")
                continue

            mechanics.list_cars()

        elif user_input == "search":
            
            if not mechanics.cars:
                print("no car entry yet!")
                continue

            try:
                search_input = int(input("input car_id you want to look: "))
            except ValueError:
                print("invalid id!")
            mechanics.search_car()
        
        elif user_input == "acc":

            if not mechanics.cars:
                print("no car entry yet!")
                continue

            while True:
                try:
                    car_id = int(input("input car_id you want to accelerate: "))
                    break
                except ValueError:
                    print("Invalid ID! Must be a number.")

            while True:
                try:
                    acc_value = int(input("input accelerating value: "))
                    break
                except ValueError:
                    print("Invalid value! Must be a number.")

            mechanics.acc_car(car_id, acc_value)

        elif user_input == "brake":

            if not mechanics.cars:
                print("no car entry yet!")
                continue

            while True:
                try:
                    car_id = int(input("input car_id you want to slow down: "))
                    break
                except ValueError:
                    print("invalid id, must be a number!")
            
            while True:
                try:
                    brake_value = int(input("input decceleration value: "))
                    break
                except ValueError:
                    print("invalid value, please input a number!")

            mechanics.brake_car(car_id,brake_value)
        
        elif user_input == "dist":

            if not mechanics.cars:
                print("no car entry yet!")
                continue

            while True:
                try:
                    car_id = int(input("input car_id you want to drive: "))
                    break
                except ValueError:
                    print("invalid id, please input a number!")
            
            while True:
                try:
                    dist_value = int(input("how many km that car travel?: "))
                    break
                except ValueError:
                    print("invalid value, please input a number!")

            mechanics.distance_car(car_id,dist_value)

        elif user_input == "repair":

            if not mechanics.cars:
                print("no car entry yet!")
                continue

            while True:
                try:
                    car_id = int(input("car_id you want to repair: "))
                    break
                except ValueError:
                    print("invalid id, please input a number")

            mechanics.repair_car(car_id)

        elif user_input == "refuel":

            if not mechanics.cars:
                print("no cat entry yet!")
                continue

            while True:

                try:
                    car_id = int(input("car_id you want to refuel: "))
                    break
                except ValueError:
                    print("invalid id, please input a number")

            mechanics.refuel(car_id)
        
        elif user_input == "age":
            if not mechanics.cars:
                print("no car entry yet!")
                continue

            while True:
                try:
                    car_id = int(input("input car_id: "))
                    break
                except ValueError:
                    print("invalid id, please input a number")

            mechanics.get_age(car_id)

        elif user_input == "honk":
            print("Beep! Beep!")

        elif user_input == "crash":
            if not mechanics.cars:
                print("no car entry yet!")
                continue
             
            while True:
                try:
                    car_id = int(input("input car_id: "))
                    break
                except ValueError:
                    print("invalid id, please input a number")

            mechanics.car_crash(car_id)

        elif user_input == "upgrade":
            if not mechanics.cars:
                print("no car entry yet!")
                continue
             
            while True:
                try:
                    car_id = int(input("input car_id: "))
                    break
                except ValueError:
                    print("invalid id, please input a number")

            mechanics.car_upgrade(car_id)

        elif user_input == "paint":
            if not mechanics.cars:
                print("no car entry yet!")
                continue
            
            while True:
                try:
                    car_id = int(input("input car_id: "))
                    break
                except ValueError:
                    print("invalid id, please input a number")

            colour_input = input("input colour: ")

            mechanics.car_paint(car_id,colour_input)

        elif user_input == "race":
            if not mechanics.cars:
                print("no car entry yet!")
                continue

            while True:
                try:
                    car_id1 = int(input("input car_id: "))
                    break
                except ValueError:
                    print("invalid id, please input a number")

            while True:
                try:
                    car_id2 = int(input("input car_id: "))
                    break
                except ValueError:
                    print("invalid id, please input a number")

            mechanics.car_race(car_id1,car_id2)

        elif user_input == "service":
            if not mechanics.cars:
                print("no car entry yet!")
                continue

            while True:
                try:
                    car_id = int(input("input car_id: "))
                    break
                except ValueError:
                    print("invalid id, please input a number")
            
            mechanics.car_service(car_id)