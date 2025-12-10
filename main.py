#!/usr/bin/env python3
"""
Main entry point for the Barbershop Management System.
"""
import sys
import os

# Add the parent directory to the path so we can import from src
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.cli import main

if __name__ == "__main__":
    main()
