class Aircraft(object):
    def __init__(self, prod_year, max_ceiling, max_speed, country, lifetime):
        self.prod_year = prod_year
        self.max_ceiling = max_ceiling
        self.max_speed = int(max_speed.strip(r'km/h'))
        self.country = country
        self.lifetime = lifetime

    @staticmethod
    def class_info():
        print("Class object named 'Aircraft' which contains 5 attributes: year of fabrication, maximum ceiling, maximum speed, country of origin, and lifetime")

    def in_use(self):
        if 2020 - self.prod_year < self.lifetime:
            print("The aircraft is still in use")
        else:
            print("The aircraft is retired")

class Plane(Aircraft):
    def __init__(self, name, plane_type, climb_rate, prod_year, max_ceiling, max_speed, country, lifetime):
        self.name = name
        self.plane_type = plane_type
        self.climb_rate = climb_rate
        super().__init__(prod_year, max_ceiling, max_speed, country, lifetime)

    def plane_era(self):
        if self.prod_year < 1939:
            print("Pre-war era plane!")
        elif 1939 <= self.prod_year <= 1945:
            print("Second World War era plane!")
        elif 1945 < self.prod_year < 1960:
            print("Post war era plane!")
        elif 1960 <= self.prod_year <= 1989:
            print("Cold War era plane!")
        else:
            print("Modern era plane!")

    def speed_classification(self):
        if self.max_speed >= 1000:
            print("Supersonic plane")
        elif 1000 > self.max_speed > 700:
            print("Transonic plane")
        else:
            print("Subsonic plane")

print("\nAdding instance P51:")
P51 = Plane('Mustang', 'fighter', '18.2m/s', 1940, '12700m', '650km/h', 'USA', 30)
P51.class_info()
P51.plane_era()
P51.in_use()
P51.speed_classification()

print("\nAdding instance mig15:")
mig15 = Plane("Fagot", 'fighter', "32.5m/s", 1950, "15500m", "975km/h", "Russia", 50)
mig15.plane_era()
mig15.in_use()
mig15.speed_classification()

print("\nAdding instance Airbus:")
airbus380 = Plane("Airbus 380", 'passanger plane', '15m/s', 2005, '13000m', '940km/h', 'France', 50)
airbus380.plane_era()
airbus380.in_use()
airbus380.speed_classification()

print("\nAdding instance Spitfire:")
spitfire = Plane("Spitfire", "fighter", "23m/s", 1939, "10400m", "650km/h", "UK", 10)
spitfire.plane_era()
spitfire.in_use()
spitfire.speed_classification()

print("\nAdding instance C130:")
c130 = Plane("Hercules", "transport", "10m/s", 1962, "9300m", "640km/h", "USA", 75)
c130.plane_era()
c130.in_use()
c130.speed_classification()