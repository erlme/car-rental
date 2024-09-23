header ={
    'cars_header' : ['Car ID','Name','Seat','Type','Price','Status'],
    'rent_header' : ['Rent ID','Customer ID','Car ID','Duration','Price','Total','Rent Status'],
    'cust_header' : ['Customer ID', 'Name','NIK','Phone No']
}

menu ={
    '1':'1. Display Data',
    '2':'2. Car Management',
    '3':'3. Rental Management',
    '4':'4. Customer Management',
    'x':'x. Exit'
}

show_menu={
    'a' : 'Show Cars',
    'b' : 'Show Rents',
    'c' : 'Show Customers',
    'x' : 'To Main Menu'
}

cars_menu={
    'a' : 'Add Car Data',
    'b' : 'Update Car Data',
    'c' : 'Delete Car Data',
    'x' : 'To Main Menu'
}

cars_status={
    'a':'available',
    'r':'rented',
    'm':'maintenance'
}

cars_filter={
    '4s' : 'Four Seat Car',
    '5s' : 'Five Seat Car',
    '7s' : 'Seven Seat Car',
    'mbs' : 'Mini Bus',
    'rt' : 'regular',
    'pt' : 'premium',
    '500ap' : 'Rent Price above 500000',
    '500bp' : 'Rent Price below 500000',
    'a':'available',
    'r':'rented',
    'm':'maintenance'
}

rent_menu={
    'a' : 'Create New Rent',
    'b' : 'Return Rented Car',
    'x' : 'To Main Menu'
}

cust_menu={
    'a': 'Create New Customer',
    'b': 'Update Customer Status',
    'c': 'Delete Customer Data',
    'x': 'To Main Menu'
}

rent_status={
    'p':'paid',
    'f':'finished'
}

cars_data = {'T71RA':{'name':'Toyota Avanza','seat':7,'type':'regular','price':300000,'status':'available'},
             'T72RA':{'name':'Toyota Avanza','seat':7,'type':'regular','price':300000,'status':'maintenance'},
             'H53RH':{'name':'Honda HRV','seat':5,'type':'regular','price':400000,'status':'available'},
             'H54RC':{'name':'Honda City','seat':4,'type':'regular','price':350000,'status':'maintenance'},
             'T75RR':{'name':'Toyota Rush','seat':7,'type':'regular','price':350000,'status':'maintenance'},
             'T76RV':{'name':'Toyota Veloz','seat':7,'type':'regular','price':350000,'status':'available'},
             'T77PI':{'name':'Toyota Innova','seat':7,'type':'premium','price':700000,'status':'available'},
             'T58PA':{'name':'Toyota Alphard','seat':5,'type':'premium','price':2000000,'status':'maintenance'},
             'M79PP':{'name':'Mitsubishi Pajero','seat':7,'type':'premium','price':1200000,'status':'available'},
             'T1410RH':{'name':'Toyota Hiace','seat':14,'type':'regular','price':1500000,'status':'available'}
            }
rent_data = {}
cust_data = {'E030896A1':{'name':'Erlangga','nik':'7551120308960002','phone':'082188479983'}}

def display_menu(): #Display the Main Menu
    print('\nWelcome to The CAR RENT-ERL- ;)\n')
    print('Select menu to begin:')
    for menu_key,menu_val in menu.items(): # Loop through menu dict
        print(f'{menu_key}: {menu_val}') # to print all the menu
    choose_menu = input('Enter the number of the menu you want to run: ')
    return choose_menu

def display_show(): # Menu 1 Display Data
    print('\nDISPLAY\n')
    print('Select menu to proceed:')
    for menu_key,menu_val in show_menu.items(): # Loop through menu dict
        print(f'{menu_key}: {menu_val}') # to print all the menu
    choose_show = input('Enter the menu you want to run: ').lower()
    return choose_show

def display_cars(cars_storage): # 1.a. List of Cars
    print(('-'*5)+'LIST OF CARS'+('-'*5))
    for h in header['cars_header']: # Loop through header dict
        print(f'{h:<20}', end=' ') # To print cars header
    print('')
    print('-'*100)
    for cars_key,cars_val in cars_storage.items():
        print(f'{cars_key:<20}', end=' ')
        print(f"{cars_val['name']:<20}", end=' ')
        print(f"{cars_val['seat']:<20}", end=' ')
        print(f"{cars_val['type']:<20}", end=' ')
        print(f"{cars_val['price']:<20}", end=' ')
        print(f"{cars_val['status']:20}")
    print('')

def filsor_cars():
    while True :
        filsor = input('Apply (f)ilter or (s)ort the table? (x) to back to main menu: ').lower()
        if filsor == 'f':
            print('\nLIST OF FILTER')
            for filter_key,filter_val in cars_filter.items(): # Loop through menu dict
                print(f'{filter_key:<5}: {filter_val}')
            filter_select = input('Select available filter: ').lower()
            while True:
                if filter_select in cars_filter:
                    res_filter = filter_display_cars(filter_select)
                    if res_filter :
                        display_cars(res_filter)
                        break
                    else:
                        invalid_input_loop()
                        break
                else:
                    invalid_input_loop()
                    break
                   
        elif filsor == 's': # if sort
            sort_col = input('Sort cars data based on what column? ((s)eat,(t)ype,(p)rice,(st)atus): ').lower() # sort by column
            sort_col_opt = {'s':'seat','t':'type','p':'price','st':'status'}
            if sort_col in sort_col_opt: # if the input is in opt dict
                sort_reverse = input('Sort order? ((a)scending,(d)escending): ').lower() # ascending or descending
                sort_reverse_opt = {'a':False,'d':True} 
                while True:
                    if sort_reverse in sort_reverse_opt: # if the input is in opt dict 
                        res_sort = sort_display_cars(sort_col_opt[sort_col],sort_reverse_opt[sort_reverse]) # sort 
                        display_cars(res_sort) # display sorted table
                        break
                    else:
                        invalid_input_loop()
                        continue
            else:
                invalid_input_loop()
                continue
                    
        elif filsor == 'x': # Back to main menu
            break

        else:
            no_exist(filsor)


def filter_display_cars(filter):
    #return filtered dict by filter selection
    if filter in ['4s','5s','7s']: # if the selection is seat number
        cars_data_filtered = [(n,cars_data[n]) for n in cars_data if cars_data[n]['seat'] == int(filter[0])] # filter based on the seat
    elif filter == 'mbs': # if the seat is more than 10
        cars_data_filtered = [(n,cars_data[n]) for n in cars_data if cars_data[n]['seat'] >= 10]
    elif filter in ['rt','pt']:# if the selection is car type
        cars_data_filtered = [(n,cars_data[n]) for n in cars_data if cars_data[n]['type'] == cars_filter[filter]]
    elif filter == '500ap': # if the selection is price above 500000
        cars_data_filtered = [(n,cars_data[n]) for n in cars_data if cars_data[n]['price'] >= 500000]
    elif filter == '500bp': # if the selection is price below 500000
        cars_data_filtered = [(n,cars_data[n]) for n in cars_data if cars_data[n]['price'] <= 500000]
    elif filter in ['a','r','m']: # if the selection is car status
        cars_data_filtered = [(n,cars_data[n]) for n in cars_data if cars_data[n]['status'] == cars_status[filter]]
    else:
        invalid_input_loop()
        return{}

    cars_data_filtered = dict(cars_data_filtered)
    return cars_data_filtered

def sort_display_cars(sort_col, sort_dir):
    #return sorted dict by column and order
    #key argument take cars_data column by accessing cars_data[key][column]
    cars_data_sorted = sorted(cars_data.items(), key = lambda x: x[1][sort_col], reverse=sort_dir)
    cars_data_sorted = dict(cars_data_sorted)
    return cars_data_sorted

def display_rent(): # 1.b. List of Rent
    print(('-'*5)+'LIST OF RENTAL'+('-'*5))
    for h in header['rent_header']: # Loop through header dict
        print(f'{h:<20}', end=' ') # To print cars header
    print('')
    print('-'*100)
    for rent_key,rent_val in rent_data.items():
        print(f'{rent_key:<20}', end=' ')
        print(f"{rent_val['cust_id']:<20}", end=' ')
        print(f"{rent_val['cars_id']:<20}", end=' ')
        print(f"{rent_val['days']:<20}", end=' ')
        print(f"{rent_val['price']:<20}", end=' ')
        print(f"{rent_val['total']:<20}", end=' ')
        print(f"{rent_val['rent_status']:<20}")

def display_cust(): # 1.c. List of Customers
    print(('-'*5)+'LIST OF CUSTOMERS'+('-'*5))
    for h in header['cust_header']: # Loop through header dict
        print(f'{h:<20}', end=' ') # To print cars header
    print('')
    print('-'*100)
    for cust_key,cust_val in cust_data.items():
        print(f'{cust_key:<20}', end=' ')
        print(f"{cust_val['name']:<20}", end=' ')
        print(f"{cust_val['nik']:<20}", end=' ')
        print(f"{cust_val['phone']:<20}")

'''
CAR MANAGEMENT FUNCTION
'''
cars_count = 10
def generate_id():# Generate incremental number to create car unique id
    global cars_count
    cars_count += 1
    return cars_count

def cars_show(): # Menu 2 Car Management Menu
    print('\nCAR MANAGEMENT\n')
    print('Select menu to proceed:')
    for menu_key,menu_val in cars_menu.items(): # Loop through cars_menu dict
        print(f'{menu_key}: {menu_val}') # to print all the cars_menu 
    choose_show = input('Enter the menu you want to run: ').lower()
    return choose_show

def add_cars(): # 2.a. Add Car
    while True:
        new_name = input('Enter Car Name: ')
        if len(new_name.split()) < 2: #Car Name Validation, if not two words
            print('Car name should be Brand + Type!') # throw error
            continue 

        break # if input is true, break from the loop

    new_seat = int(input('Enter Car Seat: '))
    new_type = input('Enter Car Type (regular or premium): ')
    new_price = int(input('Enter Car Rent Price per Day: '))

    
    split_new_name = new_name.split()

    #Create a unique id for every cars
    new_cars_id = f'{split_new_name[0][0].upper()}{new_seat}{generate_id()}{new_type[0].upper()}{split_new_name[1][0].upper()}'

    #create a dict for the new car data
    new_cars = {
        new_cars_id:{
            'name':new_name,
            'seat':new_seat,
            'type':new_type.lower(),
            'price':new_price,
            'status':cars_status['a']}
    }

    cars_data.update(new_cars) # Insert the new dict into cars_data dict
    print(f'Car {new_name} Added with id {new_cars_id}')
    display_cars(cars_data)

def edit_cars(): # 2.b. Edit Car
    if any(k for k in cars_data.keys()): # check if there is any cars on cars_data dict
        display_cars(cars_data)
        print('\nEDIT CAR DATA\n')
        id_to_edit = input('Enter Car id:').upper() #input car id 
        if id_to_edit in cars_data: #check if the car id is exist
            if cars_data[id_to_edit]['status'] == cars_status['r']: #check if the car is still rented or not
                print('\nCar status cannot be changed! \nFinish the rent first!') #cannot edit data while still rented

            else:
                cars_features_edit = input('Enter Features to update (seat,type,price,status):').lower() #input feautres to edit

                def cars_edit_func(x,y,z):
                    cars_data[x][y]=z #edit the value
                    print(f'\n{x} {y} is updated') #confirmation
                    display_cars(cars_data)

                if cars_features_edit == 'price' or cars_features_edit == 'seat': #if numerical features
                    price_seat_edit = int(input(f'Input {cars_features_edit}:')) #accept int input
                    cars_edit_func(id_to_edit,cars_features_edit,price_seat_edit)

                elif cars_features_edit == 'type': #if class feature
                    type_edit = input('Input new type (regular or premium): ').lower() #ask for regular or premium
                    if type_edit == 'regular' or type_edit == 'premium': #if the input match the class
                        cars_edit_func(id_to_edit,cars_features_edit,type_edit) #edit the data
                    else:
                        invalid_input_loop()

                elif cars_features_edit == 'status': #if status feature
                    status_edit = input('Input new status ([a]vailable,[m]aintenance): ').lower() # ask for car status
                    if status_edit == 'a' or status_edit =='m' :# if the input match the status
                        cars_edit_func(id_to_edit,cars_features_edit,cars_status[status_edit])
                    else:
                        invalid_input_loop()
                        
                else:
                    no_exist(cars_features_edit)

        else: # throw warning if car id is not exist
            no_exist(id_to_edit)
    else: # throw warning if there's no data
        no_exist('Car data')
    
def delete_cars(): # 2.c. Delete Car
    if any(k for k in cars_data.keys()): # check if there is any car on cars_data dict
        display_cars(cars_data)
        print('\nDELETE CAR DATA\n')
        id_to_delete = input('Enter Car id:').upper() #input car id 
        if id_to_delete in cars_data: #check if the car id is exist 
            if cars_data[id_to_delete]['status'] == cars_status['a']: # only available car can be deleted
                while True :
                    confirm_del_cars = input(f'Delete {id_to_delete} ? (y/n)').lower() # delete confirmation
                    if confirm_del_cars == 'y': # if yes
                        del cars_data[id_to_delete] # delete dict id 
                        print(f'{id_to_delete} is successfully removed') # success confirmation
                        break
                    
                    elif confirm_del_cars == 'n': # if no
                        print('Cancelled...') # cancel confirmation
                        break
                    
                    else: # wrong input 
                        invalid_input_loop()
                        continue        
            
            else: # confirmation if the car is not available
                print(f'{id_to_delete} is not available to be deleted!')    
    
        else: # throw warning if there's no car id 
            no_exist(id_to_delete)
    
    else: # throw warning if there's no data
        no_exist('Car data')
    
'''
RENTAL MANAGEMENT FUNCTION
'''
rent_count = 0
def rent_id():# Generate incremental number to create rent unique id
    global rent_count
    rent_count += 1
    return rent_count

def wallet(total_price):
    money = 0 #initialize money
    amount_left = total_price # new var of remaining bills

    while amount_left > 0: #loop if there is still bills to pay
        money = int(input('\nEnter payment: '))
    
        if money < amount_left: # if payment is not enough
            amount_left -= money # subtract the bill with current payment
            print(f'Your payment is still short by {amount_left}')
        elif money == amount_left: # if payment is the same as the bill
            amount_left -= money # subtract the bill with current payment
            print('Thank You!')
        else: # if the payment is over the bill
            print('Thank You!')
            print(f'Your change is: {money - amount_left}') # give the change
            amount_left = 0 # amount to pay is automatically 0 

def rent_show(): # Menu 3 Rent Management Menu
    print('\nRENTAL MANAGEMENT\n')
    print('Select menu to proceed:')
    for menu_key,menu_val in rent_menu.items(): # Loop through rent_menu dict
        print(f'{menu_key}: {menu_val}') # to print all the rent_menu 
    choose_show = input('Enter the menu you want to run: ').lower()
    return choose_show

def add_rent(): # 3.a. Add Rental Data
    rent_cust_id =input('Enter Customer ID:').upper()
    if rent_cust_id in cust_data: # Check if customer is already registered
        print(f"\nWelcome, {cust_data[rent_cust_id]['name']}")
        print('Select Car to Proceed\n')
        display_cars(dict([(n,cars_data[n]) for n in cars_data if cars_data[n]['status'] == 'available'])) # Display only available cars
        rent_car_id = input('Enter Car ID: ').upper() # Input Car ID
        if rent_car_id in cars_data: # Check if Car ID is exist
            if cars_data[rent_car_id]['status'] == cars_status['a']: # Check if Car is available to rent
                days = int(input('Enter Days to Rent, Maximum for 30 days only :')) # Input rent days
                if days < 30 and days <1 : # If not meet days criteria, throw warning
                    print('Rent Cannot Be created')
                else: # If meet criteria, create a rent 
                    total_rent = cars_data[rent_car_id]['price']*days
                    print('\nConfirm the rent\n')
                    print(f'Car Name : {cars_data[rent_car_id]['name']}')
                    print(f'Car Seat Number : {cars_data[rent_car_id]['seat']}')
                    print(f'Car Type : {cars_data[rent_car_id]['type']}')
                    print(f'Car Price per Day : {cars_data[rent_car_id]['price']}')
                    print(f'Days to rent : {days}')
                    print(f'Total payment : {total_rent}')
                    while True:
                        confirm_new_rent = input('Confirm? y/n : ').lower() # Confirm the rent
                        if confirm_new_rent == 'y': # If yes, proceed to payment
                            print('Proceed To Payment...')
                            wallet(total_rent) # Payment function
                            new_rent_id = f'R{rent_id()}{rent_car_id[0]}{rent_cust_id[0]}{rent_cust_id[-1]}{days}' #Create Unique Rent ID
                            new_rent = { # Create Rent Data
                                new_rent_id:{
                                    'cust_id':rent_cust_id,
                                    'cars_id':rent_car_id,
                                    'days':days,
                                    'price':cars_data[rent_car_id]['price'],
                                    'total':total_rent,
                                    'rent_status': rent_status['p']
                                }
                            }
                            rent_data.update(new_rent) # Store into rent_data
                            cars_data[rent_car_id]['status'] = cars_status['r']# Update cars_status in cars_data
                            print(f'Rent {new_rent_id} is succesfully processed.') # Success Notification
                            display_rent() # Display rent_data
                            break
                        elif confirm_new_rent == 'n': # Cancel Rent
                            print('Rent Cancelled...')
                            break
                        else :
                            invalid_input_loop()
                            continue
            else: # If car status is not 'a'
                print('Sorry, The Car Is Not Availbale to Rent')
        else:# If car id is not exist
            no_exist('Car ID')
    else: # if customer does not have id, ask to create cust_id
        while True :
            confirm_new_cust = input('Customer Data is Not Exist, would you like to create a new Customer?(y/n): ').lower()
            if confirm_new_cust == 'y': # if yes, proceed to add_cust()
                print('Proceed to Add New Customer...')
                add_cust()
                break
            elif confirm_new_cust == 'n': # if no, cancel rent
                print('Cancelled')
                break
            else:
                invalid_input_loop()
                continue

def edit_rent(): # 3.b. Edit Rental Status
    if any(k for k in rent_data.keys()): # check if there is any rent on rent_data dict
        display_rent()
        print('\nRETURN RENTED CAR\n')
        rent_to_edit = input('Enter Rent ID :').upper() #input rent id to finished
        if rent_to_edit in rent_data: # if rent_id is exist
            if rent_data[rent_to_edit]['rent_status'] == rent_status['f']: # if rent_status of rent_id is finished
                print(f'Rent {rent_to_edit} is already {rent_data[rent_to_edit][rent_status]}!') # throw warning
            else:
                print(f'Rent ID : {rent_to_edit}')
                while True:
                    confirm_finish_status = input('Would you like to finish the rent? (y/n) : ').lower() # confirm to finish
                    if confirm_finish_status == 'y': # if yes
                        rent_data[rent_to_edit]['rent_status'] = rent_status['f'] # update rent_status to finished
                        cars_data[rent_data[rent_to_edit]['cars_id']]['status'] = cars_status['a'] # update car status to available
                        print(f'Rent {rent_to_edit} is finished')
                        print('Make sure the car is returned in good condition') # Success notification
                        break
                    elif confirm_finish_status == 'n': # if no
                        print('Cancelled...')
                        break
                    else:
                        invalid_input_loop()
                        continue
        else: # throw waring if there's no such rent_id
            no_exist(rent_to_edit)

    else: # throw warning if there's no data
        no_exist('Rent')
        
'''
CUSTOMER VALIDATION FUNCTION

'''
cust_count = 1
def cust_id():# Generate incremental number to create customer unique id
    global cust_count
    cust_count += 1
    return cust_count

def val_name(name): # Validate name
        if len(name) < 3: # Name should be more than 3 characters
            return 'Name Should Be 3 or More Characters!'
        else:
            if '0' <= name <= '9': # Name should not contain numbers
                return 'Name Should Not Contain Numbers!'
            else:
                return True

def val_nik(nik): # Validate NIK
        if len(str(nik)) == 16 : 
            return True
        else: # NIK should be 16 digits long
            return 'NIK Should be 16 digits long!'
        
def val_phone(phone): # Validate Phone Number
        if len(phone) < 10 and len(phone) > 13: # Phone number should be between 10-13 numbers
            return 'Phone number should be between 10-13 characters long!'
        elif phone[:2] != '08': # Phone number should start with 08
            return 'Phone number should be started by 08!'
        else:
            return True
        
def val_cust(name,nik,phone): #validation for add and edit customer data
    name_validation = val_name(name)
    nik_validation = val_nik(nik)
    phone_validation = val_phone(phone)
    return name_validation,nik_validation,phone_validation

def create_cust(name,nik,phone): #create a customer data after validation succeded
    birth_date = str(nik)[6:12] # Pick birthdate
    new_cust_id = f'{name[0].upper()}{birth_date}{name[-1].upper()}{cust_id()}' # Create unique Customer ID

    new_cust = {
        new_cust_id:{
            'name':name,
            'nik':nik,
            'phone':phone,
            }
    } #create a new customer data

    cust_data.update(new_cust) # Insert the new dict into cust_data dict
    print('Customer Added')

'''
CUSTOMER MANAGEMENT FUNCTION
'''
def cust_show(): # Menu 4 Customer Management Menu
    print('\nCUSTOMER MANAGEMENT\n')
    print('Select menu to proceed:')
    for menu_key,menu_val in cust_menu.items(): # Loop through cust_menu dict
        print(f'{menu_key}: {menu_val}') # to print all the cust_menu 
    choose_show = input('Enter the menu you want to run: ').lower()
    return choose_show

def add_cust(): # 4.a. Add A New Customer
    cust_name = input('Enter Customer Name: ')
    cust_nik = int(input('Enter Customer NIK: '))
    cust_phone = input('Enter Customer phone number: ')
        
    # Check whether the NIK is already registered
    if any(cust_nik == n['nik'] for n in cust_data.values()): # if the NIK is already exist
        print('Customer is Already Exist!') # Throw warning
    else: # if not
        if val_cust(cust_name,cust_nik,cust_phone): # validate data, if true
            create_cust(cust_name,cust_nik,cust_phone) # create customer id
            display_cust() 
        else:
            invalid_input_loop()

def edit_cust(): # 4.b. Edit Customer
    if any(k for k in cust_data.keys()): # check if there is any customer on cust_data dict
        display_cust()
        print('\nEDIT CUSTOMER DATA\n')
        cust_to_edit = input('Enter Customer ID:').upper() #input customer id 
        if cust_to_edit in cust_data: #check if the customer id is exist
            cust_features_edit = input('Enter Data to update (name,nik,phone):') .lower() #input column to edit
        
            def cust_edit_func(x,y,z):  
                cust_data[x][y]=z # Function to edit the value based on the inputted column name
                print(f'{x} {y} is updated') #confirmation
                display_cust()

            if cust_features_edit == 'name' or cust_features_edit == 'phone': #if string columns
                name_phone_edit = input(f'Input {cust_features_edit}:') #accept string input
                if cust_features_edit == 'name': # If name selected
                    if val_name(name_phone_edit): # validate name, if ok,
                        cust_edit_func(cust_to_edit,cust_features_edit,name_phone_edit) #edit the data
                    else:
                        ('Data Invalid')
                elif cust_features_edit == 'phone': #If phone selected
                    if val_phone(name_phone_edit): #validate phone no, if ok
                        cust_edit_func(cust_to_edit,cust_features_edit,name_phone_edit)#edit the data
                    else:
                        ('Data Invalid')
                elif cust_features_edit == 'nik': #if nik column
                    nik_edit = int(input('Input 16 digits NIK: ')) #Input 16 digits long NIK
                    if val_nik(nik_edit): #validate NIk, if ok
                        cust_edit_func(cust_to_edit,cust_features_edit,nik_edit) #edit the data
                    else:
                        print('Data Invalid') #wrong input
                else:
                    no_exist(cust_features_edit)

        else:
            no_exist(cust_to_edit)

    else: # throw warning if there's no data
        no_exist('Customer')

def delete_cust(): # 4.c. Delete Customer
    if any(k for k in cust_data.keys()): # check if there is any customer on cust_data dict
        display_cust()
        print('\nDELETE CUSTOMER DATA\n')
        cust_to_delete = input('Enter Customer ID:').upper() #input customer id 
        if cust_to_delete in cust_data: #check if the customer id is exist
            while True :
                confirm_del_cust = input(f'Delete {cust_to_delete} ? (y/n)').lower()
                if confirm_del_cust == 'y':
                    del cust_data[cust_to_delete]
                    print(f'{cust_to_delete} Removed')
                    break
                elif confirm_del_cust == 'n':
                    print('Cancelled')
                    break
                else:
                    invalid_input_loop()
                    continue  
        else:
            no_exist(cust_to_delete)

    else: # throw warning if there's no data
        no_exist('Customer')
    

def no_exist(input):
    print('\n\n'+'!-'*6+'WARNING'+'-!'*6)
    print(f'{input} is Not Exist')
    print('!-'*6+'WARNING'+'-!'*6)

def invalid_input_loop():
    print('\n\n'+'!-'*6+'WARNING'+'-!'*6)
    print(f'\tInvalid Input!')
    print(f'\tEnter the right option')
    print('!-'*6+'WARNING'+'-!'*6)


print('CAR RENTAL')
#Looping for menu
while True:
    menu_choice = display_menu()
    if menu_choice == '1':
        show_choice = display_show()
        if show_choice == 'a':
            display_cars(cars_data)
            filsor_cars()
        elif show_choice == 'b':
            display_rent()
        elif show_choice == 'c':
            display_cust()
        elif show_choice == 'x':
            continue
        else:
            no_exist(show_choice)

    elif menu_choice == '2':
        display_cars(cars_data)
        cars_choice = cars_show()
        if cars_choice == 'a':
            add_cars()
        elif cars_choice == 'b':
            edit_cars()
        elif cars_choice == 'c':
            delete_cars()
        elif cars_choice == 'x':
            continue
        else:
            no_exist(cars_choice)

    elif menu_choice == '3':
        display_rent()
        rent_choice =  rent_show()
        if rent_choice == 'a':
            add_rent()
        elif rent_choice == 'b':
            edit_rent()
        elif rent_choice == 'x':
            continue
        else:
            no_exist(rent_choice)

    elif menu_choice == '4':
        display_cust()
        cust_choice =  cust_show()
        if cust_choice == 'a':
            add_cust()
        elif cust_choice == 'b':
            edit_cust()
        elif cust_choice == 'c':
            delete_cust()
        elif cust_choice == 'x':
            continue
        else:
            no_exist(cust_choice)

    elif menu_choice == 'x':
        print('Thank you! :)')
        print('Closing the program...')
        exit()
    #warning for wrong input
    else:
        no_exist(menu_choice)
    

