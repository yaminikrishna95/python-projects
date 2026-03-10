class Room:

	def __init__(self, room_number, room_type, price,total_rooms):

		self.room_number = room_number
		self.room_type = room_type
		self.price = price
		self.total_rooms = total_rooms
		self.is_available = True


	def display_room(self):
		print(f"Room Number: {self.room_number}")
		print(f"Room Type: {self.room_type}")
		print(f"Price: {self.price}")
		print(f"Total Rooms Available: {self.total_rooms}")
		print(f"Available: {self.is_available}")

room_1= Room(room_number=1, room_type='2 Queen', price=150,total_rooms=10)
room_2= Room(room_number=2, room_type='1 King', price=200,total_rooms=10)
room_3= Room(room_number=3, room_type='Single Bed', price=100,total_rooms=10)

room_1.display_room()
