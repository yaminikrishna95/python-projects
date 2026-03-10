class Booking:
    def __init__(self, booking_id, customer, room, check_in, check_out):
        self.booking_id = booking_id
        self.customer = customer
        self.room = room
        self.check_in = check_in
        self.check_out = check_out

    def display_booking(self):
        print(f"Booking ID: {self.booking_id}")
        print(f"Customer: {self.customer}")
        print(f"Room: {self.room}")
        print(f"Check-in: {self.check_in}")
        print(f"Check-out: {self.check_out}")

booking1 = Booking(
    101,
    "customer1",
    "room1",
    "2026-03-10",
    "2026-03-12"
)

booking1.display_booking()