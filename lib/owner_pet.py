class Pet:
    
    PET_TYPES=["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all=[]
    def __init__(self,name,pet_type,owner=None):
        self.name=name
        if pet_type in Pet.PET_TYPES:
         self.pet_type=pet_type
        else:
            raise Exception
        self._owner=owner
        
        Pet.all.append(self)
    @property
    def owner(self):
        return self._owner
    @owner.setter
    def owner(self,value):
        self._owner=value

class Owner:
    def __init__(self,name):
        self.name=name
        
  
    def pets(self):
      return [pet for pet in Pet.all if pet.owner == self]
  
    def add_pet(self,pet):
        if not isinstance(pet,Pet):
         raise Exception
        else:
            pet.owner=self
            return "Added"+pet.name

    def get_sorted_pets(self):
        return sorted([pet for pet in Pet.all if pet.owner == self], key=lambda pet:pet.name)
    

# Bob=Owner("Bob")
# Rex=Pet("Rex","dog",Bob)
# # print(Bob.pets())



# owner = Owner("John")
# pet1 = Pet("Fido", "dog", owner)
# pet2 = Pet("Clifford", "dog", owner)
# pet3 = Pet("Whiskers", "cat", owner)
# pet4 = Pet("Jerry", "reptile", owner)
# print(owner.get_sorted_pets())

