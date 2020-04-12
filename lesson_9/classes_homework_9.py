class TvSet(object):
    def __init__(self, brand, device_type, size, manufacture_date, energy_consumed, usb_interfaces, hdmi_interfaces,
                 rj_45, wifi):
        self.brand = brand
        self.type = device_type
        self.size = size
        self.manufacture_date = manufacture_date
        self.energy_consumed = energy_consumed
        self.usb_interfaces = usb_interfaces
        self.hdmi_interfaces = hdmi_interfaces
        self.rj_45 = rj_45
        self.wifi = wifi

    def can_be_placed(self):
        if int(self.size) < 20:
            return f"Due to the size, {self.size} inch, {self.brand} {self.type} is recomandated " \
                   f"to be placed in " \
                   f"small places like kitchen"
        elif int(self.size) < 80:
            return f"Due to the size, {self.size} inch, {self.brand} {self.type} is recomandated " \
                   f"to be placed in " \
                   f"medium places like rooms with 6 by 6 meters"
        return f"Due to the size, {self.size} inch, {self.brand} {self.type} is recomandated " \
               f"to be placed in medium " \
               f"places" \
               f" like rooms which exceed 6 by 6 meters "

    def is_it_smart(self):
        if self.rj_45 or self.wifi:
            return f"{self.brand} {self.type} is a smart device"
        return f"{self.brand} {self.type} is not a smart device"


class Monitor(TvSet):
    def __init__(self, brand, device_type, size, manufacture_date, energy_consumed, usb_interfaces, hdmi_interfaces,
                 rj_45, wifi,
                 touch_screen):
        self.touch_screen = touch_screen
        super().__init__(brand, device_type, size, manufacture_date, energy_consumed, usb_interfaces, hdmi_interfaces,
                         rj_45, wifi)

    def description(self):
        return f'{self.brand} {self.type} '

    def energy_consum_class(self):
        if int(self.energy_consumed) < 32:
            return f"{self.brand} {self.type} is a class A++ device"
        elif int(self.energy_consumed) < 50:
            return f"{self.brand} {self.type} is a class A+ device"
        elif int(self.energy_consumed) < 100:
            return f"{self.brand} {self.type} is a class A device"
        return f"{self.brand} {self.type} is a class B or less device"


dell_tv = TvSet('Dell', 'D19', 19, 2019, 19, 4, 2, True, True)
samsung_tv = TvSet('Samsung', 'S40', 40, 2020, 40, 2, 3, False, False)
lenovo_tv = TvSet('Lenovo', 'L32', 32, 2020, 32, 13, 3, True, False)
toshiba_tv = TvSet('Toshiba', 'T100', 100, 2017, 100, 2, 3, False, False)
toshiba_monitor = Monitor('Toshiba', 'T19', 19, 2018, 19, 3, 4, True, True, True)
hp_monitor = Monitor('HP', 'Express', 140, 2020, 70, 3, 4, True, True, False)

print(dell_tv.is_it_smart())
print(samsung_tv.is_it_smart())
print(lenovo_tv.is_it_smart())
print(toshiba_monitor.is_it_smart())
print(toshiba_tv.can_be_placed())
print(toshiba_monitor.can_be_placed())
print(toshiba_monitor.description())
print(toshiba_monitor.energy_consum_class())
print(hp_monitor.energy_consum_class())
