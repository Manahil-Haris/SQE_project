# testing.py
import unittest
from project import TrainModule, PassengerModule, BookingModule


class TestRailwaySystem(unittest.TestCase):

    def setUp(self):
        # Initialize modules
        self.train_module = TrainModule()
        self.passenger_module = PassengerModule()
        self.booking_module = BookingModule(self.train_module)

        # Add sample train and passenger
        self.train_module.add_train(101, "Express", "Lahore-Karachi", 2)
        self.passenger_module.add_passenger(1, "Manahil", "0300-1234567")

    # ---------- Train Module Tests ----------
    def test_add_train(self):
        self.train_module.add_train(102, "FastTrack", "Rawalpindi-Lahore", 50)
        self.assertIn(102, self.train_module.trains)

    def test_update_train(self):
        self.train_module.update_train(101, 10)
        self.assertEqual(self.train_module.trains[101].seats, 10)

    def test_delete_train(self):
        self.train_module.delete_train(101)
        self.assertNotIn(101, self.train_module.trains)

    def test_view_schedule(self):
        schedule = self.train_module.view_schedule()
        self.assertTrue(len(schedule) > 0)

    def test_search_by_route(self):
        result = self.train_module.search_by_route("Lahore-Karachi")
        self.assertEqual(result[0].name, "Express")

    # ---------- Passenger Module Tests ----------
    def test_add_passenger(self):
        self.passenger_module.add_passenger(2, "Ali", "0300-7654321")
        self.assertIn(2, self.passenger_module.passengers)

    def test_update_passenger(self):
        self.passenger_module.update_passenger(1, "0300-9999999")
        self.assertEqual(self.passenger_module.passengers[1].contact, "0300-9999999")

    def test_delete_passenger(self):
        self.passenger_module.delete_passenger(1)
        self.assertNotIn(1, self.passenger_module.passengers)

    def test_view_passengers(self):
        passengers = self.passenger_module.view_passengers()
        self.assertTrue(len(passengers) > 0)

    def test_search_passenger(self):
        passenger = self.passenger_module.search_passenger(1)
        self.assertEqual(passenger.name, "Manahil")

    # ---------- Booking Module Tests ----------
    def test_book_ticket_success(self):
        result = self.booking_module.book_ticket(201, 1, 101)
        self.assertEqual(result, "Ticket booked successfully!")

    def test_book_ticket_failure(self):
        # Book twice to exhaust seats
        self.booking_module.book_ticket(201, 1, 101)
        self.booking_module.book_ticket(202, 1, 101)
        result = self.booking_module.book_ticket(203, 1, 101)
        self.assertEqual(result, "Booking failed. Train not found or no seats.")

    def test_cancel_ticket(self):
        self.booking_module.book_ticket(201, 1, 101)
        result = self.booking_module.cancel_ticket(201)
        self.assertEqual(result, "Ticket cancelled successfully!")

    def test_view_bookings(self):
        self.booking_module.book_ticket(201, 1, 101)
        bookings = self.booking_module.view_bookings()
        self.assertTrue(len(bookings) > 0)

    def test_search_booking(self):
        self.booking_module.book_ticket(201, 1, 101)
        result = self.booking_module.search_booking(1)
        self.assertEqual(result[0].passenger_id, 1)

    def test_check_availability(self):
        seats = self.booking_module.check_availability(101)
        self.assertIsInstance(seats, int)

if __name__ == "__main__":
    unittest.main()
