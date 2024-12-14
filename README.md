# Secure Gassword Generator in Python

This is a password generator written in Python. It has a built-in system for selecting which characters will appear in your password. You can choose between lowercase letters, uppercase letters, digits and special characters. In case you include special characters in your password, you can choose to whether or not you want to use unusual special characters. Usual special characters include !#$%&?@ and unusual characters include all the usual ones with ()*+,-./:;<=>[\]^_{|}~ added. You can also choose the length of your password and you can set an initial word with which every password will start.

# Running from Python

## Python

I won't cover the Python installation becuase documented much better online. Just google it.

## Code

Download the compressed code from the "Download ZIP" button in the green "<>Code" menu, after you download it unzip it somewhere. You can also just clone this repo somewhere.

## Virtual environment

I highly recommend using virtual environments for running any python code. Open the folder which you unzipped or cloned in the terminal. Run the following command to create a python virtual environment.
```
python -m venv .venv
```
You should see a .venv folder now. To activate your virtual environment, if you're on Linux/MacOS run
```
source .venv/bin/activate
```
Or if you're on Windows run
```
.venv/Scripts/activate
```
Now you should see (.venv) at the beggining of every new line in your terminal. To install required packages in your virtual environment, and not your entire system, run
```
pip install -r requirements.txt
```
*Note: On some Linux distributions you might need to install the tk package to your system with your distro's package manager.*

## Run the code

While still in the virtual envrionment, run
```
python main.py
```
*Note: Depending on your python installation you might need to use python3.*
