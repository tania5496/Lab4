"""MyProgram"""

class Room():
    """Represents rooms"""
    def __init__(self, name):
        self.name = name
        self.description = None
        self.character = None
        self.item = None
        self.linkroom = dict()
        self.delivery = None
        self.text_delivery = None
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
    def set_delivery(self, delivery):
        self.delivery = delivery
    def get_details(self):
        """Returns details"""
        result = self.name +"\n"+ "-"*20 +"\n"+ self.description + "\n"
        for key in self.linkroom:
            result += f"\nЩоб потрапити в {self.linkroom[key].name} введіть '{key}'"
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
    def deliver(self, delivery):
        if delivery == self.delivery:
            return True
        return False
    def set_text_after_delivery(self, text):
        self.text_delivery = text
counter = 0
class Character():
    """Represents characters"""
    def __init__(self, name):
        self.name = name
        self.conversation = None
        self.weakness = None
    def describe(self):
        """Returns description"""
        return self.name
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
    def get_name(self):
        """Returns name of item"""
        return self.name


room401 = Room("401 кімната")
room401.set_description("Ти у своїй кімнаті. За столом сидить Соня і не робить домашку")
room401.set_delivery("Мівіна")

studentorium = Room("Студенторіум")
studentorium.set_description("На студенторіумі куча епешників, які роблять ставки коли ж Колиба виставить їм бали.")
studentorium.set_delivery("Плед")
studentorium.set_text_after_delivery("Ми чули, що у когось з 308 є те, що ти шукаєш")

room308 = Room("308 кімната")
room308.set_description("В 308 відчиняє двері Коля")
room308.set_delivery("Картка локаль")

room205 = Room("205 кімната")

room219 = Room("219 кімната")
room219.set_description("Ти стукаєш у двері 219, Даша відчиняє двері.")
room219.set_delivery("Запальничка")
room219.set_text_after_delivery("Карти показують на місце, яке схоже до раю, але наповнене болем студентів, у яких автомат не захотів приймати 20 гривень")

laundry = Room("Чистилище")
laundry.set_description("В чистилищі нікого немає, але є картка локаль на пралці. Поруч з чистилищем пан Роман набирає собі воду для чайочку, адже попереду ще кілька годин зміни.")
laundry.set_delivery("Пиріжки")
laundry.set_text_after_delivery("Будь обережним(ою), якщо тебе хтось побачить на своєму крилі ще й після 23 години, то дасть догану.\nКраще візьми з собою якийсь предмет, щоб якби тебе засік хтось з кураторів, ти міг(могла) сказати,\n що тобі терміново треба було зайти по щось.")

ground_floor = Room("0 поверх")
second_floor = Room("2 поверх")
third_floor = Room("3 поверх")
forth_floor = Room("4 поверх")

sonya = Friend("Соня")
sonya.set_conversation("Там багато людей на студенторіумі, піди запитай, може у когось з них є мівіна")
room401.set_character([sonya])

dasha = Friend("Даша")
dasha.set_conversation("Привіт. У мене немає мівіни і я не знаходила картку локаль, проте я можу зробити розклад на картах, можливо це допоможе. Але в такому разі мені потрібна запальничка для свічки.")
room219.set_character([dasha])

panRoman = Friend("Пан Роман")
panRoman.set_conversation("Еххх, зараз би до чайочку мої улюблені пиріжки з абрикосовим варенням зі Стрийського ринку, щось я забув їх сьогодні купити. Може в тебе є? Я б тоді поділився однією порадою")
laundry.set_character([panRoman])

pletenyy = Friend("Плетений")
pletenyy.set_conversation("Можу пригостити пиріжками з абрикосовим варенням зі Стрийського ринку.")

epe = Friend("Епешники")
epe.set_conversation("У нас немає мівіни, але ми можемо сказати у кого вона може бути, якщо ти позичиш нам пледик на вечір. ")
studentorium.set_character([pletenyy, epe])

kolya = Friend("Коля")
kolya.set_conversation("У мене залишилася одна упаковка мівіни. І я б тобі її віддав, але у мене загубилась картка локаль і якщо я її не знайду до ранку, то мені доведеться снідати мівіною. Я хотів запитати в чаті колегіуму чи хтось її не бачив, але колегіумський інтернет знову здох, тому мені потрібна буде допомога в пошуках.")

olexiy = Friend("Олексій")
olexiy.set_conversation("ЛЬвівський УАЛ найкращий!!!!! А взагалі можеш ще в дівчат з 205 запитати, може у них є, або в когось з 219.")

room308.set_character([kolya, olexiy])

toilet_paper = Item("Туалетний папір")
room219.set_item([toilet_paper])

local_card = Item("Картка локаль")
laundry.set_item([local_card])

mivina = Item("Мівіна")

pyrizhky = Item("Пиріжки")
studentorium.set_item([pyrizhky])

lighter = Item("Запальничка")
plaid = Item("Плед")
room401.set_item([lighter, plaid])

laundry.link_room(ground_floor, "0 поверх")
room219.link_room(second_floor, "2 поверх")
room308.link_room(third_floor, "3 поверх")
room401.link_room(forth_floor, "4 поверх")
studentorium.link_room(forth_floor, "4 поверх")

ground_floor.link_room(laundry, "Чистилище")
ground_floor.link_room(second_floor, "2 поверх")
ground_floor.link_room(third_floor, "3 поверх")
ground_floor.link_room(forth_floor, "4 поверх")

second_floor.link_room(room205, "205 кімната")
second_floor.link_room(room219, "219 кімната")
second_floor.link_room(ground_floor, "0 поверх")
second_floor.link_room(third_floor, "3 поверх")
second_floor.link_room(forth_floor, "4 поверх")

third_floor.link_room(room308, "308 кімната")
third_floor.link_room(ground_floor, "0 поверх")
third_floor.link_room(second_floor, "2 поверх")
third_floor.link_room(forth_floor, "4 поверх")

forth_floor.link_room(room401, "401 кімната")
forth_floor.link_room(studentorium, "Студенторіум")
forth_floor.link_room(ground_floor, "0 поверх")
forth_floor.link_room(second_floor, "2 поверх")
forth_floor.link_room(third_floor, "3 поверх")

current_room = room401
backpack = []

dead = False
counter_room308 = 0
print("Нарешті тобі вдалося зрозуміти умову лабораторної роботи, ти дивишся на годинник, а пройшло вже 3 години, а це означає, що вже за одинадцяту.\nТи дуже голодний, тому потрібно якнайшвидше знайти мівінку, повернутися в кімнату і не отримати догану. ")
print("Ось кілька команд, якими ти можеш користуватися:\nЩоб поговорити з персонажем -'говорити'\nДля того щоб взяти предмет, який знаходиться в кімнаті введи - 'взяти'\nЩоб віддати предмет - 'віддати'\nЩоб боротися - 'боротися'")
print("Щоби з однієї кімнати потрапити в іншу, потрібно спочатку вийти на поверх,\nпіти на поверх, на якому знаходиться потрібна кімната, а потім зайти у потрібну кімнату")
while dead == False:
    print("\n")
    if current_room == room205:
        print("Вітаю, тебе побачив о.Мисяковський і дав догану за перебування на чужому крилі після 23:00. \nНавіщо було туди йти?? Шанси отримати догану за порушення правил на його крилі - 100%. \nТакі речі треба знати, балда...\nГру завершено, ти лох, якого не поселять в к2))")
        dead = True
    else:
        if current_room == room308:
            if counter_room308 == 2:
                myroslava = Enemy("Мирослава")
                myroslava.set_conversation("Догана")
                myroslava.set_weakness = "Туалетний папір"
                room308.set_character([kolya, olexiy, myroslava])
                print("Ой-ой, тебе побачила кураторка крила Мирослава, схоже, на когось чекає догана. \nПотрібно негайно щось придумати. Ти не розгубився і сказав, що тобі терміново треба було занести Туалетний папір до кімнати.\nЯкщо він є у твоєму наплічнику - вважжай, ти викрутився, в іншому випадку...догана")
                if "Туалетний папір" in backpack:
                    print("Єєє у тебе в наплічнику був потрібний предмет, тож догани вдалось уникнути, іди швиденько по мівінку")
                    room308.set_character([kolya, olexiy])
                    counter_room308 +=1
                else:
                    print("\nЙойки, схоже викрутитись не вийшло і ти отримав догану\nГру завершено, ти лох, якого не поселять в к2))")
                    dead = True
        if dead is False:
            if current_room.description is not None:
                current_room.get_details()
                inhabitants = current_room.get_character()
                if inhabitants is not None:
                    inh_descr = "\nВ кімнаті: "
                    for character in inhabitants:
                        inh_descr += character.describe() + ", "
                    print(inh_descr[:-2])
                items = current_room.get_item()
                if items is not None:
                    item_descr = "\nПредмети, які можна взяти: "
                    for item in items:
                        item_descr += item.name + ", "
                    print(item_descr[:-2])
            else:
                result = current_room.name +"\n"+ "-"*20 +"\n"
                for key in current_room.linkroom:
                    result += f"\n\nЩоб потрапити в {current_room.linkroom[key].name} введіть '{key}'"
                print(result)
            command = input("> ")

            if command in ["Чистилище", "Студенторіум", "401 кімната", "308 кімната", "205 кімната", "219 кімната", "0 поверх", "2 поверх", "3 поверх", "4 поверх"]:
                # Move in the given direction
                current_room = current_room.move(command)
                if command == "308 кімната":
                    counter_room308 +=1
            elif command == "говорити":
                # Talk to the inhabitant - check whether there is one!
                if inhabitants is not None:
                    if len(inhabitants) == 1:
                        inhabitants[0].talk()
                    else:
                        print(f"З ким саме ви хочете поговорити? Якщо з {inhabitants[0].name} - введіть 1, якщо з {inhabitants[1].name} - введіть 2")
                        conversation_num = input()
                        if conversation_num == "1":
                            inhabitants[0].talk()
                        elif conversation_num == "2":
                            inhabitants[1].talk()
            elif command == "боротися":
                if inhabitants is not None:
                    for inhabitant in inhabitants:
                        if isinstance(inhabitant, Enemy):
                            # Fight with the inhabitant, if there is one
                            print("Що ви хочете використати для боротьби?")
                            fight_with = input()
                            # Do I have this item?
                            if fight_with in backpack:
                                if inhabitant.fight(fight_with) == True:
                                    # What happens if you win?
                                    print("Ура, ти не отримав догану")
                                    current_room.character = None
                                else:
                                    # What happens if you lose?
                                    print("Oh dear, you lost the fight.")
                                    print("That's the end of the game")
                                    dead = True
                            else:
                                print("Йойки, у тебе немає " + fight_with)
                else:
                    print("Тут немає з ким битися :)")
            elif command == "взяти":
                if items is not None:
                    item_take = "Ти взяв "
                    for item in items:
                        item_take += item.get_name() + ", "
                    item_take = item_take[:-2] + " у свій наплічник"
                    print(item_take)
                    for item in items:
                        backpack.append(item.get_name())
                    current_room.set_item(None)
                else:
                    print("Тут нічого брати!")
            elif command == "віддати":
                print("Напишіть назву предмета, який ви хочете віддати")
                delivery = input()
                if current_room.deliver(delivery):
                    if current_room.text_delivery is not None:
                        print(current_room.text_delivery)
                    elif current_room == room308:
                        room308.set_item([mivina])
                    elif current_room == room401:
                        print("ЄЄЄ гру завершено. Ти щасливий у своїй кімнаті з пачкою мівіни в руках")
                        dead = True
                else:
                    print("Йой, щось не те")
            else:
                print("Я не знаю таку команду :(")