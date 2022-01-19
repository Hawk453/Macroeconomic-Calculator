from macro import macro 

def main():

    counter = int(input("Enter 1 for GDP at MP using income method and 2 for GDP at MP using Expenditure Method : "))

    obj = macro(counter)


    print("Please enter intial data for the respective GDP calculation: ")
    
    gdp_mp = obj.GDPatMP()       

    print("The GDP at MP is : ", gdp_mp) 

if __name__ == "__main__" :
    main()
