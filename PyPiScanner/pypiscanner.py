import subprocess
from subprocess import Popen, PIPE, STDOUT, check_output
import os
import optparse

def print_banner(title=""):
    print("""
  _____       _____ _  _____                                 
 |  __ \     |  __ (_)/ ____|                                
 | |__) |   _| |__) || (___   ___ __ _ _ __  _ __   ___ _ __ 
 |  ___/ | | |  ___/ |\___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
 | |   | |_| | |   | |____) | (_| (_| | | | | | | |  __/ |   
 |_|    \__, |_|   |_|_____/ \___\__,_|_| |_|_| |_|\___|_|   
         __/ |                                               
        |___/     

Python Based Port Scanner!
""")
print_banner()

def break_point(cause):
	cause_len = len(cause)
	print(f"""
================================{cause_len * "="}
+++++++++++++++++{cause}+++++++++++++++
================================{cause_len * "="}
		""")

parser = optparse.OptionParser()
parser.add_option("-i", "--ipaddress", dest="IP", help="The IP address of the machine you are scanning ports on.")
parser.add_option("-p", "--port", dest="PORT", default="10", help="The range of ports you want to scan. For eg : 100 will be 1 to 99 Port")
parser.add_option("-f", "--filename", dest="file_name", default="target_ports.txt", help="Name of the file, the ports are stored in.")

(options, arguments) = parser.parse_args()

IP = options.IP
PORT = options.PORT
FILE_F = options.file_name

if os.path.isfile(FILE_F) == True:
	os.remove(FILE_F)

make_file = open(FILE_F, "w")

break_point("Sending Requests To Ports!")

for i in range(1,int(PORT)):
	output = subprocess.call(["nc", "-z", IP, str(i)])
	if output == 0 :
		print('\033[1;32;40m' + '[~]' + '\033[0m' + ' The port ' + str(i) + ' is open!')
		edit_file = open(FILE_F, "a")
		edit_file.write(str(i)+ ",\n")
	else : 
		pass

edit_file = open(FILE_F)
read_file = edit_file.read()

slice_read_file = read_file[:-2]

edit_file = open(FILE_F, "w")
edit_file.write(slice_read_file)

edit_file = open(FILE_F)
read_file = edit_file.read()

print('\033[1;32;40m' + '[~]'+ '\033[0m' + ' File with ports saved to ' + '\033[1;32;40m' + FILE_F + '\033[0m')

break_point("Running NMAP Scan For Found Ports!")

scan_nmap = subprocess.run(["nmap","-sV", "-sC", "-p", read_file,IP])

break_point("END")