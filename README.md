# Advent of Code 2024
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](#) ![Cython](https://img.shields.io/badge/Cython-ED8B00?logo=cython&logoColor=fff) ![](https://img.shields.io/badge/Stars%20⭐-3-yellow) ![](https://img.shields.io/badge/Days%20Completed-1-red) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Repository contains my work in progress solutions for all riddles in [Advent of Code](https://adventofcode.com/) (2024). I try to make heavy use of both numpy and cython to speed up the solutions where ever possible.
# Advent of Code 2025
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](#) ![](https://img.shields.io/badge/Stars%20⭐-24-yellow) ![](https://img.shields.io/badge/Days%20Completed-12-red) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Solutions for all riddles in [Advent of Code](https://adventofcode.com/) (2025). All solutions are in Python and should run in reasonable time. You can calculate the solutions for a day $x$ given a file containing the provided input data as follows:

```console
python day_x.py input_data.txt
```

## External Libraries
I tried to refrain from using external libraries for solution. Yet, in three cases I could not get around it:
* [Day Nine](/2025/day_nine.py) used shapely for point in polygon check
* [Day Ten](/2025/day_ten.py) used PuLP for linear programming
* [Day Eleven](/2025/day_eleven.py) used NumPy for graph representation
