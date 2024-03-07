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

# TODO:
1. Add unique hashes to every check point (based on the location of the file and the line number where it belongs).
2. Make an execution graph with these unique checkpoints as nodes.
3. Generate the stats for time taken for the code to traverse every edge in the graph (average execution time from one unique checkpoint to another)
4. Show this graph and save it.

# Updates
The package will soon be uploaded for PyPI
