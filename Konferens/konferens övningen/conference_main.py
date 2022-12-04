
import conference_databases
import conference_classes

conference_databases.populate_db()
print(conference_databases.view_db())  

conference_classes.Hall.create_halls_objects()



def menu():
    booking = conference_classes.Booking()
    while True:
        choice = input("""
press 1 to view our conference halls
press 2 to book your conference hall
press 3 to delete booked conference hall
press 4 to complete your booking
press 5 to see all bookings """)
        
        if choice == "1":
            conference_classes.Hall.show_halls()
        if choice == "2":
            booking.book_hall()
        if choice == "3":
            booking.delete_booking()
        if choice == "4":
            booking.save_booking()
        if choice == "5":
            booking.list_bookings()
            
menu()   

  

  
       