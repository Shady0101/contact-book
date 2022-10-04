def display_contact():
    print("name \t\t contact number")
    for key in contact:
        print("{}\t\t{}.format(key,contact.get(key))")

#start 
def start():
    print("you can do \n 1.Add new contact \n 2.Edite a contact \n 3.Delete contact \n 4.Search contact")
    x = int(input("What do you want to edite(enter the number) ? "))
   
    #add new contact to list 
    if 1 == x :
        new_name = input("Enter new contact name : ")
        new_number = int(input("Enter new number : "))
        contact[new_name]= new_number
        

    #edite contact in a list
    if x ==2:
        edite_contact = input("Enter the contact to be edited ")
        if edite_contact in contact:
            new_number = input("enter the mobile number ")
            contact[edite_contact] = new_number
            print("contact updated")
            display_contact
        else:
            print("name is not found in book")

    #delete contact
    if x == 3:
        delete_contact = input("Enter the contact you want to delete : ")
        if delete_contact in contact:
            contact.pop(delete_contact)        
        else:
            print("can't find this name ")    
            
contact = {}



start()











