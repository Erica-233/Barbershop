"""
Service controller for the barbershop management system.
Handles all service-related business logic.
"""
from typing import List, Optional
from ..models.service import Service
from ..storage import StorageManager


class ServiceController:
    """Controller for managing services."""
    
    def __init__(self, storage: StorageManager):
        """
        Initialize the service controller.
        
        Args:
            storage: Storage manager instance
        """
        self.storage = storage
        self.services: List[Service] = []
        self.load_services()
    
    def load_services(self):
        """Load services from storage."""
        data = self.storage.load_services()
        self.services = [Service.from_dict(s) for s in data]
    
    def save_services(self):
        """Save services to storage."""
        data = [s.to_dict() for s in self.services]
        self.storage.save_services(data)
    
    def add_service(self, name: str, duration: int, price: float,
                   description: Optional[str] = None) -> Service:
        """
        Add a new service.
        
        Args:
            name: Service name
            duration: Service duration in minutes
            price: Service price
            description: Service description (optional)
        
        Returns:
            The newly created service
        """
        service_id = self._generate_id()
        service = Service(service_id, name, duration, price, description)
        self.services.append(service)
        self.save_services()
        return service
    
    def get_service(self, service_id: str) -> Optional[Service]:
        """
        Get a service by ID.
        
        Args:
            service_id: The service's ID
        
        Returns:
            The service if found, None otherwise
        """
        for service in self.services:
            if service.service_id == service_id:
                return service
        return None
    
    def update_service(self, service_id: str, name: Optional[str] = None,
                      duration: Optional[int] = None, price: Optional[float] = None,
                      description: Optional[str] = None) -> bool:
        """
        Update a service's information.
        
        Args:
            service_id: The service's ID
            name: New name (optional)
            duration: New duration (optional)
            price: New price (optional)
            description: New description (optional)
        
        Returns:
            True if service was updated, False otherwise
        """
        service = self.get_service(service_id)
        if service:
            if name is not None:
                service.name = name
            if duration is not None:
                service.duration = duration
            if price is not None:
                service.price = price
            if description is not None:
                service.description = description
            self.save_services()
            return True
        return False
    
    def delete_service(self, service_id: str) -> bool:
        """
        Delete a service.
        
        Args:
            service_id: The service's ID
        
        Returns:
            True if service was deleted, False otherwise
        """
        for i, service in enumerate(self.services):
            if service.service_id == service_id:
                self.services.pop(i)
                self.save_services()
                return True
        return False
    
    def list_all(self) -> List[Service]:
        """Get all services."""
        return self.services.copy()
    
    def _generate_id(self) -> str:
        """Generate a unique service ID."""
        if not self.services:
            return "S001"
        
        # Extract numeric part from last ID and increment
        last_id = max(int(s.service_id[1:]) for s in self.services)
        return f"S{last_id + 1:03d}"
