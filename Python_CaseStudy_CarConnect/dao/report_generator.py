# util/report_generator.py
from entity.reservation import Reservation
from entity.vehicle import Vehicle

class ReportGenerator:
    @staticmethod
    def generate_reservation_report(reservations):
        print("Reservation Report:")
        print("----------------------------------------------------------")
        print("{:<15} {:<15} {:<15} {:<20} {:<20} {:<15} {:<10}".format(
            "Reservation ID", "Customer ID", "Vehicle ID", "Start Date", "End Date", "Total Cost", "Status"
        ))
        print("----------------------------------------------------------")
        for reservation in reservations:
            print("{:<15} {:<15} {:<15} {:<20} {:<20} {:<15} {:<10}".format(
                reservation.reservation_id, reservation.customer_id, reservation.vehicle_id,
                str(reservation.start_date), str(reservation.end_date),
                reservation.total_cost, reservation.status
            ))
        print()

    @staticmethod
    def generate_vehicle_report(vehicles):
        print("Vehicle Report:")
        print("--------------------------------------------------------")
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<10}".format(
            "Vehicle ID", "Model", "Make", "Year", "Color", "Registration Number", "Availability", "Daily Rate"
        ))
        print("--------------------------------------------------------")
        for vehicle in vehicles:
            print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<10}".format(
                vehicle.vehicle_id, vehicle.model, vehicle.make, vehicle.year, vehicle.color,
                vehicle.registration_number, "Available" if vehicle.availability else "Not Available",
                vehicle.daily_rate
            ))
        print()
