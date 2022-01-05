"""
Add parent directory of the script to path so we can import modules from parent directory.
"""

import os, sys
sys.path.insert(1, os.path.join(sys.path[0], "../"))