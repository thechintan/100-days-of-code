# try:
#     l=[1,2,5,4]
#     i=int(input("Enter the INDEX: "))
#     print(l[i])
# except:
#     print("tar dohu 0 thi 3 hudhino number nakh,char j element chhe list ma")

# finally:
#     print("I am always executed")


def function1():
    try:
        l=[1,2,5,4]
        i=int(input("Enter the INDEX: "))
        print(l[i])
        return 1
    except:
        print("tar dohu 0 thi 3 hudhino number nakh,char j element chhe list ma")
        return 0
    #finally:
    print("I am always executed")  #output ma nai aave finally vagar, return nai lakhiye to print thase
print(function1())