import csv

class csv_manager:
    def __init__(self):
        self.menu_file_path = "assets/item_menu.csv"
        self.customer_file_path = "assets/customers.csv"
    
    def write_to_menu(self, data:list[list]):
        with open(self.menu_file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)

    def read_from_menu(self) -> list[list]:
        menu_items = []
        with open(self.menu_file_path, mode ='r')as file:
          csvFile = csv.reader(file)
          for lines in csvFile:
                menu_items.append(list(lines))
        
        return menu_items

    def write_to_customers(self):
        pass

    def read_from_customers(self):
        pass