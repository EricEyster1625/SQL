import requests 
import argparse

def Download (SourceURL, DestinationFilePath): 
    r = requests.get(SourceURL) # create HTTP response object 
    with open(DestinationFilePath ,'wb') as f: 
      f.write(r.content) 
    
def ConvertDateToString (Year, Month):
    Month =  str(Month)  
    if len(Month) == 1:
        Month = "0" + Month
    DateString =  str(Year) + "-" + Month 
        
    return DateString


def FileDownload(TaxiColor, DateString):
    image_url = "https://d37ci6vzurychx.cloudfront.net/trip-data/" + TaxiColor +  "_tripdata_" + DateString  +  ".parquet"
    print(image_url)
    DestinationFilePath = DestinationPath + "\\" + TaxiColor +  "_tripdata_" + DateString  +  ".parquet"
    Download (image_url, DestinationFilePath)


def DateLoop(TaxiColor, Year, Month):
    print (TaxiColor)
    DateString = ConvertDateToString(Year, Month)

    while DateString != EndDate:
        FileDownload(TaxiColor,DateString)
        Month = Month + 1
        if Month == 13:
            Month = 1
            Year = Year + 1
        DateString = ConvertDateToString(Year, Month)
            


EndDate = "2024-08"
DestinationPath = "C:\\DATA"


#Get the taxi color
parser = argparse.ArgumentParser('TaxiColor')
parser.add_argument("TaxiColor")
args = parser.parse_args()

TaxiColor = args.TaxiColor


if(TaxiColor == "Yellow" or TaxiColor == "ALL"):
    Year = 2009
    Month = 1
    DateLoop ("yellow", Year, Month)
        
if(TaxiColor == "Green" or TaxiColor == "ALL"):
    Year = 2013
    Month = 9
    DateLoop ("green", Year, Month)

if(TaxiColor == "fhv" or TaxiColor == "ALL"):
    Year = 2015
    Month = 1
    DateLoop ("fhv", Year, Month)


if(TaxiColor == "fhvhv" or TaxiColor == "ALL"):
    Year = 2019
    Month = 2
    DateLoop ("fhvhv", Year, Month)



# for Year in range(2009,2024):
    # for Month in range(1, 13):

        # DateString = ConvertDateToString(Year, Month)
        