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

https://github.com/3J0SKA/PyPiScanner
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
parser.add_option("-c", "--ctf", action="store_true", dest="CTF", default=False,help="Scan most used ports used in CTF's [Not recommended].")

(options, arguments) = parser.parse_args()

IP = options.IP
PORT = options.PORT
FILE_F = options.file_name
CTF_OPTION = options.CTF

def scan_map(read_file,IP):
	scan_nmap = subprocess.run(["nmap","-sV", "-sC", "-p", read_file,IP])

def information(IP,PORT,FILE_F,CTF_OPTION): 
	break_point("Information!")
	print("\033[1;32;40m" + "[~]" + "\033[0m"+ " IP address to scan : " + str(IP))
	if CTF_OPTION == True:
		print("\033[1;32;40m" + "[~]" "\033[0m"+ " CTF mode : " + "True\n")
		print("\033[1;31;40m" + "[!]" "\033[0m"+ " Note : CTF mode can miss out a lots of ports.")
	else : 
		print("\033[1;32;40m"+"[~]" + "\033[0m" + " CTF mode : " + "False")
		print("\033[1;32;40m"+ "[~]"+ "\033[0m" + " Port range : " + "1 to " + str(PORT))
		print("\033[1;32;40m" + "[~]" + "\033[0m" + " File name : " + str(FILE_F))

information(IP,PORT,FILE_F,CTF_OPTION)

def scan_main(IP,PORT,FILE_F,CTF_OPTION):
	if CTF_OPTION == True:
		CTF_FILE = "ctf_ports.txt"
		make_file_ctf = open(CTF_FILE, "w")
		break_point("Sending Requests To Ports!")
		make_file_ctf.write("21,\n22,\n23,\n25,\n53,\n67,\n80,\n81,\n110,\n123,\n135,\n139,\n161,\n162,\n443,\n993,\n8080,\n8081,\n587,\n990,\n995,\n1194,\n1433,\n1434,\n3306,\n3124")
		print('\033[1;32;40m' + '[~]' + '\033[0m' + ' Ports already saved to file: ' + '\033[1;32;40m' + CTF_FILE + '\033[0m')
		make_file_ctf = open(CTF_FILE, "r")
		ctf_ports = make_file_ctf.read()
		# print(ctf_ports)
		break_point("Running NMAP Scan For Specified Ports!")
		subprocess.run(["nmap","-sV", "-sC", "--open","-p", ctf_ports,IP])
	else:
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

		scan_map(read_file,IP)

		break_point("END")


scan_main(IP,PORT,FILE_F,CTF_OPTION)

