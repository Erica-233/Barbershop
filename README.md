# Barbershop Management System

A comprehensive command-line application for managing barbershop operations, including customer management, barber scheduling, service catalog, and appointment booking.

## Features

- **Customer Management**: Add, update, search, and manage customer information
- **Barber Management**: Maintain barber profiles with specialties and contact details
- **Service Catalog**: Define services with pricing and duration
- **Appointment Scheduling**: Book, update, cancel, and complete appointments
- **Data Persistence**: All data is automatically saved to JSON files

## Installation

This system requires Python 3.6 or higher. No external dependencies are required.

### Clone the repository
```bash
git clone https://github.com/Erica-233/Barbershop.git
cd Barbershop
```

## Usage

### Starting the Application

Run the main application:
```bash
python3 main.py
```

### Main Menu

The system provides a user-friendly menu interface with the following options:

1. **Customer Management**
   - Add new customers
   - View all customers
   - Search customers by name or phone
   - Update customer information
   - Delete customers

2. **Barber Management**
   - Add new barbers
   - View all barbers
   - Update barber information
   - Delete barbers

3. **Service Management**
   - Add new services
   - View all services
   - Update service details (name, duration, price)
   - Delete services

4. **Appointment Management**
   - Create new appointments
   - View all appointments
   - View appointments by customer
   - View appointments by barber
   - Update appointment details
   - Cancel appointments
   - Mark appointments as completed

## Example Workflow

### 1. Setting Up Your Barbershop

First, add your barbers:
```
Main Menu → Barber Management → Add Barber
Name: John Smith
Specialty: Fade Specialist
Phone: 555-0101
```

Then, add your services:
```
Main Menu → Service Management → Add Service
Name: Men's Haircut
Duration: 30 minutes
Price: 25.00
Description: Classic men's haircut
```

### 2. Managing Customers

Add a new customer:
```
Main Menu → Customer Management → Add Customer
Name: Mike Johnson
Phone: 555-0202
Email: mike@example.com
```

Search for existing customers:
```
Main Menu → Customer Management → Search Customer
Search: Mike
```

### 3. Booking Appointments

Create an appointment:
```
Main Menu → Appointment Management → Create Appointment
Customer ID: C001
Barber ID: B001
Service ID: S001
Date: 2025-12-15
Time: 14:30
Notes: Customer prefers short fade
```

View appointments:
```
Main Menu → Appointment Management → View All Appointments
```

## Data Storage

All data is stored in JSON format in the `data/` directory:
- `customers.json`: Customer information
- `barbers.json`: Barber profiles
- `services.json`: Service catalog
- `appointments.json`: Appointment records

## Project Structure

```
Barbershop/
├── main.py                 # Application entry point
├── requirements.txt        # Python dependencies (none required)
├── README.md              # This file
├── data/                  # Data storage directory
│   ├── .gitkeep
│   ├── customers.json
│   ├── barbers.json
│   ├── services.json
│   └── appointments.json
└── src/                   # Source code
    ├── cli.py             # Command-line interface
    ├── storage.py         # Data persistence layer
    ├── models/            # Data models
    │   ├── __init__.py
    │   ├── customer.py
    │   ├── barber.py
    │   ├── service.py
    │   └── appointment.py
    └── controllers/       # Business logic
        ├── __init__.py
        ├── customer_controller.py
        ├── barber_controller.py
        ├── service_controller.py
        └── appointment_controller.py
```

## Features in Detail

### Customer Management
- Unique customer IDs (C001, C002, ...)
- Store name, phone, and email
- Search functionality
- Full CRUD operations

### Barber Management
- Unique barber IDs (B001, B002, ...)
- Track specialties and contact information
- View appointments per barber

### Service Catalog
- Unique service IDs (S001, S002, ...)
- Define service duration and pricing
- Optional descriptions

### Appointment System
- Unique appointment IDs (A001, A002, ...)
- Link customers, barbers, and services
- Track appointment status (scheduled, completed, cancelled)
- Add notes for special requests
- Filter appointments by customer or barber

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.