import sys
import os

sys.path.append(os.path.dirname(__file__))

from Front_End.app import app
from budget import Budget  
if __name__ == "__main__":
	app.run(debug=True)