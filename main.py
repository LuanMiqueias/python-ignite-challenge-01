from typing import List, Dict, Optional


class Contacts:
    contacts: List[Dict[str, Optional[str]]] = []

    def user_exists(self, name: Optional[str]) -> bool:
        # if contacts:
        #     return False
        if name is None:
            return False
        for contact in self.contacts:
            if contact.get("name").lower() == name.lower():
                return True
        return False

    def get(self, name):
        if name is None:
            return False
        for contact in self.contacts:
            if contact.get("name").lower() == name.lower():
                return contact

    def add(self, name, email):
        print(self.user_exists(name))

        if self.user_exists(name) == False:
            self.contacts.append({"name": name, "email": email, "isFavorite": False})
            print(f"Contato {name} adicionado com sucesso.")
            init()
        else:
            print("Contato existente!")
            addContact()

    def remove(self, name):
        if name in self.contacts:
            self.contacts.append(name)
            init()
        else:
            print("Contato não encontrado!")
            addContact()

    def listFavorites(self):
        filtered_list = []
        for contact in self.contacts:
            if contact["isFavorite"] == True:
                filtered_list.append(contact)

        print(filtered_list)

    def edit(self):
        print(self.contacts)

    def update(
        self, name: str, email: Optional[str] = None, isFavorite: Optional[bool] = None
    ):
        for contact in self.contacts:
            if contact.get("name").lower() == name.lower():
                if email is not None:
                    contact["email"] = email
                if isFavorite is not None:
                    contact["isFavorite"] = isFavorite
                print(f"Contato {name} atualizado com sucesso.")
                init()
                return

        print(f"Contato {name} não encontrado.")
        init()

    def delete(self, name: str):
        for contact in self.contacts:
            if contact.get("name").lower() == name.lower():
                self.contacts.remove(contact)
                print(f"Contato {name} removido com sucesso.")
            print(f"Contato {name} não encontrado.")
        print(self.contacts)
        init()


def addContact():
    while True:
        name = str(input("Nome: "))
        email = str(input("Email: "))
        contacts.add(name, email)
        break


def listContacts():
    contacts.listFavorites()
    init()


def deleteContact():
    name = str(input("Nome: "))
    contacts.delete(name)


def editContact():
    name = str(input("Nome: "))
    while True:
        print("1. Alterar email")
        actionId = int(input("Digite uma opção: "))
        if actionId == 1:
            email = str(input("Novo Email: "))
            contacts.update(name, email)
            break


def handleFavorite():
    name = str(input("Nome: "))
    isFavorite = contacts.get(name)["isFavorite"]
    # isFavorite = oddFavoriteValue == True : False else True
    if isFavorite == True:
        isFavorite = False
    else:
        isFavorite = True

    contacts.update(name, None, isFavorite)


actions = {
    1: addContact,
    2: editContact,
    3: handleFavorite,
    4: listContacts,
    5: deleteContact,
}
contacts = Contacts()


def init():
    while True:
        print("---------------------------------------------------")
        print("1. Adicionar Contato")
        print("2. Editar Contato")
        print("3. Adicionar/Remover Contato aos favoritos")
        print("4. Ver lista de contatos favoritos")
        print("5. Deletar Contato")
        print("")

        actionId = int(input("Digite uma opção: "))
        print("---------------------------------------------------")

        if actionId:
            actions[actionId]()
            break

        # if actionId:
        #     break
        # else:

        # if actions.find(actionId) == True:
        #     actions[actionId]()

        print(actions.find(actionId))


init()
