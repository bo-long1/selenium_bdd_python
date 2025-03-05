import os
import sys

# Add path to helpers/ and driver
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))

# Add sys.path to import environment.py
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.append(parent_dir)