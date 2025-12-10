"""
Appointment controller for the barbershop management system.
Handles all appointment-related business logic.
"""
from typing import List, Optional
from datetime import datetime
from ..models.appointment import Appointment
from ..storage import StorageManager


class AppointmentController:
    """Controller for managing appointments."""
    
    def __init__(self, storage: StorageManager):
        """
        Initialize the appointment controller.
        
        Args:
            storage: Storage manager instance
        """
        self.storage = storage
        self.appointments: List[Appointment] = []
        self.load_appointments()
    
    def load_appointments(self):
        """Load appointments from storage."""
        data = self.storage.load_appointments()
        self.appointments = [Appointment.from_dict(a) for a in data]
    
    def save_appointments(self):
        """Save appointments to storage."""
        data = [a.to_dict() for a in self.appointments]
        self.storage.save_appointments(data)
    
    def create_appointment(self, customer_id: str, barber_id: str, service_id: str,
                          appointment_datetime: str, notes: Optional[str] = None) -> Appointment:
        """
        Create a new appointment.
        
        Args:
            customer_id: ID of the customer
            barber_id: ID of the barber
            service_id: ID of the service
            appointment_datetime: Date and time (ISO format)
            notes: Additional notes (optional)
        
        Returns:
            The newly created appointment
        """
        appointment_id = self._generate_id()
        appointment = Appointment(
            appointment_id, customer_id, barber_id, service_id,
            appointment_datetime, Appointment.STATUS_SCHEDULED, notes
        )
        self.appointments.append(appointment)
        self.save_appointments()
        return appointment
    
    def get_appointment(self, appointment_id: str) -> Optional[Appointment]:
        """
        Get an appointment by ID.
        
        Args:
            appointment_id: The appointment's ID
        
        Returns:
            The appointment if found, None otherwise
        """
        for appointment in self.appointments:
            if appointment.appointment_id == appointment_id:
                return appointment
        return None
    
    def update_appointment(self, appointment_id: str, customer_id: Optional[str] = None,
                          barber_id: Optional[str] = None, service_id: Optional[str] = None,
                          appointment_datetime: Optional[str] = None,
                          notes: Optional[str] = None) -> bool:
        """
        Update an appointment's information.
        
        Args:
            appointment_id: The appointment's ID
            customer_id: New customer ID (optional)
            barber_id: New barber ID (optional)
            service_id: New service ID (optional)
            appointment_datetime: New datetime (optional)
            notes: New notes (optional)
        
        Returns:
            True if appointment was updated, False otherwise
        """
        appointment = self.get_appointment(appointment_id)
        if appointment:
            if customer_id is not None:
                appointment.customer_id = customer_id
            if barber_id is not None:
                appointment.barber_id = barber_id
            if service_id is not None:
                appointment.service_id = service_id
            if appointment_datetime is not None:
                appointment.appointment_datetime = appointment_datetime
            if notes is not None:
                appointment.notes = notes
            self.save_appointments()
            return True
        return False
    
    def cancel_appointment(self, appointment_id: str) -> bool:
        """
        Cancel an appointment.
        
        Args:
            appointment_id: The appointment's ID
        
        Returns:
            True if appointment was cancelled, False otherwise
        """
        appointment = self.get_appointment(appointment_id)
        if appointment:
            appointment.status = Appointment.STATUS_CANCELLED
            self.save_appointments()
            return True
        return False
    
    def complete_appointment(self, appointment_id: str) -> bool:
        """
        Mark an appointment as completed.
        
        Args:
            appointment_id: The appointment's ID
        
        Returns:
            True if appointment was completed, False otherwise
        """
        appointment = self.get_appointment(appointment_id)
        if appointment:
            appointment.status = Appointment.STATUS_COMPLETED
            self.save_appointments()
            return True
        return False
    
    def get_appointments_by_customer(self, customer_id: str) -> List[Appointment]:
        """Get all appointments for a customer."""
        return [a for a in self.appointments if a.customer_id == customer_id]
    
    def get_appointments_by_barber(self, barber_id: str) -> List[Appointment]:
        """Get all appointments for a barber."""
        return [a for a in self.appointments if a.barber_id == barber_id]
    
    def get_appointments_by_status(self, status: str) -> List[Appointment]:
        """Get all appointments with a specific status."""
        return [a for a in self.appointments if a.status == status]
    
    def list_all(self) -> List[Appointment]:
        """Get all appointments."""
        return self.appointments.copy()
    
    def _generate_id(self) -> str:
        """Generate a unique appointment ID."""
        if not self.appointments:
            return "A001"
        
        # Extract numeric part from last ID and increment
        try:
            last_id = max(int(a.appointment_id[1:]) for a in self.appointments if a.appointment_id.startswith('A') and a.appointment_id[1:].isdigit())
            return f"A{last_id + 1:03d}"
        except (ValueError, IndexError):
            # Fallback: count existing appointments and add 1
            return f"A{len(self.appointments) + 1:03d}"
