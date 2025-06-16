#To which party you have casted your vote?
#BJP=1,CNGRS=2,AAP=3,OTHER=ANY NUMBERS

x=int(input("Enter the number of party:")) #x is the variable to match
match x:
    #if x is 1
    case 1:
        print ("VOTER HAVE VOTED FOR BJP")
    #case with if statement
    case 2:
        print('VOTER HAVE VOTED FOR CONGRESS')
    case 3:
        print('VOTER HAVE VOTED FOR AAP')
    case _: #default case
        print("VOTER HAVE VOTED FOR OTHER")