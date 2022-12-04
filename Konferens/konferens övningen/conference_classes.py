from zoneinfo import available_timezones
import conference_databases as cd


halls = []

class Hall():
    def __init__(self, name,seats,price):
        self.name = name
        self.seats = seats
        self.price = price
        self.status = "Available"
    
        
        
    def __str__(self):
        return (f"{self.name} seats{self.seats} costs {self.price}kr")
    
    def __repr__(self):
        return (f"{self.name} seats{self.seats} costs {self.price}kr")
    @staticmethod
    def show_halls():
        name_list = [f"{obj.name}: {obj.status}" for obj in halls]
        print("\n".join([*name_list]))    
     
    @staticmethod  
    # it's decorator
    def create_halls_objects():
        global halls
        cd.cursor.execute("SELECT * from halls")
        db_content = cd.cursor.fetchall()
        for item in db_content:
            halls.append(Hall(item[1],item[2],item[3]))
        if not db_content:
            print("database is empty")
            
        return halls
        
        
class Booking():
    def __init__ (self):
        self.booked_halls = []
        self.time = None
        self.name = None
        self.phone = None
        
    def __str__(self):
        if self.booked_halls:
            return "\n".join([f"{obj.name} booked by {self.name} for {self.time}" for obj in self.booked_halls])
        else:
            return "You booking is empty"
    
    def __repr__(self):
        if self.booked_halls:
            return "\n".join([f"{obj.name} booked by {self.name} for {self.time}" for obj in self.booked_halls])
        else:
            return "You booking is empty"
    def book_hall(self):
        hall_name = input("Which hall would you like to book? ").lower()
        
        hall = next(obj for obj in halls if obj.name == hall_name )
        if hall.status == "Available":
            hall_time = input("Which time? ")
            username = input("What is your name? ")
            user_phone = input("What is your phone number? ")
            self.booked_halls.append(hall)
            hall.status = "Booked"
            self.time = hall_time
            self.name = username
            self.phone = user_phone
        else:
            print("This hall is not available ")
    def save_booking(self):
        cd.cursor.execute(
            "INSERT OR IGNORE INTO customers ('name', 'phone_number') VALUES (?, ?)", (self.name, self.phone))
       
            
            
        id = cd.cursor.execute("SELECT id FROM customers WHERE name = ? ", (self.name,))
        id = list(id)[0][0]
        content = str(self)
        total = 0
        for item in self.booked_halls:
            total += item.price
            
        cd.cursor.execute(
            "INSERT INTO bookings ('customer_id', 'content', 'total') VALUES (?, ?, ?)", (id, content, total,))
        print("Your booking has been saved ")
        
    def delete_booking(self):
        hall_name = input("Which hall would you like to delete? ").lower()
        
        hall = next(obj for obj in halls if obj.name == hall_name )
        if hall.status == "Booked":
            self.booked_halls.remove(hall)
            hall.status = "Available"
        if not self.booked_halls:
            print("No bookings available")
            
        
        
    def list_bookings(self):
        cd.cursor.execute("SELECT * from bookings")
        db_contents = cd.cursor.fetchall()
        for item in db_contents:
            print(item)
        
   
        

if __name__ == "__main__":
    pass
    

