"""
CLI interface for the barbershop management system.
"""
import os
from typing import Optional
from datetime import datetime
from .storage import StorageManager
from .controllers import (
    CustomerController, BarberController,
    ServiceController, AppointmentController
)


class BarbershopCLI:
    """Command-line interface for the barbershop management system."""
    
    def __init__(self):
        """Initialize the CLI with all controllers."""
        # Get the absolute path to the data directory
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        data_dir = os.path.join(base_dir, "data")
        
        self.storage = StorageManager(data_dir)
        self.customer_ctrl = CustomerController(self.storage)
        self.barber_ctrl = BarberController(self.storage)
        self.service_ctrl = ServiceController(self.storage)
        self.appointment_ctrl = AppointmentController(self.storage)
    
    def clear_screen(self):
        """Clear the terminal screen."""
        os.system('clear' if os.name != 'nt' else 'cls')
    
    def print_header(self, title: str):
        """Print a formatted header."""
        print("\n" + "=" * 60)
        print(f"  {title}")
        print("=" * 60 + "\n")
    
    def wait_for_enter(self):
        """Wait for user to press Enter."""
        input("\nPress Enter to continue...")
    
    def run(self):
        """Run the main CLI loop."""
        while True:
            self.clear_screen()
            self.print_header("BARBERSHOP MANAGEMENT SYSTEM")
            print("1. Customer Management")
            print("2. Barber Management")
            print("3. Service Management")
            print("4. Appointment Management")
            print("5. Exit")
            
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == "1":
                self.customer_menu()
            elif choice == "2":
                self.barber_menu()
            elif choice == "3":
                self.service_menu()
            elif choice == "4":
                self.appointment_menu()
            elif choice == "5":
                print("\nThank you for using Barbershop Management System!")
                break
            else:
                print("Invalid choice. Please try again.")
                self.wait_for_enter()
    
    # Customer Management
    def customer_menu(self):
        """Display customer management menu."""
        while True:
            self.clear_screen()
            self.print_header("CUSTOMER MANAGEMENT")
            print("1. Add Customer")
            print("2. View All Customers")
            print("3. Search Customer")
            print("4. Update Customer")
            print("5. Delete Customer")
            print("6. Back to Main Menu")
            
            choice = input("\nEnter your choice (1-6): ").strip()
            
            if choice == "1":
                self.add_customer()
            elif choice == "2":
                self.view_all_customers()
            elif choice == "3":
                self.search_customer()
            elif choice == "4":
                self.update_customer()
            elif choice == "5":
                self.delete_customer()
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please try again.")
                self.wait_for_enter()
    
    def add_customer(self):
        """Add a new customer."""
        self.clear_screen()
        self.print_header("ADD NEW CUSTOMER")
        
        name = input("Enter customer name: ").strip()
        if not name:
            print("Error: Name cannot be empty.")
            self.wait_for_enter()
            return
        
        phone = input("Enter phone number: ").strip()
        if not phone:
            print("Error: Phone cannot be empty.")
            self.wait_for_enter()
            return
        
        email = input("Enter email (optional, press Enter to skip): ").strip()
        email = email if email else None
        
        try:
            customer = self.customer_ctrl.add_customer(name, phone, email)
            print(f"\n✓ Customer added successfully!")
            print(f"  ID: {customer.customer_id}")
            print(f"  Name: {customer.name}")
            print(f"  Phone: {customer.phone}")
            if customer.email:
                print(f"  Email: {customer.email}")
        except Exception as e:
            print(f"\n✗ Error adding customer: {e}")
        
        self.wait_for_enter()
    
    def view_all_customers(self):
        """View all customers."""
        self.clear_screen()
        self.print_header("ALL CUSTOMERS")
        
        customers = self.customer_ctrl.list_all()
        
        if not customers:
            print("No customers found.")
        else:
            for customer in customers:
                print(f"\nID: {customer.customer_id}")
                print(f"Name: {customer.name}")
                print(f"Phone: {customer.phone}")
                if customer.email:
                    print(f"Email: {customer.email}")
                print("-" * 40)
        
        self.wait_for_enter()
    
    def search_customer(self):
        """Search for a customer."""
        self.clear_screen()
        self.print_header("SEARCH CUSTOMER")
        
        query = input("Enter name or phone to search: ").strip()
        if not query:
            print("Error: Search query cannot be empty.")
            self.wait_for_enter()
            return
        
        customers = self.customer_ctrl.search_customers(query)
        
        if not customers:
            print(f"\nNo customers found matching '{query}'.")
        else:
            print(f"\nFound {len(customers)} customer(s):")
            for customer in customers:
                print(f"\nID: {customer.customer_id}")
                print(f"Name: {customer.name}")
                print(f"Phone: {customer.phone}")
                if customer.email:
                    print(f"Email: {customer.email}")
                print("-" * 40)
        
        self.wait_for_enter()
    
    def update_customer(self):
        """Update a customer."""
        self.clear_screen()
        self.print_header("UPDATE CUSTOMER")
        
        customer_id = input("Enter customer ID: ").strip()
        customer = self.customer_ctrl.get_customer(customer_id)
        
        if not customer:
            print(f"Error: Customer with ID '{customer_id}' not found.")
            self.wait_for_enter()
            return
        
        print(f"\nCurrent details:")
        print(f"Name: {customer.name}")
        print(f"Phone: {customer.phone}")
        print(f"Email: {customer.email or 'N/A'}")
        
        print("\nEnter new details (press Enter to keep current value):")
        name = input(f"Name [{customer.name}]: ").strip()
        phone = input(f"Phone [{customer.phone}]: ").strip()
        email = input(f"Email [{customer.email or 'N/A'}]: ").strip()
        
        name = name if name else None
        phone = phone if phone else None
        email = email if email else None
        
        if self.customer_ctrl.update_customer(customer_id, name, phone, email):
            print("\n✓ Customer updated successfully!")
        else:
            print("\n✗ Error updating customer.")
        
        self.wait_for_enter()
    
    def delete_customer(self):
        """Delete a customer."""
        self.clear_screen()
        self.print_header("DELETE CUSTOMER")
        
        customer_id = input("Enter customer ID: ").strip()
        customer = self.customer_ctrl.get_customer(customer_id)
        
        if not customer:
            print(f"Error: Customer with ID '{customer_id}' not found.")
            self.wait_for_enter()
            return
        
        print(f"\nCustomer to delete:")
        print(f"Name: {customer.name}")
        print(f"Phone: {customer.phone}")
        
        confirm = input("\nAre you sure you want to delete this customer? (yes/no): ").strip().lower()
        
        if confirm == "yes":
            if self.customer_ctrl.delete_customer(customer_id):
                print("\n✓ Customer deleted successfully!")
            else:
                print("\n✗ Error deleting customer.")
        else:
            print("\nDeletion cancelled.")
        
        self.wait_for_enter()
    
    # Barber Management
    def barber_menu(self):
        """Display barber management menu."""
        while True:
            self.clear_screen()
            self.print_header("BARBER MANAGEMENT")
            print("1. Add Barber")
            print("2. View All Barbers")
            print("3. Update Barber")
            print("4. Delete Barber")
            print("5. Back to Main Menu")
            
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == "1":
                self.add_barber()
            elif choice == "2":
                self.view_all_barbers()
            elif choice == "3":
                self.update_barber()
            elif choice == "4":
                self.delete_barber()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")
                self.wait_for_enter()
    
    def add_barber(self):
        """Add a new barber."""
        self.clear_screen()
        self.print_header("ADD NEW BARBER")
        
        name = input("Enter barber name: ").strip()
        if not name:
            print("Error: Name cannot be empty.")
            self.wait_for_enter()
            return
        
        specialty = input("Enter specialty (optional, press Enter to skip): ").strip()
        specialty = specialty if specialty else None
        
        phone = input("Enter phone number (optional, press Enter to skip): ").strip()
        phone = phone if phone else None
        
        try:
            barber = self.barber_ctrl.add_barber(name, specialty, phone)
            print(f"\n✓ Barber added successfully!")
            print(f"  ID: {barber.barber_id}")
            print(f"  Name: {barber.name}")
            if barber.specialty:
                print(f"  Specialty: {barber.specialty}")
            if barber.phone:
                print(f"  Phone: {barber.phone}")
        except Exception as e:
            print(f"\n✗ Error adding barber: {e}")
        
        self.wait_for_enter()
    
    def view_all_barbers(self):
        """View all barbers."""
        self.clear_screen()
        self.print_header("ALL BARBERS")
        
        barbers = self.barber_ctrl.list_all()
        
        if not barbers:
            print("No barbers found.")
        else:
            for barber in barbers:
                print(f"\nID: {barber.barber_id}")
                print(f"Name: {barber.name}")
                if barber.specialty:
                    print(f"Specialty: {barber.specialty}")
                if barber.phone:
                    print(f"Phone: {barber.phone}")
                print("-" * 40)
        
        self.wait_for_enter()
    
    def update_barber(self):
        """Update a barber."""
        self.clear_screen()
        self.print_header("UPDATE BARBER")
        
        barber_id = input("Enter barber ID: ").strip()
        barber = self.barber_ctrl.get_barber(barber_id)
        
        if not barber:
            print(f"Error: Barber with ID '{barber_id}' not found.")
            self.wait_for_enter()
            return
        
        print(f"\nCurrent details:")
        print(f"Name: {barber.name}")
        print(f"Specialty: {barber.specialty or 'N/A'}")
        print(f"Phone: {barber.phone or 'N/A'}")
        
        print("\nEnter new details (press Enter to keep current value):")
        name = input(f"Name [{barber.name}]: ").strip()
        specialty = input(f"Specialty [{barber.specialty or 'N/A'}]: ").strip()
        phone = input(f"Phone [{barber.phone or 'N/A'}]: ").strip()
        
        name = name if name else None
        specialty = specialty if specialty else None
        phone = phone if phone else None
        
        if self.barber_ctrl.update_barber(barber_id, name, specialty, phone):
            print("\n✓ Barber updated successfully!")
        else:
            print("\n✗ Error updating barber.")
        
        self.wait_for_enter()
    
    def delete_barber(self):
        """Delete a barber."""
        self.clear_screen()
        self.print_header("DELETE BARBER")
        
        barber_id = input("Enter barber ID: ").strip()
        barber = self.barber_ctrl.get_barber(barber_id)
        
        if not barber:
            print(f"Error: Barber with ID '{barber_id}' not found.")
            self.wait_for_enter()
            return
        
        print(f"\nBarber to delete:")
        print(f"Name: {barber.name}")
        
        confirm = input("\nAre you sure you want to delete this barber? (yes/no): ").strip().lower()
        
        if confirm == "yes":
            if self.barber_ctrl.delete_barber(barber_id):
                print("\n✓ Barber deleted successfully!")
            else:
                print("\n✗ Error deleting barber.")
        else:
            print("\nDeletion cancelled.")
        
        self.wait_for_enter()
    
    # Service Management
    def service_menu(self):
        """Display service management menu."""
        while True:
            self.clear_screen()
            self.print_header("SERVICE MANAGEMENT")
            print("1. Add Service")
            print("2. View All Services")
            print("3. Update Service")
            print("4. Delete Service")
            print("5. Back to Main Menu")
            
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == "1":
                self.add_service()
            elif choice == "2":
                self.view_all_services()
            elif choice == "3":
                self.update_service()
            elif choice == "4":
                self.delete_service()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Please try again.")
                self.wait_for_enter()
    
    def add_service(self):
        """Add a new service."""
        self.clear_screen()
        self.print_header("ADD NEW SERVICE")
        
        name = input("Enter service name: ").strip()
        if not name:
            print("Error: Name cannot be empty.")
            self.wait_for_enter()
            return
        
        try:
            duration = int(input("Enter duration (minutes): ").strip())
            price = float(input("Enter price ($): ").strip())
        except ValueError:
            print("Error: Invalid duration or price.")
            self.wait_for_enter()
            return
        
        description = input("Enter description (optional, press Enter to skip): ").strip()
        description = description if description else None
        
        try:
            service = self.service_ctrl.add_service(name, duration, price, description)
            print(f"\n✓ Service added successfully!")
            print(f"  ID: {service.service_id}")
            print(f"  Name: {service.name}")
            print(f"  Duration: {service.duration} minutes")
            print(f"  Price: ${service.price:.2f}")
            if service.description:
                print(f"  Description: {service.description}")
        except Exception as e:
            print(f"\n✗ Error adding service: {e}")
        
        self.wait_for_enter()
    
    def view_all_services(self):
        """View all services."""
        self.clear_screen()
        self.print_header("ALL SERVICES")
        
        services = self.service_ctrl.list_all()
        
        if not services:
            print("No services found.")
        else:
            for service in services:
                print(f"\nID: {service.service_id}")
                print(f"Name: {service.name}")
                print(f"Duration: {service.duration} minutes")
                print(f"Price: ${service.price:.2f}")
                if service.description:
                    print(f"Description: {service.description}")
                print("-" * 40)
        
        self.wait_for_enter()
    
    def update_service(self):
        """Update a service."""
        self.clear_screen()
        self.print_header("UPDATE SERVICE")
        
        service_id = input("Enter service ID: ").strip()
        service = self.service_ctrl.get_service(service_id)
        
        if not service:
            print(f"Error: Service with ID '{service_id}' not found.")
            self.wait_for_enter()
            return
        
        print(f"\nCurrent details:")
        print(f"Name: {service.name}")
        print(f"Duration: {service.duration} minutes")
        print(f"Price: ${service.price:.2f}")
        print(f"Description: {service.description or 'N/A'}")
        
        print("\nEnter new details (press Enter to keep current value):")
        name = input(f"Name [{service.name}]: ").strip()
        duration_str = input(f"Duration [{service.duration}]: ").strip()
        price_str = input(f"Price [{service.price:.2f}]: ").strip()
        description = input(f"Description [{service.description or 'N/A'}]: ").strip()
        
        name = name if name else None
        duration = int(duration_str) if duration_str else None
        price = float(price_str) if price_str else None
        description = description if description else None
        
        try:
            if self.service_ctrl.update_service(service_id, name, duration, price, description):
                print("\n✓ Service updated successfully!")
            else:
                print("\n✗ Error updating service.")
        except ValueError:
            print("\n✗ Error: Invalid duration or price format.")
        
        self.wait_for_enter()
    
    def delete_service(self):
        """Delete a service."""
        self.clear_screen()
        self.print_header("DELETE SERVICE")
        
        service_id = input("Enter service ID: ").strip()
        service = self.service_ctrl.get_service(service_id)
        
        if not service:
            print(f"Error: Service with ID '{service_id}' not found.")
            self.wait_for_enter()
            return
        
        print(f"\nService to delete:")
        print(f"Name: {service.name}")
        print(f"Price: ${service.price:.2f}")
        
        confirm = input("\nAre you sure you want to delete this service? (yes/no): ").strip().lower()
        
        if confirm == "yes":
            if self.service_ctrl.delete_service(service_id):
                print("\n✓ Service deleted successfully!")
            else:
                print("\n✗ Error deleting service.")
        else:
            print("\nDeletion cancelled.")
        
        self.wait_for_enter()
    
    # Appointment Management
    def appointment_menu(self):
        """Display appointment management menu."""
        while True:
            self.clear_screen()
            self.print_header("APPOINTMENT MANAGEMENT")
            print("1. Create Appointment")
            print("2. View All Appointments")
            print("3. View Appointments by Customer")
            print("4. View Appointments by Barber")
            print("5. Update Appointment")
            print("6. Cancel Appointment")
            print("7. Complete Appointment")
            print("8. Back to Main Menu")
            
            choice = input("\nEnter your choice (1-8): ").strip()
            
            if choice == "1":
                self.create_appointment()
            elif choice == "2":
                self.view_all_appointments()
            elif choice == "3":
                self.view_appointments_by_customer()
            elif choice == "4":
                self.view_appointments_by_barber()
            elif choice == "5":
                self.update_appointment()
            elif choice == "6":
                self.cancel_appointment()
            elif choice == "7":
                self.complete_appointment()
            elif choice == "8":
                break
            else:
                print("Invalid choice. Please try again.")
                self.wait_for_enter()
    
    def create_appointment(self):
        """Create a new appointment."""
        self.clear_screen()
        self.print_header("CREATE NEW APPOINTMENT")
        
        # Show available customers
        customers = self.customer_ctrl.list_all()
        if not customers:
            print("No customers found. Please add a customer first.")
            self.wait_for_enter()
            return
        
        print("Available Customers:")
        for customer in customers:
            print(f"  {customer.customer_id}: {customer.name}")
        
        customer_id = input("\nEnter customer ID: ").strip()
        if not self.customer_ctrl.get_customer(customer_id):
            print("Error: Invalid customer ID.")
            self.wait_for_enter()
            return
        
        # Show available barbers
        barbers = self.barber_ctrl.list_all()
        if not barbers:
            print("\nNo barbers found. Please add a barber first.")
            self.wait_for_enter()
            return
        
        print("\nAvailable Barbers:")
        for barber in barbers:
            print(f"  {barber.barber_id}: {barber.name}")
        
        barber_id = input("\nEnter barber ID: ").strip()
        if not self.barber_ctrl.get_barber(barber_id):
            print("Error: Invalid barber ID.")
            self.wait_for_enter()
            return
        
        # Show available services
        services = self.service_ctrl.list_all()
        if not services:
            print("\nNo services found. Please add a service first.")
            self.wait_for_enter()
            return
        
        print("\nAvailable Services:")
        for service in services:
            print(f"  {service.service_id}: {service.name} (${service.price:.2f})")
        
        service_id = input("\nEnter service ID: ").strip()
        if not self.service_ctrl.get_service(service_id):
            print("Error: Invalid service ID.")
            self.wait_for_enter()
            return
        
        # Get appointment date and time
        print("\nEnter appointment date and time:")
        date_str = input("Date (YYYY-MM-DD): ").strip()
        time_str = input("Time (HH:MM): ").strip()
        
        try:
            appointment_datetime = f"{date_str}T{time_str}:00"
            # Validate datetime format
            datetime.fromisoformat(appointment_datetime)
        except ValueError:
            print("Error: Invalid date or time format.")
            self.wait_for_enter()
            return
        
        notes = input("\nEnter notes (optional, press Enter to skip): ").strip()
        notes = notes if notes else None
        
        try:
            appointment = self.appointment_ctrl.create_appointment(
                customer_id, barber_id, service_id, appointment_datetime, notes
            )
            print(f"\n✓ Appointment created successfully!")
            print(f"  ID: {appointment.appointment_id}")
            print(f"  Date/Time: {appointment.appointment_datetime}")
            print(f"  Status: {appointment.status}")
        except Exception as e:
            print(f"\n✗ Error creating appointment: {e}")
        
        self.wait_for_enter()
    
    def view_all_appointments(self):
        """View all appointments."""
        self.clear_screen()
        self.print_header("ALL APPOINTMENTS")
        
        appointments = self.appointment_ctrl.list_all()
        
        if not appointments:
            print("No appointments found.")
        else:
            for appointment in appointments:
                customer = self.customer_ctrl.get_customer(appointment.customer_id)
                barber = self.barber_ctrl.get_barber(appointment.barber_id)
                service = self.service_ctrl.get_service(appointment.service_id)
                
                print(f"\nID: {appointment.appointment_id}")
                print(f"Customer: {customer.name if customer else 'Unknown'}")
                print(f"Barber: {barber.name if barber else 'Unknown'}")
                print(f"Service: {service.name if service else 'Unknown'}")
                print(f"Date/Time: {appointment.appointment_datetime}")
                print(f"Status: {appointment.status}")
                if appointment.notes:
                    print(f"Notes: {appointment.notes}")
                print("-" * 40)
        
        self.wait_for_enter()
    
    def view_appointments_by_customer(self):
        """View appointments for a specific customer."""
        self.clear_screen()
        self.print_header("APPOINTMENTS BY CUSTOMER")
        
        customer_id = input("Enter customer ID: ").strip()
        customer = self.customer_ctrl.get_customer(customer_id)
        
        if not customer:
            print(f"Error: Customer with ID '{customer_id}' not found.")
            self.wait_for_enter()
            return
        
        print(f"\nAppointments for {customer.name}:")
        appointments = self.appointment_ctrl.get_appointments_by_customer(customer_id)
        
        if not appointments:
            print("No appointments found.")
        else:
            for appointment in appointments:
                barber = self.barber_ctrl.get_barber(appointment.barber_id)
                service = self.service_ctrl.get_service(appointment.service_id)
                
                print(f"\nID: {appointment.appointment_id}")
                print(f"Barber: {barber.name if barber else 'Unknown'}")
                print(f"Service: {service.name if service else 'Unknown'}")
                print(f"Date/Time: {appointment.appointment_datetime}")
                print(f"Status: {appointment.status}")
                print("-" * 40)
        
        self.wait_for_enter()
    
    def view_appointments_by_barber(self):
        """View appointments for a specific barber."""
        self.clear_screen()
        self.print_header("APPOINTMENTS BY BARBER")
        
        barber_id = input("Enter barber ID: ").strip()
        barber = self.barber_ctrl.get_barber(barber_id)
        
        if not barber:
            print(f"Error: Barber with ID '{barber_id}' not found.")
            self.wait_for_enter()
            return
        
        print(f"\nAppointments for {barber.name}:")
        appointments = self.appointment_ctrl.get_appointments_by_barber(barber_id)
        
        if not appointments:
            print("No appointments found.")
        else:
            for appointment in appointments:
                customer = self.customer_ctrl.get_customer(appointment.customer_id)
                service = self.service_ctrl.get_service(appointment.service_id)
                
                print(f"\nID: {appointment.appointment_id}")
                print(f"Customer: {customer.name if customer else 'Unknown'}")
                print(f"Service: {service.name if service else 'Unknown'}")
                print(f"Date/Time: {appointment.appointment_datetime}")
                print(f"Status: {appointment.status}")
                print("-" * 40)
        
        self.wait_for_enter()
    
    def update_appointment(self):
        """Update an appointment."""
        self.clear_screen()
        self.print_header("UPDATE APPOINTMENT")
        
        appointment_id = input("Enter appointment ID: ").strip()
        appointment = self.appointment_ctrl.get_appointment(appointment_id)
        
        if not appointment:
            print(f"Error: Appointment with ID '{appointment_id}' not found.")
            self.wait_for_enter()
            return
        
        customer = self.customer_ctrl.get_customer(appointment.customer_id)
        barber = self.barber_ctrl.get_barber(appointment.barber_id)
        service = self.service_ctrl.get_service(appointment.service_id)
        
        print(f"\nCurrent details:")
        print(f"Customer: {customer.name if customer else 'Unknown'}")
        print(f"Barber: {barber.name if barber else 'Unknown'}")
        print(f"Service: {service.name if service else 'Unknown'}")
        print(f"Date/Time: {appointment.appointment_datetime}")
        
        print("\nEnter new date and time (press Enter to keep current value):")
        date_str = input(f"Date (YYYY-MM-DD) [{appointment.appointment_datetime.split('T')[0]}]: ").strip()
        time_str = input(f"Time (HH:MM) [{appointment.appointment_datetime.split('T')[1][:5]}]: ").strip()
        
        appointment_datetime = None
        if date_str and time_str:
            try:
                appointment_datetime = f"{date_str}T{time_str}:00"
                datetime.fromisoformat(appointment_datetime)
            except ValueError:
                print("Error: Invalid date or time format.")
                self.wait_for_enter()
                return
        
        notes = input(f"Notes [{appointment.notes or 'N/A'}]: ").strip()
        notes = notes if notes else None
        
        if self.appointment_ctrl.update_appointment(appointment_id, appointment_datetime=appointment_datetime, notes=notes):
            print("\n✓ Appointment updated successfully!")
        else:
            print("\n✗ Error updating appointment.")
        
        self.wait_for_enter()
    
    def cancel_appointment(self):
        """Cancel an appointment."""
        self.clear_screen()
        self.print_header("CANCEL APPOINTMENT")
        
        appointment_id = input("Enter appointment ID: ").strip()
        appointment = self.appointment_ctrl.get_appointment(appointment_id)
        
        if not appointment:
            print(f"Error: Appointment with ID '{appointment_id}' not found.")
            self.wait_for_enter()
            return
        
        customer = self.customer_ctrl.get_customer(appointment.customer_id)
        print(f"\nAppointment to cancel:")
        print(f"Customer: {customer.name if customer else 'Unknown'}")
        print(f"Date/Time: {appointment.appointment_datetime}")
        
        confirm = input("\nAre you sure you want to cancel this appointment? (yes/no): ").strip().lower()
        
        if confirm == "yes":
            if self.appointment_ctrl.cancel_appointment(appointment_id):
                print("\n✓ Appointment cancelled successfully!")
            else:
                print("\n✗ Error cancelling appointment.")
        else:
            print("\nCancellation aborted.")
        
        self.wait_for_enter()
    
    def complete_appointment(self):
        """Mark an appointment as completed."""
        self.clear_screen()
        self.print_header("COMPLETE APPOINTMENT")
        
        appointment_id = input("Enter appointment ID: ").strip()
        appointment = self.appointment_ctrl.get_appointment(appointment_id)
        
        if not appointment:
            print(f"Error: Appointment with ID '{appointment_id}' not found.")
            self.wait_for_enter()
            return
        
        customer = self.customer_ctrl.get_customer(appointment.customer_id)
        print(f"\nAppointment to complete:")
        print(f"Customer: {customer.name if customer else 'Unknown'}")
        print(f"Date/Time: {appointment.appointment_datetime}")
        
        confirm = input("\nMark this appointment as completed? (yes/no): ").strip().lower()
        
        if confirm == "yes":
            if self.appointment_ctrl.complete_appointment(appointment_id):
                print("\n✓ Appointment marked as completed!")
            else:
                print("\n✗ Error completing appointment.")
        else:
            print("\nOperation cancelled.")
        
        self.wait_for_enter()


def main():
    """Main entry point for the application."""
    cli = BarbershopCLI()
    cli.run()


if __name__ == "__main__":
    main()
