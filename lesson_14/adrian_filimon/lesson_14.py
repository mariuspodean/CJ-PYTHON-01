"""
Trucks drive around 500km a day and can work 5-6 days a week
1km is payed for 0.85euro and everything after 2500km a week is payed with 1euro
Make your class in such a way so that you can calculate the km payed and also the extra
bonus for each km over 2500 km and the total income for 1 week.
BONUS : if you know that 1L of Diesel costs 1,23E and a truck's consumption is 30L/100KM, how much does a
payed km cost, with and without bonus?
"""


class PaymentMixin:

    def __init__(self, *args):
        class_name = type(self).__name__
        print(f'{class_name} initialized.')

        return super().__init__(*args)

    def calculate_km_payed(self):
        base_km = 10000
        diesel_price = 1.23
        if self.truck_km <= 10000:
            km_payed = self.truck_km * 0.85
            km_total = self.truck_km
            diesel_fueled = 0.30 * km_total
            diesel_cost = diesel_price * diesel_fueled
            km_driven_with_outcome = km_payed - diesel_cost
            print(f"These are the trucks km driver in total {km_total}")
            print(f"These are payed km before diesel {km_payed}")
            print(f"This is the diesel cost {diesel_cost}")
            print(f"This are KM driven with outcome {km_driven_with_outcome}")


            # return self.truck_km
        else:
            km_total = self.truck_km
            bonus_km = km_total - base_km
            bonus_pay = bonus_km * 1.1     # 2200
            final_km_pay = base_km *  0.85 + bonus_pay
            diesel_fueled = 0.30 * km_total
            diesel_cost = diesel_price * diesel_fueled
            km_driven_with_outcome = final_km_pay - diesel_cost
            print(f"These are the trucks km driver in total {km_total}")
            print(f"These are payed km before diesel {final_km_pay}")
            print(f"This is the diesel cost {diesel_cost}")
            print(f"This are KM driven with outcome {km_driven_with_outcome}")


            # return self.truck_km

    def calculate_days_worked(self):
        km = self.truck_km
        days = self.days_worked
        print(km / days)



# din final_pay  - diesel_price * (0,30 * km_driven)= km_driven_with_outcome
#



class Truck(PaymentMixin):

    def __init__(self, truck_nr, truck_km, days_worked):
        self._truck_nr = truck_nr
        self.truck_km = truck_km
        self.days_worked = days_worked

    @property
    def truck_nr(self):
        return self._truck_nr


CJ33PYT = Truck("cj33pyt", 12000, 20)
CJ22PYT = Truck("cj20pyt", 10000, 20)

CJ33PYT.calculate_km_payed()
print("**********************************")
CJ22PYT.calculate_km_payed()