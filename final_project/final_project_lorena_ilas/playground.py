from application import *
import gmplot
import urllib.parse
import webbrowser
import os
import pathlib

s = Login()
logged_in = False

Stop = False

if Stop is False:
    tasks = (input('What would you like to do? enter [Login], or [quit]'))

    if tasks == 'Login':
        LoginInfoUser = (input('Please enter Username'))
        LoginInfoPassword = (input('Please enter Password'))
        logged_in = s.check(LoginInfoUser, LoginInfoPassword)
    else:
        print("See you later!")
        Stop = True

if logged_in:
    current_user = s.get_current_user()
    print(s)
    if current_user.user_type == "Client":
        customer_menu()

    else:

        addresses = ConvertAddress()

        addresses.append('Pasteur 61, Cluj-Napoca, Romania')
        addresses.append('Sobarilor 38, Cluj-Napoca, Romania')
        addresses.append('Traian 21, Cluj-Napoca, Romania')
        addresses.append('Ferdinand 26, Cluj-Napoca, Romania')
        addresses.append('Calea Turzii 227, Cluj-Napoca, Romania')

        print("\n PRINT Addresses: \n")
        print(addresses)

        lat = []
        lng = []

        for address in addresses:
            url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) + '?format=json'

            response = requests.get(url).json()
            print(response[0]["lat"])
            print(response[0]["lon"])
            lat.append(float(response[0]["lat"]))
            lng.append(float(response[0]["lon"]))

        gmapOne = gmplot.GoogleMapPlotter(46.7566149, 23.5811587, 14)
        gmapOne.scatter(lat, lng, 'red', size=50, marker=False)
        gmapOne.plot(lat, lng, "blue", edge_width=2.5)
        gmapOne.draw("map.html")

        map_path = os.path.abspath("map.html")
        map_url = pathlib.Path(map_path).as_uri()
        webbrowser.open_new(map_url)

        distances = []
        grouped_points = [(o_lat, o_lng) for o_lat, o_lng in zip(lat, lng)]

        for current_point, next_point in zip(grouped_points, grouped_points[1:]):
            distance = AddressManager.calculate_distance(current_point, next_point)
            distances.append(distance)

        increased_price = AddressManager.price_increase_generator(distances)
        print(f"As a driver you should get  {increased_price:.2f} euro")
