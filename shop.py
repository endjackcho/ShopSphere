import json
import os
######
# Files
file_product = "products.json"
file_box = "box.json"

# Saving data
def save_data(file,lst):
    with open(file,"w") as f :
        json.dump(lst,f)

# Loading data automaticly
def load_data(file):
    try :
        with open(file,"r") as f :
            return json.load(f)
    except :
        return []

# Deleting file
def delete_file(file):
    if os.path.exists(file) :
        os.remove(file)

# Deleting file,list
def delete_data(file,lst):
    if os.path.exists(file) and len(lst) > 0 :
        q = input("Are your sure to deleting file (Y/N) ? ")
        q = q.strip().lower()
        if q == "y" or q == "yes" or q == "yeah" :
            lst.clear()
            delete_file(file)
            print("\n>> List Was Deleted !\n")
        else :
            print("\n>> List wasen't Deleted !\n")
    else :
        print(errors["err-not-fnd"])

# Lists (auto load)
products_list = load_data(file_product)
box_list = load_data(file_box)

# Errors
errors = {
    "err-num" : "\n>> Error : Please enter valid input for options !\n",
    "err-opt" : "\n>> Error : Please choose option from options !\n",
    "err-prc" : "\n>> Invalid Price !\n",
    "err-lst" : "\n>> List Was Empty !\n",
    "err-not-fnd" : "\n>> Not Found !\n"
}

#####

########################################### Functions ###################################################################
# Admin Started

# Just for better response
def clear_terminal():
    os.system("cls")

# Adding item to list (A)
def add():
    while True :
        name = input("Name of product (press enter to stop) : ")
        if name == "" : break
        price = input("Price of product : ")
        if price.isnumeric() :
            if int(price) > 0 :
                products_list.append({
                    "name" : name,
                    "price" : int(price),
                })
            else :
                print(errors["err-prc"])
        else :
            print(errors["err-prc"])

# Chaping lists
def chap(lst):
    if len(lst) > 0 :
        print("Number\tName\tPrice\n")
        for i,product in enumerate(lst,1):
            print(str(i)+")\t"+product["name"]+"\t"+str(product["price"])+"$\n")
        return True
    else :
        print(errors["err-lst"])

# Chaping product lst
def chap_main_list() :
    return True if chap(products_list) == True else False

# Removing products from list (A)
def remove_product():
    if chap_main_list() == True :
        name = input("Name for remove : ")
        for product in products_list :
            if product["name"] == name.lower().strip() :
                products_list.remove(product)
                print("\n>> Removed !\n")
                break
        else :
            print(errors["err-not-fnd"])
    else :
        print(errors["err-lst"])

# Admin managment (A)
def admin():
    clear_terminal()
    while True :
        print("\n\tWelcome Back\t\n")
        menu = input("\n1.Add Product\n2.Remove Product\n3.Product's List\n4.Save Data\n5.Delete Data\n6.Quit\n")
        clear_terminal()
        if menu.isnumeric():
            if menu == "1" : add()
            elif menu == "2" : remove_product()
            elif menu == "3" : 
                chap_main_list()
                input("\nPress Enter to conitinue !\n")
            elif menu == "4" : 
                save_data(file_product,products_list)
                print("\n>> Data Saved Sucessfully !\n")
            elif menu == "5" : delete_data(file_product,products_list)
            elif menu == "6" : break
            else :
                print(errors["err-opt"])
        else :
            print(errors["err-num"])

# Admin Ended

# Customer started

# Adding product into box (C)
def purhcase():
    if chap_main_list() == True :
        name = input("Name for buy : ")
        for product in products_list :
            if product["name"] == name.lower() :
                box_list.append(product)
                print("\n>>> Added To Box !\n")
                save_data(file_box,box_list)
                break
        else :
            print(errors["err-not-fnd"])

# Purchasing Product (C)
def final_purch():
    clear_terminal()
    if chap(box_list) == True :
        q = input("\n>> Are You sure about purchasing all items (Y/N) ? ")
        q = q.strip().lower()
        if q == "y" or q == "yes" or q == "yeah" :
            delete_file(file_box)
            box_list.clear()
            print("\n>> Purchase Seuccessfully !\n")
        else :
            print("\n>> Purchasig Canceled !\n")

# Manage cart (C)
def cart_manage():
    q = input("\n>> Press enter to back to the menu else enter something else !\n")
    if q != "" :
        while True:
            menu = input("\n1.Deleting Box\n2.Purchase\n3.Quit\n- ")
            if menu.isnumeric() :
                if menu == "1" :
                    delete_data(file_box,box_list)
                elif menu == "2" : final_purch()
                elif menu == "3" : break
            else :
                print(errors["err-num"])

# Review Cart (C)
def cart():
    if chap(box_list) == True :
        s = 0
        for item in box_list :
            s += item["price"]

        print(f"\n>>> Total price : {s}$\n")

# Customer Managment (C)
def customer():
    while True :
        menu = input("1.Buy\n2.Product's List\n3.Cart\n4.Quit\n")
        clear_terminal()
        if menu.isnumeric() :
            if menu == "1" : purhcase()
            elif menu == "2" :
                chap_main_list()
            elif menu == "3" :
                cart()
                cart_manage()
            elif menu == "4" : break
            else :
                print(errors["err-opt"])
        else :
            print(errors["err-num"])

########################################### Main #######################################################################

# Main Func
def main():
    while True :
        menu = input("1.Customer\t2.Admin\t\t3.Quit\n")
        clear_terminal()
        if menu.isnumeric():
            if menu == "1" : customer()
            elif menu == "2" : admin()
            elif menu == "3" : break
            else :
                print(errors["err-opt"])
        else :
            print(errors["err-num"])

    print("""
    ~ Thanks for choosing use to your work !
        - Created by : @endjackcho
    """.rstrip())

if __name__ == "__main__" :
    main()


# Actully you can make a username,password for admin !