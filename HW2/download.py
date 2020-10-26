"""
Author: Francesc Roura Adserias, Scientific programming course, 2nd assignment.
Creation date: 20201024
Description: this script downloads data from http://srtm.csi.cgiar.org/srtmdata/
    A. Write a script which, given a longitude and a latitude as arguments, 
    downloads the corresponding file in the current directory.
 
    B. Extend this script to be a bit more clever: download the data file only 
    if the file isn’t already available in the current directory. This is 
    particularly useful because the server is not very fast.
    C. Extend this script to be even more clever: given a range of longitudes 
    and latitudes, it should download all the files covering this area. For 
    example, the range 9°W to 18°W and 44°N to 47°N would download 6 files. 
    In order to avoid manual mistakes, warn the user by announcing the number 
    of files that the command is going to download, and ask for confirmation 
    before going on (by using the input() function).
    D1. print a message to the user announcing if the file was downloaded or 
    was already on disk
"""

if __name__ == '__main__':
    #import modules
    import urllib.request
    import sys
    import math
    import os
    #import numpy as np
##A.
    #Check latlon coordinates
    lat1 = int(sys.argv[1])
    lon1 = int(sys.argv[2])
    lat2 = int(sys.argv[3])
    lon2 = int(sys.argv[4])
    #lat1=50
    #lat2=40
    #lon1=-100
    #lon2=-90
    if (lon1 or lon2) > 180 or (lon1 or lon2) < -180:
        sys.exit('Longitude out of bounds [-180,180]')
    if (lon1 > lon2):
        sys.exit('Longitude 1 must be smaller than or equal to longitude 2')
    if (lat1 or lat2) > 60 or (lat1 or lat2) < -60:
        sys.exit('Latitude out of bounds [-60,60]')
    if (lat1 < lat2):
        sys.exit('Latitude 1 must be greater than or equal to latitude 2')
        
    ilo1 = math.trunc((lon1 + 180)/5) + 1
    ila1 = math.trunc(-(lat1 - 60)/5) + 1
    ilo2 = math.trunc((lon2 + 180)/5) + 1
    ila2 = math.trunc(-(lat2 - 60)/5) + 1

    ilo = []
    ila = []
    url = []
    #ila = range(ila1, ila2)
    for i in range(ilo1, ilo2):     
        if len(str(i)) == 1:
            element = '0' + str(i)
            ilo.append(element)
        else:
            ilo.append(str(i))
    for i in range(ila1, ila2):     
        if len(str(i)) == 1:
            element = '0' + str(i)
            ila.append(element)
        else:
            ila.append(str(i))
    #if len(ila1) == 1:
    #    ila1 = '0' + ila1
    #if len(ilo2) == 1:
    #    ilo2 = '0' + ilo2
    #if len(ila2) == 1:
    #    ila2 = '0' + ila2
        
    source = "http://srtm.csi.cgiar.org/wp-content/uploads/files/srtm_5x5/TIFF/srtm_"
    #url = np.repeat(source, len(ila)*len(ilo))
    print("WARNING: " + str(len(ila)*len(ilo)) + " elements are going to be downloaded")
    y = input("type 'y' to continue:")
    if not(y == "y"):
        sys.exit('You have chosen to exit the script')
    for lo in ilo:
        for la in ila:
            url = source + lo + "_" + la + ".zip"
            filename = "srtm_" + lo + "_" + la + ".tif"
            if not os.path.exists(filename):
                urllib.request.urlretrieve(url, filename)
                print('The file' + filename + 'has been downloaded at the filesystem') 
                size = os.stat(filename).st_size*0.000001
                print("with a size of " + str(size)[0:5] + " MB")
            else:
                print('The file' + filename + ' was at the filesystem already')  
   # print(url)
   # url = source + ilo + "_" + ila
   # filename = "srtm_" + ilo + "_" + ila + ".tif"
##B.
    #if not os.path.exists(filename):
    #    urllib.request.urlretrieve(url + ".zip", filename)
    #else:
    #    sys.exit('The file' + filename + ' exists already')        
    #a = "patata"
    #print(a)