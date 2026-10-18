from copy import copy, deepcopy

# TODO 1:
# Create a parent class.
class ParentClass:
    # - Include at least one class variable
    # All parents reside in same neighborhood
    parent_neighborhood_name = "Neighborhood: Candle Light"

    # - Include at least two instance variables.
    # - Include a constructor (__init__).
    #def __init__(self, mom_name: str, dad_name:str):
     #   self.mom_name = mom_name
      #  self.dad_name = dad_name

    def __init__(self, mom_name: str, dad_name: str):

        if not isinstance(mom_name, str) or not mom_name.strip():
            raise ValueError("Mom's name must be a non-empty string.")

        if not isinstance(dad_name, str) or not dad_name.strip():
            raise ValueError("Dad's name must be a non-empty string.")

        self.mom_name = mom_name.strip()
        self.dad_name = dad_name.strip()

# - Include a method that returns or displays information about the object.
    def display_info(self):
        print(self.parent_neighborhood_name)
        print("\n=== Parent Info ===")
        print(f"Mom's name: {self.mom_name}, Dad's name: {self.dad_name}")

#************************************************************************************

# TODO 2:

# Create a child class that inherits from the parent class.  Use inheritance
class ChildClass(ParentClass):
    # - Add at least one new class variable.
    bsa_troop = "Fayetteville Troop 70"

    def __init__(self, mom_name, dad_name, child_name: str, child_rank: str):
        super().__init__(mom_name, dad_name)
        if not isinstance(child_name, str) or not child_name.strip():
            raise ValueError("Child's name must be a non-empty string.")
        # - Add at least two new instance variables.
        self.child_name = child_name.strip()
        self.child_rank = child_rank

    # - Add at least one new method.
    def get_child_rank(self):
        return self.child_rank
    # call it:
    # child1 = ChildClass("Mary", "James", "Mikey", "Tenderfoot")
    # print(child1.get_child_rank())

    # - Override a method from the parent class.
    def display_info(self):  # overriding: redefines ParentClass "display_info" line
        print("\n=== Child's Info ===")
        print(f"Child's name: {self.child_name}, Rank: {self.child_rank}")
#==============================================================>>>


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:



# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")
    print("TODO: Implement namespace demonstration")

    # - Create at least two objects of the child class.
    child1 = ChildClass("Mary", "James", "Alex", "Tenderfoot")
    child2 = ChildClass("Suzy", "Bruce", "Cody", "Second Class")

    print("\n=== Class Namespace ===")
    print(ChildClass.__dict__)      # - Display each object's namespace using __dict__.

    print("\n=== First Child's Instance Namespace ===")

    child1.favorite_activity = "Hiking"   # - Add a new attribute to only one object after it is created.
    print(child1.__dict__)

    print("\n=== Second Child's Instance Namespace ===")
    print(child2.__dict__)

    # - Access a class variable through the class itself.
    # - Access the same class variable through an object.
    print()
    print("Class variable accessed through class: ", ChildClass.bsa_troop)
    print("Class variable accessed through object: ", child1.bsa_troop)
#==========================================================>>>


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")
    print("TODO: Implement shallow copy and deep copy demonstration")

    a = {"Name" : "Smith", "Activities" : ["Hiking", "Camping"]}
    b = copy(a)  #shallow copy accepts/adapts to modified data
    c = deepcopy(a)  #deep copy retains all original data

    a["Activities"][1] = "Fire"  #modify original a's nested data
    print("Original after modification: " , a)
    print("Shallow copy: " , b)
    print("Deep copy preserving original nested data: " , c)
#==================================================================>>>


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\nTODO: Create and test your parent object")

    parent1 = ParentClass("Maria", "None")
    parent1.display_info()

    print()

    print("\nTODO: Create and test your child object")
    child3 = ChildClass("Emma", "Evan",
                        "Lee", "First Class")
    child3.display_info()

    ParentClass.display_info(child3)
    print(f"Child's rank: {child3.get_child_rank()}")

    # - Call your namespace demonstration function.
    # - Call your copy demonstration function.
    demonstrate_namespaces()  #calls namespaces function with both objects created within it
    demonstrate_copying()

if __name__ == "__main__":
    main()