"""
Customer model for the barbershop management system.
"""
from datetime import datetime
from typing import Optional


class Customer:
    """Represents a customer in the barbershop system."""
    
    def __init__(self, customer_id: str, name: str, phone: str, 
                 email: Optional[str] = None, created_at: Optional[str] = None):
        """
        Initialize a Customer.
        
        Args:
            customer_id: Unique identifier for the customer
            name: Customer's full name
            phone: Customer's phone number
            email: Customer's email address (optional)
            created_at: Timestamp when customer was created (optional)
        """
        self.customer_id = customer_id
        self.name = name
        self.phone = phone
        self.email = email
        self.created_at = created_at or datetime.now().isoformat()
    
    def to_dict(self) -> dict:
        """Convert customer to dictionary for storage."""
        return {
            'customer_id': self.customer_id,
            'name': self.name,
            'phone': self.phone,
            'email': self.email,
            'created_at': self.created_at
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Customer':
        """Create a Customer instance from a dictionary."""
        return cls(
            customer_id=data['customer_id'],
            name=data['name'],
            phone=data['phone'],
            email=data.get('email'),
            created_at=data.get('created_at')
        )
    
    def __str__(self) -> str:
        """String representation of the customer."""
        return f"Customer({self.customer_id}): {self.name} - {self.phone}"
    
    def __repr__(self) -> str:
        """Detailed string representation."""
        return f"Customer(id={self.customer_id}, name={self.name}, phone={self.phone}, email={self.email})"
