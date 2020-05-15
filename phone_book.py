
op = ('1. Add a contact', '2. View contact list', '3. Modify a contact', '4. Delete a contact')

#this section of the script reads the whole phone book from a buffer,
#namely phone_book.txt, then assignes the values to a dictionary in which
#the key is the name
pb = {}
alf = []

#gets every lines, corrisponding to a contact and stores it in the list lines
with open('phone_book.txt') as f:
    lines = [line.rstrip() for line in f]
#sorts through the list and assigns the contact info to the dictionary
for i in lines:
    name, number = i.split(' ')
    pb[name] = number
    alf.append(name)


#this operations allows to later print the phone book in alphabetic order cause dictionaries suck
alf.sort()
f.close()
#########

#this is a set of very simple ausiliary functions in order to not repeat myself
###
#prints the phone book
def prnt():
    print('\n\nThis is Simone contact list\n')
    for name in alf:
        print(f'{name}  {pb[name]}\n')

#writes the new buffer
def wri():
    f = open('phone_book.txt', 'w')
    for name in alf:
        f.write(f'{name} {pb[name]}\n')
    f.close()

#removes a contact from the buffer
def rem():
    name = input('what contact do you wish to remove? ')
    del pb[name]
    alf.remove(name)

def r_menu():
    print("press 9 to perform another action, 0 to exit")
    o = int(input())
    if o == 9:
        menu()
    if o == 0:
        print("Bye")
        return False
####

#menu function; this is the main function
#the fact that it's a function will allow to make it itarable so to not relaunch
#the script over and over to do multiple actions
def menu():
    print('chose an option:\n')
    for i in op:
        print(i)

    a = int(input())

    #adds the contact to the buffer
    if a ==  1:
        name = input('what is the contact name? ')
        number = input('what is the contact number? ')
        #checks if the contact, name and number is already in the phone book
        for nam in pb:
            if pb[nam] == number and nam == name:
                r_menu()
        pb[name] = number
        #sorts the names in alphabetical order
        alf.append(name)
        alf.sort()
        wri()


    #prints the whole contact list
    if a == 2:
        prnt()


    #allows the user to modify a contact
    if a == 3:
        b = int(input('do you wish to first see the contact list?\nInsert "1" for yes and "0" for no'))
        if b == 1:
            prnt()

        c = ['1. name', '2. number', '3. both']
        print('what do you wish to modify?\n')
        for i in c:
            print(i)
        o = int(input())

        if o == 1:
            o_name = input('what is the name of the contact you wish to modify? ')
            #assign the phone number, not to be modified to a buffer, in order to not lose it
            tmp = pb[o_name]
            del pb[o_name]
            #acquires the new name and sorts the new list in alphabetic order
            n_name = input('what name do you wish to assign to this contact? ')
            pb[n_name] = tmp
            alf.append(n_name)
            alf.sort()
            #writes on the buffer
            wri()


        if o == 2:
            name = input('what is the name of the contact you wish to modify? ')
            n_num = input('what is the new number? ')
            del pb[name]
            pb[name] = n_num
            wri()


        if  o == 3:
            rem()
            name = input('what is the contact name? ')
            number = input('what is the contact number? ')
            pb[name] = number
            alf.append(name)
            alf.sort()
            wri()
            r_menu()



    #deletes a contact
    if a == 4:
        rem()
        wri()

    r_menu()


menu()
