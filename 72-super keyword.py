#super- parent class na method ne call kare

# class parentclass:
#     def parent_method(self):
#         print('this is parent method')
# class childclass(parentclass):
#     def child_method(self):
#         print('this is child method')
#         super().parent_method()
# child_object=childclass()
# child_object.child_method()

# class parentclass:
#     def parent_method(self):
#         print('this is parent method')
# class childclass(parentclass):
#     def parent_method(self):
#         print('Harry')
#         super().parent_method()
#     def child_method(self):
#         print('this is child method')
#         super().parent_method()
# child_object=childclass()
# child_object.child_method()

class parentclass:
    def parent_method(self):
        print('this is parent method')
class childclass(parentclass):
    def parent_method(self):
        print('Harry')
        super().parent_method()
    def child_method(self):
            print('this is child method')
            super().parent_method()
child_object=childclass()
child_object.child_method()
child_object.parent_method()