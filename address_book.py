from csv import *
from address import Address
from work_address import WorkAddress


class AddressBook():

    def __init__(self, name):
        self.name = name
        self.addresses = []


    def add_address(self, address):

        if isinstance(address, Address):
            self.addresses.append(address)
        else:
            raise TypeError('Address object must be an instance of Address class')


    def find(self, search_phrase):
        results_list = []

        for element in self.addresses:
            if search_phrase.lower() in element.get_full_address().lower():
                results_list.append(element)

        return results_list


    def sort(self):

        for element in range(len(self.addresses)-1,0,-1):
            for i in range(len(self.addresses)-1):
                if self.addresses[i].get_full_address() > self.addresses[i+1].get_full_address():
                    temp = self.addresses[i]
                    self.addresses[i] = self.addresses[i+1]
                    self.addresses[i+1] = temp

        return self.addresses

    @staticmethod
    def load_items_from_file(file_name):

        if file_name:
            with open (file_name, 'r') as csv_file:
                list_of_items = reader(csv_file, delimiter = ',')
                item_list = []
                for row in list_of_items:
                    item_list.append(row)
            return item_list
        else:
            raise FileNotFoundError

    @staticmethod
    def create_from_csv(list_name, csv_path):
        database_list = AddressBook.load_items_from_file(csv_path)
        database_list.remove(database_list[0])

        book = AddressBook(list_name)

        for element in database_list:
            if element[4] == '':
                address = Address(element[0], element[1], element[2], element[3])
                book.add_address(address)
            else:
                address = WorkAddress(element[0], element[1], element[2], element[3], element[4])
                book.add_address(address)

        return book
