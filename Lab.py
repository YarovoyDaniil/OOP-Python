from abc import ABC, abstractmethod
import re
import pymongo
class SingletonMetaclass(type):
    __instance = {}

    def __call__(cls,*args,**kwargs):
        if cls not in cls.__instance:
            cls.__instance[cls] = super().__call__(*args,**kwargs)
        return cls.__instance[cls]


class DataBase(metaclass=SingletonMetaclass):
    def insert(self,name,phone,email,carname,mark,transfer):
        connection = pymongo.MongoClient("mongodb://localhost:27017/")
        database = connection["Cardatabase"]
        collection = database["Cars"]
        data = {"Name of owner":name,"Phone number of owner":phone,"Email address of owner":email,"Name of car":carname,"Name of mark":mark,"Type of transfer":transfer}
        x = collection.insert_one(data)

    def select_by_car(self,carname,mark,transfer):
        connection = pymongo.MongoClient("mongodb://localhost:27017/")
        database = connection["Cardatabase"]
        collection = database["Cars"]
        data = {"Name of car":carname,"Name of mark":mark,"Type of transfer":transfer}
        x = collection.find(data).limit(5)
        for i in x:
            print(x)

    def select_by_owner(self,name,phone,email):
        connection = pymongo.MongoClient("mongodb://localhost:27017/")
        database = connection["Cardatabase"]
        collection = database["Cars"]
        data = {"Name of owner":name,"Phone number of owner":phone,"Email address of owner":email}
        x = collection.find(data).limit(5)
        for i in x:
            print(x)



class Car(ABC):
    @abstractmethod
    def get_name(self):
        pass
    @abstractmethod
    def set_name(self,new):
        pass

    @abstractmethod
    def set_mark(self, new):
        pass

    @abstractmethod
    def get_mark(self):
        pass

    @abstractmethod
    def set_transfer(self, new):
        pass

    @abstractmethod
    def get_transfer(self):
        pass



class Owner(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_phone(self):
        pass

    @abstractmethod
    def get_email(self):
        pass

    @abstractmethod
    def set_name(self,new):
        pass

    @abstractmethod
    def set_phone(self,new):
        pass

    @abstractmethod
    def set_email(self,new):
        pass


class ConcreteOwner(Owner):
    def __init__(self,name,phone,email):
        self.__name = name
        self.__phone = phone
        self.__email = email
        if type(self.__name) != str:
            raise WrongName("Incorrect name")
        if type(self.__phone) != int:
            raise WrongPhone("Phone number must contain only numbers")
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        a = re.search(regex, self.__email)
        if a == None:
            raise WrongEmail("Incorrect email")

    def get_name(self):
        return self.__name


    def set_name(self,new):
        if type(new) != str:
            raise WrongName("Incorrect name")
        self.__name = new

    def get_phone(self):
        return self.__phone

    def set_phone(self,new):
        if type(new) != int:
            raise WrongPhone("Phone number must contain only numbers")
        self.__phone = new

    def get_email(self):
        return self.__email

    def set_email(self,new):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        a = re.search(regex, new)
        if a == None:
            raise WrongEmail("Incorrect email")
        self.__email = new

class ConcreteCar(Car):

    def __init__(self,name,mark,transfer):
        self.__name = name
        self.__mark = mark
        self.__transfer = transfer
        if type(self.__name) != str:
            raise WrongName("Incorrect name")
        if type(self.__mark) != str:
            raise WrongMark("Incorrect mark")
        if type(self.__transfer) != str:
            raise WrongTransfer("This field can be only:automatic transmission or transmission ")



    def get_name(self):
        return self.__name

    def set_name(self,new):
        if type(new) != str:
            raise WrongName("Incorrect name")
        self.__name = new

    def get_mark(self):
        return self.__mark

    def set_mark(self,new):
        if type(new) != str:
            raise WrongMark("Incorrect mark")
        self.__mark = new

    def get_transfer(self):
        return self.__transfer

    def set_transfer(self, new):
        if type(new) != str:
            raise WrongTransfer("This field can be only:automatic transmission or transmission ")
        self.__transfer = new

class MachineCopare:
    def __init__(self,first:ConcreteCar,second:ConcreteCar):
        self.first_car = first
        self.second_car = second

    def compare(self):
        pass




class Fuel:
    def __init__(self, vol):
        self.__volume = vol

    def get_volume(self):
        return self.__volume

    def set_volume(self, v:int):
        self.__volume = v

class Wheels:
    __wheel_type = 'Classic steel wheel'

    def get_wheels_type(self):
        return self.__wheel_type

    def set_wheels_type(self,w:str):
        self.__wheel_type = w


class WrongName(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class WrongPhone(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class WrongEmail(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class WrongMark(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class WrongTransfer(Exception):
    def __init__(self, msg):
        super().__init__(msg)



def test():
    while True:
        try:
            print("\n\n\n1.Find car by owner")
            print("2.Find owner by car")
            print("3.Input own information")
            print("4.Exit")
            k = int(input("Enter your choice:"))
            db = DataBase()
            if k==1:
                print("Enter name of owner:")
                name = str(input())
                print("Enter phone number of owner")
                phone = int(input())
                print("Enter email of owner")
                email = str(input())
                owner = ConcreteOwner(name, phone, email)
                print(db.select_by_owner(owner.get_name(),owner.get_phone(),owner.get_email()))

            if k ==2:
                print("Enter name of car:")
                carname = str(input())
                print("Enter mark of car:")
                mark = str(input())
                print("Enter type of transfer:")
                transfer = str(input())
                car = ConcreteCar(carname, mark, transfer)
                db.select_by_car(car.get_name(), car.get_mark(), car.get_transfer())
            if k ==3:
                print("Enter your name: ")
                name = str(input())
                print("Enter your phone number:")
                phone = int(input())
                print("Enter your email:")
                email = str(input())
                owner = ConcreteOwner(name,phone,email)
                print("Enter name of car:")
                carname = str(input())
                print("Enter mark of car:")
                mark = str(input())
                print("Enter type of transfer:")
                transfer = str(input())
                car = ConcreteCar(carname,mark,transfer)
                while True:
                    print("You entered:\nName:",owner.get_name(),"\nPhone number:",owner.get_phone(),"\nEmail:",owner.get_email(),"\nName of car:",car.get_name(),"\nMark of car:",car.get_mark(),"\nType of transfer:",car.get_transfer(),"\n\n\n")
                    print("1.Insert in database\n2.Change Name\n3.Change phone\n4.Change email\n5.Change name of car\n6.Change mark of car\n7.Change type of transfer\n8.Exit to menu")
                    change = int(input("Enter your choice:"))
                    if change == 1:
                        db.insert(owner.get_name(),owner.get_phone(),owner.get_email(),car.get_name(),car.get_mark(),car.get_transfer())
                        print("Data was inserted")
                        break
                    if change ==2:
                        print("Set new name:")
                        name = str(input())
                        owner.set_name(name)
                    if change == 3:
                        print("Set new phone:")
                        phone = int(input())
                        owner.set_phone(phone)
                    if change == 4:
                        print("Set new email:")
                        email = str(input())
                        owner.set_email(email)
                    if change == 5:
                        print("Set new name of car:")
                        carname = str(input())
                        car.set_name(carname)
                    if change == 6:
                        print("Set new mark of car:")
                        mark = str(input())
                        car.set_mark(mark)
                    if change == 7:
                        print("Set new type of transfer:")
                        transfer = str(input())
                        car.set_transfer(transfer)
                    if change == 8:
                        break
            if k == 4:
                break
        except ValueError:
            print("\nWrong input\n\n")
        except WrongEmail as e:
            print(f'{e}')
        except WrongName as e:
            print(f'{e}\n\n')
        except WrongPhone as e:
            print(f'{e}\n\n')
        except WrongTransfer as e:
            print(f'{e}\n\n')
if __name__ == '__main__':
    test()