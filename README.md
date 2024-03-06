# pyChek : A Smarter Logger
Python Library to Track Program Progress
![pychek-test](https://github.com/xbais/pychek/assets/56718090/154fa3b4-6ca9-4e35-8b84-546e5354d182)

# Dependencies
Please make sure that the following Python packages are installed on your system / virtual environment : tqdm, colorama, pyfiglet, psutil

# Setup
1. Download the `main.py` file from this repo and rename it to `pyprodigy.py`.
2. Add these lines to the start of your Python script:
```python
import sys
sys.path.append("/location/of/pyprodigy.py")
from pychek import check
```

# Usage
1. `check("header", "Your Header Goes Here")` : Print the graffitti header.
2. `check("pass", "Your custom pass message here")`
3. `check("info", "Your custom info message here")`
4. `check("finish")` : program execution finishes here.

# Note:
**PyChek will not work in interactive Python shell.**

# Updates
The package will soon be uploaded for PyPI
