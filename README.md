# Service Metal Coding Test

The development of this code was conducted in a WSL2 Ubuntu environment. Installation and execution of code should be adapted to fit your specific environment.

## Table of Contents

1. [Database design](#1-database-design)
2. [API interaction](#2-api-interaction)
3. [Algorithms](#3-algorithms)

## 1. Database design

The code for this question can be found in [1-database-design.sql](1-database-design.sql).

The entry is based on the [following product](https://www.pvcfittingsonline.com/collections/pvc-gate-valves/products/2-pvc-socket-gate-valve-spears-2022-020) on [PVCFittingsOnline.com](https://www.pvcfittingsonline.com/).

The code was developed and tested using MariaDB v15.1, a popular fork of MySQL. The submission will work with either a MariaDB or MySQL installation.

If using WSL2, after MariaDB installation and set-up, run the following code to create and display the table:
```
sudo mysql -u [username] < 1-database_design.sql
```
In most cases, `[username]` can be replaced by `root`.

## 2. API interaction

The code for this question can be found in [2-api-interaction.py](2-api-interaction.py).

The code was developed and tested using Python v3.10.12.

This script requires external libraries to run. Ensure that you have `pip` installed, and run the following code in your terminal:
```
pip install --upgrade pip
pip install -r requirements.txt
```
`requirements.txt` contains a list of all external and third-party packages and libraries required for successful program execution.

To run the script in the terminal, execute the following code in the command line:
```
python3 2-api-interaction.py
```

## 3. Algorithms

The code for this question can be found in [3-algorithms.py](3-algorithms.py).

The code was developed and tested using Python v3.10.12.

This script does not require any external packages or libraries.

To run the script in the terminal, execute the following code in the command line:
```
python3 3-algorithms.py [filename]
```
OR
```
python3 3-algorithms.py
```
The program contains command-line positional arguments, but these are not necessary for the program. If no command-line arguments are provided, the path to the input file will be collected during the runtime of the program. For more information, type the following:
```
python3 3-algorithms.py --help
```