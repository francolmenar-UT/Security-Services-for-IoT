import glob
import re
import subprocess
import os
#load filenames of all pcap files
#path = "C:\\Users\\Raphael\\github\\Security-Services-for-IoT\\Final-Project\\pcap\\raw\\MiLamp\\"
#path = "C:\\Users\\Raphael\\github\\Security-Services-for-IoT\\Final-Project\\pcap\\raw\\Smart_Plug-HS100\\"
path = "C:\\Users\\Raphael\\github\\Security-Services-for-IoT\\Final-Project\\pcap\\processed\\Smart_Plug-HS100\\"

out_path = "C:\\Users\\Raphael\\github\\Security-Services-for-IoT\\Final-Project\\pcap\\processed\\splug-csv_processed\\"
#out_path = "C:\\Users\\Raphael\\github\\Security-Services-for-IoT\\Final-Project\\pcap\\processed\\csv-files\\"
filenames = (glob.glob(path + "*.pcapng"))

#extract filenames
testname = []
for file in filenames:
    names = file.split("\\")
    testname.append(names[len(names) -1].split(".")[0])

#conver pcap files to csv and save them under the same name as the pcap file
for i in range(len(filenames)):
    command = "tshark -r" + filenames[i] + " -T fields -e frame.number -e frame.time -e eth.src -e eth.dst " + \
            "-e ip.src -e ip.dst -e ip.proto -e data.data -e data.len -e udp.srcport -e udp.dstport -e udp.length " + \
            "-e eth.addr.oui_resolved -e tcp.srcport  -e tcp.dstport -e tcp.len -E header=y -E separator="","" -E quote=d -E occurrence=f > " + out_path + testname[i] + ".csv"
    os.system(command)
