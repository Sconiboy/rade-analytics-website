#!/usr/bin/env python3
import sys
import os

# Add the project directory to Python path
sys.path.insert(0, '/home/ubuntu/rade-production')

from src.main import app

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
