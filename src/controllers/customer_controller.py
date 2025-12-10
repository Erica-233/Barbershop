"""
Customer controller for the barbershop management system.
Handles all customer-related business logic.
"""
from typing import List, Optional
from ..models.customer import Customer
from ..storage import StorageManager


class CustomerController:
    """Controller for managing customers."""
    
    def __init__(self, storage: StorageManager):
        """
        Initialize the customer controller.
        
        Args:
            storage: Storage manager instance
        """
        self.storage = storage
        self.customers: List[Customer] = []
        self.load_customers()
    
    def load_customers(self):
        """Load customers from storage."""
        data = self.storage.load_customers()
        self.customers = [Customer.from_dict(c) for c in data]
    
    def save_customers(self):
        """Save customers to storage."""
        data = [c.to_dict() for c in self.customers]
        self.storage.save_customers(data)
    
    def add_customer(self, name: str, phone: str, email: Optional[str] = None) -> Customer:
        """
        Add a new customer.
        
        Args:
            name: Customer's name
            phone: Customer's phone number
            email: Customer's email (optional)
        
        Returns:
            The newly created customer
        """
        customer_id = self._generate_id()
        customer = Customer(customer_id, name, phone, email)
        self.customers.append(customer)
        self.save_customers()
        return customer
    
    def get_customer(self, customer_id: str) -> Optional[Customer]:
        """
        Get a customer by ID.
        
        Args:
            customer_id: The customer's ID
        
        Returns:
            The customer if found, None otherwise
        """
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer
        return None
    
    def search_customers(self, query: str) -> List[Customer]:
        """
        Search for customers by name or phone.
        
        Args:
            query: Search query
        
        Returns:
            List of matching customers
        """
        query_lower = query.lower()
        results = []
        for customer in self.customers:
            if (query_lower in customer.name.lower() or 
                query_lower in customer.phone):
                results.append(customer)
        return results
    
    def update_customer(self, customer_id: str, name: Optional[str] = None,
                       phone: Optional[str] = None, email: Optional[str] = None) -> bool:
        """
        Update a customer's information.
        
        Args:
            customer_id: The customer's ID
            name: New name (optional)
            phone: New phone (optional)
            email: New email (optional)
        
        Returns:
            True if customer was updated, False otherwise
        """
        customer = self.get_customer(customer_id)
        if customer:
            if name is not None:
                customer.name = name
            if phone is not None:
                customer.phone = phone
            if email is not None:
                customer.email = email
            self.save_customers()
            return True
        return False
    
    def delete_customer(self, customer_id: str) -> bool:
        """
        Delete a customer.
        
        Args:
            customer_id: The customer's ID
        
        Returns:
            True if customer was deleted, False otherwise
        """
        for i, customer in enumerate(self.customers):
            if customer.customer_id == customer_id:
                self.customers.pop(i)
                self.save_customers()
                return True
        return False
    
    def list_all(self) -> List[Customer]:
        """Get all customers."""
        return self.customers.copy()
    
    def _generate_id(self) -> str:
        """Generate a unique customer ID."""
        if not self.customers:
            return "C001"
        
        # Extract numeric part from last ID and increment
        last_id = max(int(c.customer_id[1:]) for c in self.customers)
        return f"C{last_id + 1:03d}"
