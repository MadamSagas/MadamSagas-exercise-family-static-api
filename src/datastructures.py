
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

'''
John Jackson, 33 Years old, Lucky Numbers: 7, 13, 22

Jane Jackson, 35 Years old, Lucky Numbers: 10, 14, 3

Jimmy Jackson, 5 Years old, Lucky Numbers: 1

'''

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [{ "id": self._generateId(),
                          "first_name": "Jhon",
                          "last_name": self.last_name, 
                          "age": 33,
                          "lucky_numbers":[7, 13, 22]
                          },
                         {"id": self._generateId(),
                          "first_name": "Jane",
                          "last_name": self.last_name,
                          "age": 35,
                          "lucky_numbers":[10, 14, 3]
                             
                         },
                         {"id": self._generateId(),
                          "first_name": "Jimmy",
                          "last_name": self.last_name,
                          "age": 5,
                          "lucky_numbers":[1]
                         }]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # Agregar el miembro a la lista de miembros
        self._members.append(member)

    def delete_member(self, id):
        # Método para eliminar un miembro de la lista de miembros por su ID
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                return True
        return False        


    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member
        return None

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
