# Crypto Arbitrage Finder

## Overview  
Crypto Arbitrage Finder is a Python tool designed to monitor cryptocurrency prices across multiple exchanges, detect discrepancies, and present potential arbitrage opportunities in real time. It helps traders spot situations where buying a coin on one exchange and selling it on another would be profitable.

## Features  
- Fetches live price data for coins from multiple exchanges  
- Compares prices across exchanges to detect mismatches  
- Flags arbitrage opportunities based on configurable thresholds  
- Saves data logs or alerts for further analysis  
- Supports customization of coins and exchanges via configuration  

## Usage

Populate coins.txt with the list of coin symbols you want to monitor.

Update js.json or config file with exchange API endpoints or credentials.

Run the script: python main.py

The script will output detected arbitrage opportunities to console, logs, or a designated output file.
