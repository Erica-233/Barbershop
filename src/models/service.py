"""
Service model for the barbershop management system.
"""
from datetime import datetime
from typing import Optional


class Service:
    """Represents a service offered by the barbershop."""
    
    def __init__(self, service_id: str, name: str, duration: int, price: float,
                 description: Optional[str] = None, created_at: Optional[str] = None):
        """
        Initialize a Service.
        
        Args:
            service_id: Unique identifier for the service
            name: Service name (e.g., "Haircut", "Beard Trim")
            duration: Service duration in minutes
            price: Service price in dollars
            description: Service description (optional)
            created_at: Timestamp when service was created (optional)
        """
        self.service_id = service_id
        self.name = name
        self.duration = duration
        self.price = price
        self.description = description
        self.created_at = created_at or datetime.now().isoformat()
    
    def to_dict(self) -> dict:
        """Convert service to dictionary for storage."""
        return {
            'service_id': self.service_id,
            'name': self.name,
            'duration': self.duration,
            'price': self.price,
            'description': self.description,
            'created_at': self.created_at
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Service':
        """Create a Service instance from a dictionary."""
        return cls(
            service_id=data['service_id'],
            name=data['name'],
            duration=data['duration'],
            price=data['price'],
            description=data.get('description'),
            created_at=data.get('created_at')
        )
    
    def __str__(self) -> str:
        """String representation of the service."""
        return f"Service({self.service_id}): {self.name} - ${self.price} ({self.duration} min)"
    
    def __repr__(self) -> str:
        """Detailed string representation."""
        return f"Service(id={self.service_id}, name={self.name}, price=${self.price}, duration={self.duration}min)"
