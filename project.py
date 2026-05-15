
class Train:
    def __init__(self, train_id, name, route, seats):
        self.train_id = train_id
        self.name = name
        self.route = route
        self.seats = seats

class TrainModule:
    def __init__(self):
        self.trains = {}

    def add_train(self, train_id, name, route, seats):
        self.trains[train_id] = Train(train_id, name, route, seats)

    def update_train(self, train_id, seats):
        if train_id in self.trains:
            self.trains[train_id].seats = seats

    def delete_train(self, train_id):
        if train_id in self.trains:
            del self.trains[train_id]

    def view_schedule(self):
        return [(t.train_id, t.name, t.route, t.seats) for t in self.trains.values()]

    def search_by_route(self, route):
        return [t for t in self.trains.values() if t.route == route]


class Passenger:
    def __init__(self, passenger_id, name, contact):
        self.passenger_id = passenger_id
        self.name = name
        self.contact = contact

class PassengerModule:
    def __init__(self):
        self.passengers = {}

    def add_passenger(self, passenger_id, name, contact):
        self.passengers[passenger_id] = Passenger(passenger_id, name, contact)

    def update_passenger(self, passenger_id, contact):
        if passenger_id in self.passengers:
            self.passengers[passenger_id].contact = contact

    def delete_passenger(self, passenger_id):
        if passenger_id in self.passengers:
            del self.passengers[passenger_id]

    def view_passengers(self):
        return [(p.passenger_id, p.name, p.contact) for p in self.passengers.values()]

    def search_passenger(self, passenger_id):
        return self.passengers.get(passenger_id, None)

class Booking:
    def __init__(self, booking_id, passenger_id, train_id):
        self.booking_id = booking_id
        self.passenger_id = passenger_id
        self.train_id = train_id

class BookingModule:
    def __init__(self, train_module):
        self.bookings = {}
        self.train_module = train_module

    def book_ticket(self, booking_id, passenger_id, train_id):
        train = self.train_module.trains.get(train_id)
        if train and train.seats > 0:
            train.seats -= 1
            self.bookings[booking_id] = Booking(booking_id, passenger_id, train_id)
            return "Ticket booked successfully!"
        return "Booking failed. Train not found or no seats."

    def cancel_ticket(self, booking_id):
        if booking_id in self.bookings:
            train_id = self.bookings[booking_id].train_id
            self.train_module.trains[train_id].seats += 1
            del self.bookings[booking_id]
            return "Ticket cancelled successfully!"
        return "Cancellation failed."

    def view_bookings(self):
        return [(b.booking_id, b.passenger_id, b.train_id) for b in self.bookings.values()]

    def search_booking(self, passenger_id):
        return [b for b in self.bookings.values() if b.passenger_id == passenger_id]

    def check_availability(self, train_id):
        train = self.train_module.trains.get(train_id)
        return train.seats if train else "Train not found"

