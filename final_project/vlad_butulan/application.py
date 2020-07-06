import tkinter
import tkinter.messagebox
from tkcalendar import Calendar, DateEntry
from backend import PrittyPrinter, Room, Room_Inventory, Client, Clients, My_Rooms_CM
from prettytable import PrettyTable
import logging
import yaml
import datetime

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, filename='logger.log', datefmt='%m/%d/%Y %I:%M:%S %p')

with My_Rooms_CM() as inventory:
    hotel_rooms = yaml.load(inventory, Loader=yaml.BaseLoader)
    logger.info('Rooms file successfuly loaded')

window = tkinter.Tk()
window.title("Hotel manager")
window.geometry("600x500+300+200")

first_frame=tkinter.Frame(window, width=600, height=500)
first_frame.grid(column=0, row=0)
second_frame=tkinter.Frame(window, width=600, height=500)
second_frame.grid(column=0, row=0)
third_frame=tkinter.Frame(window, width=600, height=500)
third_frame.grid(column=0, row=0)
fourth_frame=tkinter.Frame(window, width=600, height=500)
fourth_frame.grid(column=0, row=0)
fith_frame=tkinter.Frame(window, width=600, height=500)
fith_frame.grid(column=0, row=0)

def nice_display(fct):
    def inner(name, surname, age, address, check_in_date, check_out_date, room):
        client_tb = PrettyTable(["Name", "Reserved room", "Check-in", "Check-out", "Cost"])
        price = room_inventory.price[room] * (check_out_date - check_in_date).days
        client_tb.add_row([name+' '+surname, room, str(check_in_date), str(check_out_date), price])
        print(client_tb)
        return fct(name, surname, age, address, check_in_date, check_out_date, room)
    return inner

@nice_display
def check_in(name, surname, age, address, check_in_date, check_out_date, room):
    """function for any check-in"""
    client_id = clients.check_client(name, surname)
    if not client_id:
        client_id = clients.new_client(name, surname, age, address)
        logger.info('New client created: {} {}'.format(name, surname))
    avail_rooms = room_inventory.check_availability(room, [check_in_date, check_out_date])
    if len(avail_rooms) > 0:
        result = room_inventory.reserve(avail_rooms[0], client_id, [check_in_date, check_out_date])
        clients.reserve(avail_rooms[0], client_id, [check_in_date, check_out_date])
        price = room_inventory.price[room] * (check_out_date - check_in_date).days
        result += "\nTotal price is {}RON".format(price)
        logger.info('New {} reserved nr: {} by {} {}'.format(room, avail_rooms[0], name, surname))
        return result
    else:
        logging.warning('No {} available'.format(room))
        return "No {} available!".format(room)

def frame1_widgets():
    """welcome window"""

    message = tkinter.Message(first_frame, text="Welcome", width=100)
    message.place(relx=0.09, rely=0.01, relheight=0.15, relwidth=0.80)
    b1 = tkinter.Button(first_frame, text='Check in', command=lambda: switch_frame('checkin_page'))
    b1.place(relx=0.09, rely=0.15, relheight=0.12, relwidth=0.80)
    b2 = tkinter.Button(first_frame, text='Client profile', width=15, command=lambda: switch_frame('client_stats'))
    b2.place(relx=0.09, rely=0.30, relheight=0.12, relwidth=0.80)
    b3 = tkinter.Button(first_frame, text='Room availability', width=15, command=lambda: switch_frame('check_availability'))
    b3.place(relx=0.09, rely=0.45, relheight=0.12, relwidth=0.80)
    b4 = tkinter.Button(first_frame, text='Hotel details', width=15, command=lambda: switch_frame('hotel_stats'))
    b4.place(relx=0.09, rely=0.60, relheight=0.12, relwidth=0.80)
    b5 = tkinter.Button(first_frame, text = 'Quit', width=15, command=window.destroy)
    b5.place(relx=0.09, rely=0.75, relheight=0.12, relwidth=0.80)

def frame2_widgets():
    """check-in window"""
    
    def check_room():
        name = client_name.get()
        surname = client_surname.get()
        check_in_date = cal1.get_date()
        check_out_date = cal2.get_date()
        age = client_age.get()
        address = client_address.get()
        if single_room.get():
            resultat = check_in(name, surname, age, address, check_in_date, check_out_date, 'single_room')
            tkinter.messagebox.showinfo("Success", resultat)
        elif double_room.get():
            resultat = check_in(name, surname, age, address, check_in_date, check_out_date, 'double_room')
            tkinter.messagebox.showinfo("Success", resultat)
        else:
            tkinter.messagebox.showerror("Error", "No room selected")

    l1 = tkinter.Label(second_frame, text="Name")
    l1.grid(row=0, column=0, sticky=tkinter.E)

    l2 = tkinter.Label(second_frame, text="Surname")
    l2.grid(row=0, column=2, sticky=tkinter.E)

    l3 = tkinter.Label(second_frame, text="age")
    l3.grid(row=1, column=0, sticky=tkinter.E)

    l4 = tkinter.Label(second_frame, text="Address")
    l4.grid(row=1, column=2, sticky=tkinter.E)

    client_name=tkinter.StringVar()
    e1=tkinter.Entry(second_frame, textvariable=client_name, width=15)
    e1.grid(row=0,column=1)
 
    client_surname=tkinter.StringVar()
    e2=tkinter.Entry(second_frame, textvariable=client_surname, width=15)
    e2.grid(row=0,column=3)
 
    client_age=tkinter.StringVar()
    e3=tkinter.Entry(second_frame, textvariable=client_age, width=15)
    e3.grid(row=1,column=1)

    client_address=tkinter.StringVar()
    e3=tkinter.Entry(second_frame, textvariable=client_address, width=15)
    e3.grid(row=1,column=3)

    message = tkinter.Message(second_frame, text="Choose room:", width=100)
    message.grid(row=2, columnspan=2, sticky=tkinter.W)

    single_room = tkinter.IntVar()
    ch_btn1 = tkinter.Checkbutton(second_frame, text ="single room", variable=single_room)
    ch_btn1.grid(row=3, sticky=tkinter.W)

    double_room = tkinter.IntVar()
    ch_btn2 = tkinter.Checkbutton(second_frame, text ="double room", variable=double_room)
    ch_btn2.grid(row=3, column=1, sticky=tkinter.W)
 
    l5 = tkinter.Label(second_frame, text="Check-in date")
    l5.grid(row=4, column=0, sticky=tkinter.E)

    l6 = tkinter.Label(second_frame, text="Check-out date")
    l6.grid(row=4, column=2, sticky=tkinter.E)

    cal1 = DateEntry(second_frame, width=10, background='darkblue', foreground='white', borderwidth=2, year=2020)
    cal1.grid(row=4, column=1)

    cal2 = DateEntry(second_frame, width=10, background='darkblue', foreground='white', borderwidth=2, year=2020)
    cal2.grid(row=4, column=3)

    b1 = tkinter.Button(second_frame, text='Submit', width=15, command=check_room)
    b1.grid(row=5, column=2)
    b2 = tkinter.Button(second_frame, text='Back', width=15, command=lambda: switch_frame('start_page'))
    b2.grid(row=6, column=2)


def frame3_widgets():
    """ client details window"""

    def show_clients():
        list1.delete(0, tkinter.END)
        list1.insert(tkinter.END, ('ID', 'Name', 'Surname', "RoomNumber", "Check-In", "Check-Out"))
        for client in clients:
            for room_nr, period in client.reserved_room.items():
                list1.insert(tkinter.END, (client.user_id, client.client_details['name'], client.client_details['surname'], room_nr, period[0], period[1]))

    def show_client():
        if list1.curselection() and list1.curselection()[0] != 0:
            selected_tuple = list1.get(list1.curselection()[0])
            for client in clients:
                if client.user_id == selected_tuple[0]:
                    result = client.status()
            top = tkinter.Toplevel()
            top.title("Client details")
            text = tkinter.Text(top, borderwidth=3)
            text.grid(row=0, column=0, padx=2, pady=2)
            text.insert(tkinter.END, chars=result)
            text.see(tkinter.END)
        else:
            tkinter.messagebox.showerror("Error", "No client selected")

    list1=tkinter.Listbox(third_frame, height=6, width=50)
    list1.grid(row=0,column=0, rowspan=6, columnspan=10)

    sb1=tkinter.Scrollbar(third_frame)
    sb1.grid(row=0,column=10,rowspan=6)

    list1.configure(yscrollcommand=sb1.set)
    sb1.configure(command=list1.yview)

    b1 = tkinter.Button(third_frame, text='Show clients', width=15, command=show_clients)
    b1.grid(column=11, row=0)
    b2 = tkinter.Button(third_frame, text='Show details', width=15, command=show_client)
    b2.grid(column=11, row=1)
    b3 = tkinter.Button(third_frame, text='Back', width=15, command=lambda: switch_frame('start_page'))
    b3.grid(column=11, row=2)

def frame4_widgets():
    """room availability window"""

    def check_date():
        check_in_date = cal1.get_date()
        check_out_date = cal2.get_date()
        free_rooms = {}
        for room_type in ['single_room', 'double_room']:
            free_rooms.update({room_type:room_inventory.check_availability(room_type, [check_in_date, check_out_date])})
        result = ""
        for key, value in free_rooms.items():
            result += "Free rooms for {}: {}\n".format(key, len(value))
        tkinter.messagebox.showinfo("Check availability result", result)

    l1 = tkinter.Label(fourth_frame, text="Choose check-in date")
    l1.grid(row=0, column=0)

    l1 = tkinter.Label(fourth_frame, text="Choose check-out date")
    l1.grid(row=0, column=2)

    cal1 = DateEntry(fourth_frame, width=12, background='darkblue', foreground='white', borderwidth=2, year=2020)
    cal1.grid(row=1, column=0)

    cal2 = DateEntry(fourth_frame, width=12, background='darkblue', foreground='white', borderwidth=2, year=2020)
    cal2.grid(row=1, column=2)

    b1 = tkinter.Button(fourth_frame, text='Check', width=15, command=check_date)
    b1.grid(row=1, column=3)

    b2 = tkinter.Button(fourth_frame, text='Back', width=15, command=lambda: switch_frame('start_page'))
    b2.grid(row=2, column=3)

def frame5_widgets():
    """hotel stats window"""

    def show_rooms():
        rooms_tb = PrettyTable(["Room nr.", "Room type", "Reserved by", "Check-in", "Check-out"])
        for room in room_inventory:
            rooms_tb.add_row([room.room_details['nr'], room.room_details['type'], "", "", ""])
            if len(room.in_use):
                period_in = []
                period_out = []
                client_in = []
                for user_id, period in room.in_use.items():
                    client_in = clients.get_user(user_id)
                    period_in = period[0]
                    period_out = str(period[1])
                    rooms_tb.add_row(["", "", client_in, period_in, period_out])
            else:
                client_in = '-Free-'
                period_in = '-NA-'
                period_out = '-NA-'
                rooms_tb.add_row(["", "", client_in, period_in, period_out])
        output.delete('1.0', tkinter.END)
        output.insert(tkinter.END, chars=rooms_tb)
        output.see(tkinter.END)
        rooms_tb.clear()

    output = tkinter.Text(fith_frame, height=20, width=70)
    output.grid(row=0, column=0, padx=2, pady=2)

    b1 = tkinter.Button(fith_frame, text='Show rooms', width=15, command=show_rooms)
    b1.grid(column=0, row=1)
    b2 = tkinter.Button(fith_frame, text='Back', width=15, command=lambda: switch_frame('start_page'))
    b2.grid(column=0, row=2)

def switch_frame(to_page):
    frames = {}
    frames['start_page'] = first_frame
    frames['checkin_page'] = second_frame
    frames['client_stats'] = third_frame
    frames['check_availability'] = fourth_frame
    frames['hotel_stats'] = fith_frame
    for page in frames.keys():
        if page != to_page:
            frames[page].grid_forget()
    frames[to_page].grid(column=0, row=0)

frame1_widgets()
frame2_widgets()
frame3_widgets()
frame4_widgets()
frame5_widgets()
switch_frame('start_page')

client1 = Client(1, {'name':'Pandele', 'surname':'Piron', 'age':'110', 'address':'Vacantei Mari 21'}, {})
clients = Clients()
clients.append(client1)

room_inventory = Room_Inventory([])
for key, value in hotel_rooms.items():
    key = Room(value, {})
    room_inventory.append(key)

date1 = datetime.date.today()
date2 =date1 + datetime.timedelta(days=3)
clients.reserve('1', 1, [date1, date2])
room_inventory.reserve('1', 1, [date1, date2])

window.mainloop()
