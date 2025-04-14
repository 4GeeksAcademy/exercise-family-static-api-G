"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- get_member: Should return a member from the self._members list
"""

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = [
            
                {  # Miembro 1: John Jackson
                "id": self._generate_id(),  # Autogenera ID 
                "first_name": "John",
                "last_name": self.last_name,  # "Jackson"
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {  # Miembro 2: Jane Jackson
                "id": self._generate_id(),  # Autogenera ID 
                "first_name": "Jane",
                "last_name": self.last_name,  # "Jackson"
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {  # Miembro 3: Jimmy Jackson
                "id": self._generate_id(),  # Autogenera ID 
                "first_name": "Jimmy",
                "last_name": self.last_name,  # "Jackson"
                "age": 5,
                "lucky_numbers": [1]
            }
            
        ]

    # This method generates a unique incremental ID
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id
    
    #PARA AGREGAR MIEMBROS 

    def add_member(self, member):
        if "id" not in member: #GUARDAR UN ID SI NO EXISTE
            member["id"]= self._generate_id() #ASIGNAR UN ID AUTOMATICAMENTE
        member["last_name"]=self.last_name
        print(member)
        self._members.append(member)
        return member
            
        ## You have to implement this method
        ## Append the member to the list of _members
        

    def delete_member(self, id):
        member_index=-1
        for i,member in enumerate(self._members):
            if member ["id"] ==id:
                member_index=i
                break
        if member_index==-1:
            return False
        self._members.pop(member_index)
        return True
        ## You have to implement this method
        ## Loop the list and delete the member with the given id
        

    def get_member(self, id):
        for member in self._members:
            if member ["id"] == id:
                return member
        return None
        ## You have to implement this method
        ## Loop all the members and return the one with the given id
        
    # This method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members