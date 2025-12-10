"""
Barber model for the barbershop management system.
"""
from datetime import datetime
from typing import Optional, List


class Barber:
    """Represents a barber in the barbershop system."""
    
    def __init__(self, barber_id: str, name: str, specialty: Optional[str] = None,
                 phone: Optional[str] = None, created_at: Optional[str] = None):
        """
        Initialize a Barber.
        
        Args:
            barber_id: Unique identifier for the barber
            name: Barber's full name
            specialty: Barber's specialty (e.g., "Fade specialist", "Beard trimming")
            phone: Barber's phone number
            created_at: Timestamp when barber was added (optional)
        """
        self.barber_id = barber_id
        self.name = name
        self.specialty = specialty
        self.phone = phone
        self.created_at = created_at or datetime.now().isoformat()
    
    def to_dict(self) -> dict:
        """Convert barber to dictionary for storage."""
        return {
            'barber_id': self.barber_id,
            'name': self.name,
            'specialty': self.specialty,
            'phone': self.phone,
            'created_at': self.created_at
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Barber':
        """Create a Barber instance from a dictionary."""
        return cls(
            barber_id=data['barber_id'],
            name=data['name'],
            specialty=data.get('specialty'),
            phone=data.get('phone'),
            created_at=data.get('created_at')
        )
    
    def __str__(self) -> str:
        """String representation of the barber."""
        specialty_str = f" - {self.specialty}" if self.specialty else ""
        return f"Barber({self.barber_id}): {self.name}{specialty_str}"
    
    def __repr__(self) -> str:
        """Detailed string representation."""
        return f"Barber(id={self.barber_id}, name={self.name}, specialty={self.specialty})"
