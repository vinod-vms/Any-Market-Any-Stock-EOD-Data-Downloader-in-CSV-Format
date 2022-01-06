import os
import glob
import yfinance as yf
from ticker import symbols
from get_csv_data_files import download_csv


if __name__ == "__main__":
    download_csv(symbols)
