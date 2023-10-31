# pyProdigy : A Smarter Print for Execution Checks
A Python Library to Track Program Progress
![2023-11-01_03-33](https://github.com/aakashsinghbais/pyprodigy/assets/56718090/b5eb78db-c61f-4e37-8933-73fe9a7ee363)

# Dependencies
Please make sure that the following Python packages are installed on your system / virtual environment : tqdm, colorama, pyfiglet, psutil

# Setup
1. Download the `main.py` file from this repo and rename it to `pyprodigy.py`.
2. Add these lines to the start of your Python script:
```python
import sys
sys.path.append("/location/of/pyprodigy.py")
from pyprodigy import check
```

# Usage
1. `check("header", "Your Header Goes Here")` : Print the graffitti header.
2. `check("pass", "Your custom pass message here")`
3. `check("info", "Your custom info message here")`
4. `check("finish")` : program execution finishes here.

# Updates
The package will soon be uploaded for PyPI
