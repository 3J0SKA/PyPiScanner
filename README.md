
# PyPiScanner

 A Python3 based **fast port scanner** specifically made for CTF's! 


## Key Features!

* Specify range of ports to be scanned. 
* Scan ports which are heavily used in CTF's
* Run a Nmap scan on the ports found for more information.
* Ports are saved in a file for further usage.
## Pre Installations 

To run this application you will need [Netcat](https://sectools.org/tool/netcat/) for sending requests and [Nmap](https://nmap.org/download.html) for detailed port scanning.

### Installing Netcat

```bash
# Installing Netcat on Debian/Ubuntu
sudo apt-get install Netcat

# Installing Netcat on Fedora 22+ and RHEL8
dnf install nc

# Installing Netcat on CentOS/RHEL
yum install nc
```

### Installing Nmap

```bash 
# Installing Nmap on Debian/Ubuntu
sudo apt-get install nmap

# Installing Nmap on CentOS/RHEL
yum install nmap

#Installing Nmap on Fedora 22+ and RHEL8
dnf install nmap
```

Note :  If you face any problem while downloading either of these programs, try updating your packages by `sudo apt/yum update -y`

## How To Use!

To clone and run this program, you'll need [Python3](https://www.python.org/downloads/) and [Git](https://git-scm.com/).

```bash
  # Clone the application
  git clone https://github.com/3J0SKA/PyPiScanner.git

  # Go into the repository
  cd PyPiScanner
  
  # Run the script
  python pypiscanner.py
```

**Note** : This python application is designed for Linux systems.
    
## Usage/Examples

### Options:

```
-i | --ipaddress     Specify IP address to scan ports on.
-p | --port          Specify range of ports, for example, 100 will scan port 1 to 99.
-f | --filename      Specify the file name to store the ports in.
-c | --ctf           Special CTF mode which uses common ports used in CTF's.
-h | --help          Shows a descriptive help menu.
```

### Basic Usage

```bash
python3 pypiscanner.py -i 127.0.0.1 -p 1000 -f file_name.txt 
```

### Usage For CTF's!

```bash
python3 pypiscanner.py -i 127.0.0.1 -c
```

* Note : The CTF functionality might miss a lots of ports on the system. This port list only contains *mostly used* ports.

