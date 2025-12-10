"""
Storage manager for the barbershop management system.
Handles data persistence using JSON files.
"""
import json
import os
from typing import Dict, List, Any


class StorageManager:
    """Manages data persistence for the barbershop system."""
    
    def __init__(self, data_dir: str = "data"):
        """
        Initialize the storage manager.
        
        Args:
            data_dir: Directory where data files are stored
        """
        self.data_dir = data_dir
        self.customers_file = os.path.join(data_dir, "customers.json")
        self.barbers_file = os.path.join(data_dir, "barbers.json")
        self.services_file = os.path.join(data_dir, "services.json")
        self.appointments_file = os.path.join(data_dir, "appointments.json")
        
        # Ensure data directory exists
        os.makedirs(data_dir, exist_ok=True)
        
        # Initialize files if they don't exist
        self._initialize_files()
    
    def _initialize_files(self):
        """Create empty data files if they don't exist."""
        for filepath in [self.customers_file, self.barbers_file, 
                        self.services_file, self.appointments_file]:
            if not os.path.exists(filepath):
                self._save_json(filepath, [])
    
    def _load_json(self, filepath: str) -> List[Dict[str, Any]]:
        """Load data from a JSON file."""
        try:
            with open(filepath, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def _save_json(self, filepath: str, data: List[Dict[str, Any]]):
        """Save data to a JSON file."""
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
    
    # Customer operations
    def load_customers(self) -> List[Dict[str, Any]]:
        """Load all customers from storage."""
        return self._load_json(self.customers_file)
    
    def save_customers(self, customers: List[Dict[str, Any]]):
        """Save all customers to storage."""
        self._save_json(self.customers_file, customers)
    
    # Barber operations
    def load_barbers(self) -> List[Dict[str, Any]]:
        """Load all barbers from storage."""
        return self._load_json(self.barbers_file)
    
    def save_barbers(self, barbers: List[Dict[str, Any]]):
        """Save all barbers to storage."""
        self._save_json(self.barbers_file, barbers)
    
    # Service operations
    def load_services(self) -> List[Dict[str, Any]]:
        """Load all services from storage."""
        return self._load_json(self.services_file)
    
    def save_services(self, services: List[Dict[str, Any]]):
        """Save all services to storage."""
        self._save_json(self.services_file, services)
    
    # Appointment operations
    def load_appointments(self) -> List[Dict[str, Any]]:
        """Load all appointments from storage."""
        return self._load_json(self.appointments_file)
    
    def save_appointments(self, appointments: List[Dict[str, Any]]):
        """Save all appointments to storage."""
        self._save_json(self.appointments_file, appointments)
