For string:-
string = "Hello, World!"
print(len(string))  # Output: 13

For List:-
my_list = [1, 2, 3, 4, 5]
print(len(my_list))  # Output: 5

For Tuple:-
my_tuple = (1, 2, 3)
print(len(my_tuple))  # Output: 3

For Dictionary:-
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(len(my_dict))  # Output: 3

For Set:-
my_set = {1, 2, 3, 4, 5}
print(len(my_set))  # Output: 5

For Class:-

class MyCustomClass:
    def __init__(self):
        self.data = [1, 2, 3, 4, 5]
    
    def __len__(self):
        return len(self.data)

obj = MyCustomClass()
print(len(obj))  # Output: 5









