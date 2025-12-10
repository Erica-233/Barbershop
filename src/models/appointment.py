"""
Appointment model for the barbershop management system.
"""
from datetime import datetime
from typing import Optional


class Appointment:
    """Represents an appointment in the barbershop system."""
    
    STATUS_SCHEDULED = "scheduled"
    STATUS_COMPLETED = "completed"
    STATUS_CANCELLED = "cancelled"
    
    def __init__(self, appointment_id: str, customer_id: str, barber_id: str,
                 service_id: str, appointment_datetime: str, 
                 status: str = STATUS_SCHEDULED, notes: Optional[str] = None,
                 created_at: Optional[str] = None):
        """
        Initialize an Appointment.
        
        Args:
            appointment_id: Unique identifier for the appointment
            customer_id: ID of the customer
            barber_id: ID of the barber
            service_id: ID of the service
            appointment_datetime: Date and time of the appointment (ISO format)
            status: Appointment status (scheduled, completed, cancelled)
            notes: Additional notes about the appointment
            created_at: Timestamp when appointment was created (optional)
        """
        self.appointment_id = appointment_id
        self.customer_id = customer_id
        self.barber_id = barber_id
        self.service_id = service_id
        self.appointment_datetime = appointment_datetime
        self.status = status
        self.notes = notes
        self.created_at = created_at or datetime.now().isoformat()
    
    def to_dict(self) -> dict:
        """Convert appointment to dictionary for storage."""
        return {
            'appointment_id': self.appointment_id,
            'customer_id': self.customer_id,
            'barber_id': self.barber_id,
            'service_id': self.service_id,
            'appointment_datetime': self.appointment_datetime,
            'status': self.status,
            'notes': self.notes,
            'created_at': self.created_at
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Appointment':
        """Create an Appointment instance from a dictionary."""
        return cls(
            appointment_id=data['appointment_id'],
            customer_id=data['customer_id'],
            barber_id=data['barber_id'],
            service_id=data['service_id'],
            appointment_datetime=data['appointment_datetime'],
            status=data.get('status', cls.STATUS_SCHEDULED),
            notes=data.get('notes'),
            created_at=data.get('created_at')
        )
    
    def __str__(self) -> str:
        """String representation of the appointment."""
        return f"Appointment({self.appointment_id}): {self.appointment_datetime} - {self.status}"
    
    def __repr__(self) -> str:
        """Detailed string representation."""
        return (f"Appointment(id={self.appointment_id}, customer={self.customer_id}, "
                f"barber={self.barber_id}, datetime={self.appointment_datetime}, status={self.status})")
