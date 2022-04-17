"""MyProgram"""
class Room():
    """Represents rooms"""
    def __init__(self, name):
        self.name = name
        self.description = None
        self.character = None
        self.item = None
        self.linkroom = dict()
    def set_description(self, room_descr):
        """Receives description"""
        self.description = room_descr
    def link_room(self, another_room, direction):
        """Receives direction to another room and it's name"""
        self.linkroom[direction] = another_room
    def set_character(self, character):
        """Receives character"""
        self.character = character
    def set_item(self, item):
        """Receives item"""
        self.item = item
    def get_details(self):
        """Returns details"""
        result = self.name +"\n"+ "-"*20 +"\n"+ self.description
        for key in self.linkroom:
            result += f"\nThe {self.linkroom[key].name} is " + key
        print(result)
    def get_item(self):
        """Returns item"""
        return self.item
    def get_character(self):
        """Returns character"""
        return self.character
    def move(self, command):
        """Changes the current room"""
        return self.linkroom[command]
counter = 0
class Character():
    """Represents characters"""
    def __init__(self, name):
        self.name = name
        self.conversation = None
        self.weakness = None
    # def describe(self):
    #     """Returns description"""
    #     result = f"{self.name} is here!\n{self.description}"
    #     print(result)
    def talk(self):
        """Returns conversation"""
        print(f"[{self.name} says]: {self.conversation}")
    def set_conversation(self, conversation):
        """Receive conversation"""
        self.conversation = conversation
    def fight(self, fight_with):
        global counter
        """Returns the result of fight"""
        if self.weakness == fight_with:
            counter+=1
            return True
        return False
class Enemy(Character):
    """Represents enemies"""
    def __init__(self, name):
        super().__init__(name)
    def set_weakness(self, weakness):
        """Receives weakness of character"""
        self.weakness = weakness
    def get_defeated(self):
        """Returns number of defeats"""
        global counter
        return counter
class Friend(Character):
    """Represents friends"""
    def __init__(self, name):
        super().__init__(name)
class Item():
    """Represents items"""
    def __init__(self, item_name):
        self.name = item_name
        self.describtion = None
    def set_description(self, item_descr):
        """Receive description"""
        self.describtion = item_descr
    def describe(self):
        """Returns description of item"""
        print(f"The [{self.name}] is here - {self.describtion}")
    def get_name(self):
        """Returns name of item"""
        return self.name
