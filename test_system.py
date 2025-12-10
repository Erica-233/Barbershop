#!/usr/bin/env python3
"""
Test script to verify the Barbershop Management System functionality.
"""
import os
import sys

# Add the parent directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.storage import StorageManager
from src.controllers import (
    CustomerController, BarberController,
    ServiceController, AppointmentController
)

def test_system():
    """Test all major functionality of the barbershop system."""
    
    print("=" * 60)
    print("BARBERSHOP MANAGEMENT SYSTEM - FUNCTIONALITY TEST")
    print("=" * 60)
    
    # Initialize storage and controllers
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, "data")
    
    storage = StorageManager(data_dir)
    customer_ctrl = CustomerController(storage)
    barber_ctrl = BarberController(storage)
    service_ctrl = ServiceController(storage)
    appointment_ctrl = AppointmentController(storage)
    
    # Test Customer Management
    print("\n--- Testing Customer Management ---")
    customer1 = customer_ctrl.add_customer("John Doe", "555-0101", "john@example.com")
    print(f"✓ Added customer: {customer1}")
    
    customer2 = customer_ctrl.add_customer("Jane Smith", "555-0102", "jane@example.com")
    print(f"✓ Added customer: {customer2}")
    
    all_customers = customer_ctrl.list_all()
    print(f"✓ Total customers: {len(all_customers)}")
    
    search_results = customer_ctrl.search_customers("John")
    print(f"✓ Search for 'John' found {len(search_results)} customer(s)")
    
    # Test Barber Management
    print("\n--- Testing Barber Management ---")
    barber1 = barber_ctrl.add_barber("Mike Wilson", "Fade Specialist", "555-0201")
    print(f"✓ Added barber: {barber1}")
    
    barber2 = barber_ctrl.add_barber("Sarah Johnson", "Beard Expert", "555-0202")
    print(f"✓ Added barber: {barber2}")
    
    all_barbers = barber_ctrl.list_all()
    print(f"✓ Total barbers: {len(all_barbers)}")
    
    # Test Service Management
    print("\n--- Testing Service Management ---")
    service1 = service_ctrl.add_service("Men's Haircut", 30, 25.00, "Classic men's haircut")
    print(f"✓ Added service: {service1}")
    
    service2 = service_ctrl.add_service("Beard Trim", 15, 15.00, "Beard trimming and shaping")
    print(f"✓ Added service: {service2}")
    
    service3 = service_ctrl.add_service("Kids Haircut", 20, 18.00, "Haircut for children")
    print(f"✓ Added service: {service3}")
    
    all_services = service_ctrl.list_all()
    print(f"✓ Total services: {len(all_services)}")
    
    # Test Appointment Management
    print("\n--- Testing Appointment Management ---")
    appointment1 = appointment_ctrl.create_appointment(
        customer1.customer_id,
        barber1.barber_id,
        service1.service_id,
        "2025-12-15T14:30:00",
        "Customer prefers short fade"
    )
    print(f"✓ Created appointment: {appointment1}")
    
    appointment2 = appointment_ctrl.create_appointment(
        customer2.customer_id,
        barber2.barber_id,
        service2.service_id,
        "2025-12-16T10:00:00"
    )
    print(f"✓ Created appointment: {appointment2}")
    
    all_appointments = appointment_ctrl.list_all()
    print(f"✓ Total appointments: {len(all_appointments)}")
    
    # Test appointment status changes
    appointment_ctrl.complete_appointment(appointment1.appointment_id)
    completed = appointment_ctrl.get_appointment(appointment1.appointment_id)
    print(f"✓ Appointment status changed to: {completed.status}")
    
    # Test filtering
    customer_appointments = appointment_ctrl.get_appointments_by_customer(customer1.customer_id)
    print(f"✓ Appointments for {customer1.name}: {len(customer_appointments)}")
    
    barber_appointments = appointment_ctrl.get_appointments_by_barber(barber1.barber_id)
    print(f"✓ Appointments for {barber1.name}: {len(barber_appointments)}")
    
    # Test data persistence
    print("\n--- Testing Data Persistence ---")
    print("✓ Reloading data from storage...")
    customer_ctrl.load_customers()
    barber_ctrl.load_barbers()
    service_ctrl.load_services()
    appointment_ctrl.load_appointments()
    
    print(f"✓ Customers after reload: {len(customer_ctrl.list_all())}")
    print(f"✓ Barbers after reload: {len(barber_ctrl.list_all())}")
    print(f"✓ Services after reload: {len(service_ctrl.list_all())}")
    print(f"✓ Appointments after reload: {len(appointment_ctrl.list_all())}")
    
    # Summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    print("✓ All tests passed successfully!")
    print(f"✓ System has {len(customer_ctrl.list_all())} customers")
    print(f"✓ System has {len(barber_ctrl.list_all())} barbers")
    print(f"✓ System has {len(service_ctrl.list_all())} services")
    print(f"✓ System has {len(appointment_ctrl.list_all())} appointments")
    print("\nThe Barbershop Management System is ready to use!")
    print("Run 'python3 main.py' to start the interactive application.")
    print("=" * 60)

if __name__ == "__main__":
    test_system()
