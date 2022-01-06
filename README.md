## Any-Market-Any-Stock-EOD-Data-Downloader-in-CSV-Format

This little Python utility allows us to download end of day data in CSV format - Any stock or commodity: Stocks, Gold, Silver, Crude Oil... Any Exchange: NASDAQ, NSE, Singapore, NYSE...

Use the csv file to feed into other programs including Amibroker.


### Usage

We should have Python 3.6+ installed.

1. Clone the repo.
2. In the command line, ```cd``` into the cloned folder.
3. Run ```pip install -r requirement.text``` or ```pip3 install -r requirement.txt``` depending on whether you are in Windows or Linux.
4. In the ticker.py file, update the symbols as a single string. See the existing ticker.py file. You can use this link to look for symbols: https://finance.yahoo.com/ 
Amazon is 'AMZN', and Singapore Airlines is 'C6L.SI'.
5. If you are on Linux, comment/uncomment lines 32 and 33 of the 'get_csv_data_files.py' file.
5. Run ```python main.py``` or ```python3 main.py```<br/> The files should get automatically downloaded into the current folder.

### License
Anyone can _and should_ change the code, use it, or reuse it, on any other application.<br/> You are welcome. <br/> Only an attribution would suffice. <br/> MIT License &copy; [Vinod Mathew Sebastian](https://vinod-vms.netlify.app)
