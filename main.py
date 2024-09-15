class Theatre:
    def __init__(self, rows=5, seats_per_row=10):  # Corrected constructor method
        # Initialize the seating arrangement with empty ('O') seats
        self.rows = rows
        self.seats_per_row = seats_per_row
        self.seating = [['O' for _ in range(seats_per_row)] for _ in range(rows)]

    def display_seating(self):
        print("\nTheatre Seating Arrangement:")
        print("  " + " ".join([str(i+1).rjust(2, ' ') for i in range(self.seats_per_row)]))
        for i, row in enumerate(self.seating):
            print(chr(65+i) + " " + " ".join(row))

    def check_availability(self, row, seat):
        # Check if the selected seat is available
        return self.seating[row][seat] == 'O'

    def book_seat(self, row, seat):
        if self.check_availability(row, seat):
            self.seating[row][seat] = 'X'
            print(f"\nSeat {chr(65+row)}{seat+1} has been successfully booked!")
        else:
            print(f"\nSorry, Seat {chr(65+row)}{seat+1} is already booked.")

    def view_booked_seats(self):
        print("\nBooked Seats:")
        booked = []
        for i, row in enumerate(self.seating):
            for j, seat in enumerate(row):
                if seat == 'X':
                    booked.append(f"{chr(65+i)}{j+1}")
        if booked:
            print(", ".join(booked))
        else:
            print("No seats have been booked yet.")


def main():
    theatre = Theatre()

    while True:
        print("\n----- Theatre Booking System -----")
        print("1. View Seating Arrangement")
        print("2. Book a Seat")
        print("3. View Booked Seats")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            theatre.display_seating()
        elif choice == '2':
            theatre.display_seating()
            row = input("\nEnter the row (A-E): ").upper()
            seat = int(input("Enter the seat number (1-10): ")) - 1

            if row.isalpha() and 'A' <= row <= chr(65+theatre.rows-1) and 0 <= seat < theatre.seats_per_row:
                theatre.book_seat(ord(row) - 65, seat)
            else:
                print("\nInvalid row or seat number. Please try again.")
        elif choice == '3':
            theatre.view_booked_seats()
        elif choice == '4':
            print("Thank you for using the Theatre Booking System!")
            break
        else:
            print("Invalid choice. Please select from the options.")
if __name__ == "__main__":
    main()
