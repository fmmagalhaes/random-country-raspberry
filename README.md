# Random Country Raspberry

This repository aims at giving daily information about a random country. This was achieved by using a mini LCD connected to a Raspberry PI.

<img src="https://user-images.githubusercontent.com/8866496/195190798-30d6fdd9-f1f8-45f4-b8c3-56457b05df46.jpeg" width="500">



The communication with the LCD was done through the interfacing made available by this repository:
https://github.com/the-raspberry-pi-guy/lcd

The country information comes from RestCountries API  
https://restcountries.com/

## Setup

### Install dependencies
```pip install requests```  
```pip install schedule```  


### Run in the console
To run this in the console, simply run  
```python console_random_country.py```

### Run on Raspberry Pi
1. Follow this installation guide to setup the drivers for the LCD communication  
https://github.com/the-raspberry-pi-guy/lcd#Installation

2. Run ```python lcd_random_country.py```

A random country will now be displayed daily in your LCD. Make the necessary adjustments to edit the periodicity at your own will. 
