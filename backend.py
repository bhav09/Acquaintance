#here the medium that we are using to store the data is a csv file.
import csv
import numpy as np
import pandas as pd
import os
import operator
from pathlib import Path

#for staff
#here the columns for food item are : [name of item , inventory (kgs) , expiry date]

#methods
'''
def file():                                         SEGMENT 1 : IF YOU WANT TO MAKE A MENU OF YOUR OWN
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_cols)
            writer.writeheader()
            for data in items_data:
                writer.writerow(data)
    except IOError:
        print("I/O error")

#adding food items
def new_item():
    global item_info
    choice = 'yes'
    while choice == 'yes':
        item_info = {}
        for i in csv_cols:
            print('Enter',i,end=':')
            entry = input()
            item_info.update({i:entry})
        choice = input('Want to enter more')
        items.append(item_info)

def add_data():
    global df
    try:
        with open(csv_file,'a+',newline='') as csvfile:
            writer = csv.DictWriter(csvfile,fieldnames=csv_cols)
            writer.writeheader()
            for data in items:
                writer.writerow(data)
    except IOError:
        print('I/O Error')
    df = pd.read_csv('food_items.csv')
    print(df)
    remove_index = []
    x = list(df['name_of_item'])
    for i in range(len(x)):
        if x[i] == 'name_of_item':
            remove_index.append(i)
    print(remove_index)
    df = df.drop(df.index[remove_index])
    print('----------------------------------------')
    print('Data frame is:')
    print(df)

    # re arranging the indices
    print('----------------------------------------')

    df.reset_index(drop=True, inplace=True)
    print('Index reseted')
    print(df)
    print('Data Added')
    clearning_file()


def clearning_file():
    df = pd.read_csv('food_items.csv')
    print(df)
    remove_index = []
    x = list(df['name_of_item'])
    for i in range(len(x)):
        if x[i] == 'name_of_item':
            remove_index.append(i)
    print(remove_index)
    df = df.drop(df.index[remove_index])
    print('----------------------------------------')
    print(df)

    # re arranging the indices
    print('----------------------------------------')

    df.reset_index(drop=True, inplace=True)
    print(df)

    #converting the data frame to csv file
    df.to_csv(csv_file,header=True,index=False) #header is for giving the naem to columns

def set_MRP():
    df = pd.read_csv('food_items.csv')
    df.columns = csv_cols
    print(df)
    x = list(df['name_of_item'])
    print('Enter MRP')
    price_of_items = []
    for i in range(len(x)):
        dict_price = {}
        print(x[i],end=' ')
        price = input()
        dict_price.update({x[i]:price})
        price_of_items.append(dict_price)
    print(price_of_items)
'''
def all_food_items():

    food = list(df_menu['name_of_item'])
    count = 0
    for i in range(len(food)):
        dict_preference.update({food[i]:count})
    print(dict_preference)

def menu():
    global check_file
    all_food_items()
    #now dealing with actual menu
    #df_menu = pd.read_csv('Hotel_Menu - Sheet1.csv')
    print(df_menu)
    print('Enter index of the dish that you want to order:')
    order_food = [] #this will have the index values of the food item that our customer wants to eat.
    choice = 'yes'
    while choice == 'yes':
        item_index = int(input('Enter index'))
        order_food.append(item_index) #appending the food items that the customer wishes to order
        choice = input('Enter more?')
    item_name = df_menu['name_of_item']
    item_name = list(item_name)
    for i in order_food:
        y = item_name[i]
        dict_preference[y] += 1
    print('Preferences are: ')
    print(dict_preference)

def signup():
    global username,password
    username = input('Enter Username:')
    password = input('Enter Password')
    ref = pd.read_csv('Hotel_Menu - Sheet1.csv')
    data_file = f'{username}-{password}.csv'
    cols = ['name_of_item','preferences']
    ref.columns = cols
    #print(ref.columns)
    print(ref)
    print(ref.iloc[:,1])
    choice = list(ref.iloc[:,1])
    print(choice)
    ref_choice = []
    for i in choice:
        i -= i      #initially the number of times any dish that has been added is 0 so i-i =0
        ref_choice.append(i)
    print(ref_choice)
    ref.iloc[:,1] = ref_choice
    ref.to_csv(data_file, header=True, index=False)
    file_path = f'User Data/{username}/'
    print('Account Created!')
    os.mkdir(file_path)
    Path(data_file).rename(f'User Data/{username}/'+data_file)   #changing the path of the created file

def login():                        #has menu (), recommend()
    global check_folder , username,password,user_data
    username = input('Enter Username:')
    password = input('Enter Password:')
    check_folder = username
    #print(check_file)
    if check_folder in os.listdir('C:/Users/91884/PycharmProjects/hotel_management_system/User Data/'):
        print('File exists')
        user_data = pd.read_csv(f'User Data/{check_folder}/'+f'{username}-{password}.csv')
        if input('Want to order food?') == 'yes':
            menu()
            #print(dict_preference.values())
            dictionary = {}
            for i in range(len(user_data.index)):
                var = list(user_data.iloc[i])
                dictionary.update({var[0]:var[1]})
            for i in dictionary:
                dictionary[i] += dict_preference[i]
            print('Dictionary is:',dictionary)
            file_name = f'User Data/{username}/{username}-{password}.csv'
            abc = []
            for i in dictionary:
                abc.append({'name_of_item': i, 'preferences': dictionary[i]})
            try:
                with open(file_name, 'w', newline='') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=['name_of_item', 'preferences'])
                    writer.writeheader()
                    for data in abc:
                        writer.writerow(data)
                    print('Done')
            except IOError:
                print('I/O Error')
            #user_data.iloc[:,1] = dict_preference.values()
            user_data.to_csv(check_folder,header='True',index=False)
            #print('login_file_converted')
            recommend()
            Path(check_folder).replace(f'C:/Users/91884/PycharmProjects/hotel_management_system/User Data/{username}/'+check_folder)
            update()
        else:
            print('Have a great day!')
    else:
        print('File not found') 
        print('Signing Up')
        signup()
        print('Logging Up')
        login()

def recommend():
    #global username,password
    # we want to store the preference based on descending order. So that the customer would be able to order.
    print('--------------------Recommending-----------------------------------')
    user_data = pd.read_csv(f'User Data/{check_folder}/{username}-{password}.csv')
    print(user_data)
    user_data.set_index(user_data['name_of_item'])
    user_data.transpose()
    d = user_data['preferences'].to_dict()
    # d = {"a": 10, "b": 43, "c": 31}
    cd = sorted(d.items(), key=operator.itemgetter(1), reverse=True) #prints the dict in desc order of the value
    cd = dict(cd)
    print(cd)
    keys_index = list(cd.keys())
    x = user_data['name_of_item']
    y = {}
    for i in range(len(user_data['name_of_item'])):
        y.update({x[keys_index[i]]: cd[keys_index[i]]})
    print(y)
    recommend_file = f'{username}-{password}_recommend'+'.csv'
    print(recommend_file)
    y = pd.DataFrame(y.items()) #covnerting y to a data frame
    y.columns = ['name_of_item','preferences']
    print(y)
    y.to_csv(recommend_file, header=True, index=False)
    if recommend_file not in os.listdir(f'User Data/{username}/'):
        Path(recommend_file).rename(f'User Data/{username}/' + recommend_file)
    else:
        os.remove(f'User Data/{username}/' + recommend_file)
        Path(recommend_file).rename(f'User Data/{username}/' + recommend_file)
    print('Done')

def update():
    print('---------------------------Updating-----------------------------')
    dictionary = {}
    user_file = pd.read_csv(f'C:/Users/91884/PycharmProjects/hotel_management_system/User Data/{username}/{username}-{password}.csv')  # now changing the recommendations from the root
    data_dict = csv.reader(open(f'C:/Users/91884/PycharmProjects/hotel_management_system/User Data/{username}/{username}-{password}_recommend.csv'))
    d = {}
    l = []
    list_to = []
    for row in data_dict:
        k, v = row
        d[k] = v
    # print(d)
    d.pop('name_of_item')
    print(d)  # dictionary
    user_file.to_dict()
    print(user_file)
    for k in user_file:
        y = user_file[k]
        l.append(y)
    d1 = l[0]  # dict 1
    d2 = l[1]  # dict 2
    dic = {}  # dictionary for adding the values from 2 different dictionaries
    for i in range(14):
        dic.update({d1[i]: d2[i]})
    print(d)
    for i in dic:
        dic[i] = d[i]
        dictionary.update({i: dic[i]})
    print('--------------------------')
    print(dictionary)

    csv_cols = ['name_of_item', 'preferences']

    for i in dictionary:
        list_to.append({csv_cols[0]: i, csv_cols[1]: dictionary[i]})
        print()
    print(list_to)
    csv_file = f'{username}-{password}.csv'
    try:
        with open(csv_file, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_cols)
            writer.writeheader()
            for data in list_to:
                writer.writerow(data)
        os.remove(f'User Data/{username}/{csv_file}')
        Path(csv_file).rename(f'User Data/{username}/{csv_file}')
    except IOError:
        print('I/O Error')



#main code
csv_cols = ['name_of_item','inventory','expiry_date']
items_data = [
    {'name_of_item':'Burger','inventory':10,'expiry_date':'01/01/2020'},
    {'name_of_item':'Sandwitch','inventory':10,'expiry_date':'01/01/2020'}
]
items = []
csv_file = 'food_items.csv'
#file()
dict_preference = {} #for showing all the prefenences

df_menu = pd.read_csv('Hotel_Menu - Sheet1.csv')
#add_new_item = input('Want to add new item:')

'''
if add_new_item == 'yes':
    new_item()                          #un-comment when have un-commented segment 1 
    print('Added Successfully ')

print(items)

print('Want to add the data to the file ?')
print()
confirmation = input('Yes/No:')
if confirmation == 'Yes' or confirmation == 'yes':
    add_data()

#editing the data (removing all the extra csv_cols from our csv file)
print('----------------------------------------')

if input('Set MRP on food items?') == 'yes':
    set_MRP()
'''
#for customers
click_to_enter = input('Login/Signup:')
if click_to_enter == 'Signup':
    signup()
elif click_to_enter == 'Login':
    login()

#what would you like to order
#all_food_items()

#to do : try to impute the length of the code
