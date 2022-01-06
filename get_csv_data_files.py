import os
import glob
import yfinance as yf
from ticker import symbols
# (c) Vinod Mathew Sebastian https://vinod-vms.netlify.app
# for Licensing, see bottom of page

def initial_csv_files():
    initial_csv_files_in_dir = glob.glob('*.csv')
    num = len(initial_csv_files_in_dir)
    return num


def get_number_of_files_downloaded(n):
    current_count = glob.glob('*.csv')
    return len(current_count) - n


def log_success(num):
    print(f"{num} new CSV files created.")

def get_data(dataset):
    return yf.download(dataset, period="max", group_by="ticker")

def download_csv(ticker):
    initial_num_of_csv_files = initial_csv_files()
    
    try:
        ticker_list = ticker.split(' ')
        for symbol in ticker_list:
            pathname = os.path.dirname(os.path.realpath(__file__))
            path = pathname+ '/' + symbol+ '.csv' #Linux
            #path = pathname+ '\' + symbol+ '.csv'  #Windows
            print(path)
            if os.path.exists(path):
                print(f"{symbol} already exists. Overwrite?")
                user_input = input("Enter 'y' to overwrite or 'n' to keep existing file.\n")
                if user_input.lower() == 'y':
                    os.remove(path)
                    initial_num_of_csv_files -= 1
                    print(f'Downloading {symbol} ...')
                    data =  get_data(symbol)
                    #pathname = os.getcwd()
                    data.to_csv(path)
                    print(f'Done with {symbol}')
                elif user_input.lower() == 'n':
                    pass
            else:
                data =  get_data(symbol)
                data.to_csv(path)
                print(f'Done with {symbol}')
               
              
    except Exception as e:
        print(f"Error! Trouble downloading file(s).{get_number_of_files_downloaded(initial_num_of_csv_files)} file\(s\) downloaded.")
    return log_success(get_number_of_files_downloaded(initial_num_of_csv_files))



#MIT License
