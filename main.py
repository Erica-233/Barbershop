"""
Barbershop Management System
A simple CLI-based system to manage barbershop operations including customers,
barbers, services, and appointments.
"""

import sqlite3
import os


DB_NAME = "barbershop.db"


def init_db():
    """Initialize the database using schema.sql file."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Read and execute the schema file
    schema_path = os.path.join(os.path.dirname(__file__), "schema.sql")
    with open(schema_path, 'r') as schema_file:
        schema_sql = schema_file.read()
        cursor.executescript(schema_sql)
    
    conn.commit()
    conn.close()
    print(f"Database '{DB_NAME}' initialized successfully.")


def add_customer(name, phone):
    """Add a new customer to the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    try:
        cursor.execute(
            "INSERT INTO customers (name, phone) VALUES (?, ?)",
            (name, phone)
        )
        conn.commit()
        customer_id = cursor.lastrowid
        print(f"Customer '{name}' added successfully with ID: {customer_id}")
        return customer_id
    except sqlite3.IntegrityError as e:
        print(f"Error adding customer: {e}")
        return None
    finally:
        conn.close()


def add_barber(name):
    """Add a new barber to the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute(
        "INSERT INTO barbers (name, status) VALUES (?, ?)",
        (name, "available")
    )
    conn.commit()
    barber_id = cursor.lastrowid
    conn.close()
    
    print(f"Barber '{name}' added successfully with ID: {barber_id}")
    return barber_id


def add_service(name, price):
    """Add a new service to the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute(
        "INSERT INTO services (name, price) VALUES (?, ?)",
        (name, price)
    )
    conn.commit()
    service_id = cursor.lastrowid
    conn.close()
    
    print(f"Service '{name}' added successfully with ID: {service_id} (Price: ${price})")
    return service_id


def book_appointment(customer_id, barber_id, service_id, date):
    """Create a new appointment."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    try:
        cursor.execute(
            """INSERT INTO appointments 
               (customer_id, barber_id, service_id, appointment_date, status) 
               VALUES (?, ?, ?, ?, ?)""",
            (customer_id, barber_id, service_id, date, "scheduled")
        )
        conn.commit()
        appointment_id = cursor.lastrowid
        print(f"Appointment booked successfully with ID: {appointment_id}")
        return appointment_id
    except sqlite3.IntegrityError as e:
        print(f"Error booking appointment: {e}")
        return None
    finally:
        conn.close()


def get_appointments():
    """List all appointments with details (joins to get names)."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT 
            a.id,
            c.name AS customer_name,
            b.name AS barber_name,
            s.name AS service_name,
            s.price,
            a.appointment_date,
            a.status
        FROM appointments a
        JOIN customers c ON a.customer_id = c.id
        JOIN barbers b ON a.barber_id = b.id
        JOIN services s ON a.service_id = s.id
        ORDER BY a.appointment_date
    """)
    
    appointments = cursor.fetchall()
    conn.close()
    
    if not appointments:
        print("No appointments found.")
        return []
    
    print("\n=== Appointments ===")
    print(f"{'ID':<5} {'Customer':<15} {'Barber':<15} {'Service':<15} {'Price':<10} {'Date':<20} {'Status':<10}")
    print("-" * 100)
    
    for apt in appointments:
        apt_id, customer, barber, service, price, date, status = apt
        print(f"{apt_id:<5} {customer:<15} {barber:<15} {service:<15} ${price:<9.2f} {date:<20} {status:<10}")
    
    return appointments


def main():
    """Main execution block to demonstrate the functionality."""
    print("=== Barbershop Management System ===\n")
    
    # Initialize the database
    init_db()
    
    print("\n--- Adding Sample Data ---\n")
    
    # Add sample customers
    customer1_id = add_customer("John Doe", "555-0101")
    customer2_id = add_customer("Jane Smith", "555-0102")
    
    # Add sample barbers
    barber1_id = add_barber("Mike Johnson")
    barber2_id = add_barber("Sarah Williams")
    
    # Add sample services
    service1_id = add_service("Haircut", 25.00)
    service2_id = add_service("Shave", 15.00)
    service3_id = add_service("Haircut & Shave", 35.00)
    
    print("\n--- Booking Appointments ---\n")
    
    # Book sample appointments
    book_appointment(customer1_id, barber1_id, service1_id, "2024-01-15 10:00:00")
    book_appointment(customer2_id, barber2_id, service3_id, "2024-01-15 11:00:00")
    book_appointment(customer1_id, barber2_id, service2_id, "2024-01-16 14:00:00")
    
    print("\n--- Retrieving All Appointments ---\n")
    
    # Display all appointments
    get_appointments()
    
    print("\n=== Demo Complete ===")


if __name__ == "__main__":
    main()
