"""
Barber controller for the barbershop management system.
Handles all barber-related business logic.
"""
from typing import List, Optional
from ..models.barber import Barber
from ..storage import StorageManager


class BarberController:
    """Controller for managing barbers."""
    
    def __init__(self, storage: StorageManager):
        """
        Initialize the barber controller.
        
        Args:
            storage: Storage manager instance
        """
        self.storage = storage
        self.barbers: List[Barber] = []
        self.load_barbers()
    
    def load_barbers(self):
        """Load barbers from storage."""
        data = self.storage.load_barbers()
        self.barbers = [Barber.from_dict(b) for b in data]
    
    def save_barbers(self):
        """Save barbers to storage."""
        data = [b.to_dict() for b in self.barbers]
        self.storage.save_barbers(data)
    
    def add_barber(self, name: str, specialty: Optional[str] = None,
                   phone: Optional[str] = None) -> Barber:
        """
        Add a new barber.
        
        Args:
            name: Barber's name
            specialty: Barber's specialty (optional)
            phone: Barber's phone (optional)
        
        Returns:
            The newly created barber
        """
        barber_id = self._generate_id()
        barber = Barber(barber_id, name, specialty, phone)
        self.barbers.append(barber)
        self.save_barbers()
        return barber
    
    def get_barber(self, barber_id: str) -> Optional[Barber]:
        """
        Get a barber by ID.
        
        Args:
            barber_id: The barber's ID
        
        Returns:
            The barber if found, None otherwise
        """
        for barber in self.barbers:
            if barber.barber_id == barber_id:
                return barber
        return None
    
    def update_barber(self, barber_id: str, name: Optional[str] = None,
                     specialty: Optional[str] = None, phone: Optional[str] = None) -> bool:
        """
        Update a barber's information.
        
        Args:
            barber_id: The barber's ID
            name: New name (optional)
            specialty: New specialty (optional)
            phone: New phone (optional)
        
        Returns:
            True if barber was updated, False otherwise
        """
        barber = self.get_barber(barber_id)
        if barber:
            if name is not None:
                barber.name = name
            if specialty is not None:
                barber.specialty = specialty
            if phone is not None:
                barber.phone = phone
            self.save_barbers()
            return True
        return False
    
    def delete_barber(self, barber_id: str) -> bool:
        """
        Delete a barber.
        
        Args:
            barber_id: The barber's ID
        
        Returns:
            True if barber was deleted, False otherwise
        """
        for i, barber in enumerate(self.barbers):
            if barber.barber_id == barber_id:
                self.barbers.pop(i)
                self.save_barbers()
                return True
        return False
    
    def list_all(self) -> List[Barber]:
        """Get all barbers."""
        return self.barbers.copy()
    
    def _generate_id(self) -> str:
        """Generate a unique barber ID."""
        if not self.barbers:
            return "B001"
        
        # Extract numeric part from last ID and increment
        last_id = max(int(b.barber_id[1:]) for b in self.barbers)
        return f"B{last_id + 1:03d}"
