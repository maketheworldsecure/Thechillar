import subprocess
import sys

def nmap(url):
	with open ('nmaptxt','w')as f1:
		t1 =subprocess.run(['sudo','nmap','-sV','-sC','-O',url],stdout=f1,text= 'true')
		print("(+) Running Nikto")
		nikto(url)

def nikto(url):
	with open ('nikto.txt','w')as f1:
		t1 =subprocess.run(['nikto','-host',url],stdout=f1,text= 'true')
		#print("(+) Running YOURNEWTOOLFUNCTION")
		#YOURNEWTOOLFUNCTION(url)

def main():

	
	if len(sys.argv) != 2:
		print("(+) Usage: %s <url>" % sys.argv[0])
		print("(+) Example: %s www.example.com" % sys.argv[0])
		sys.exit(-1)

	url = sys.argv[1]
	print("(+) Running Nmap")
	nmap(url)


if __name__ == "__main__":
	result = pyfiglet.figlet_format("The Chiller", font = "slant" )
	
	print('\033[1;32m' + result)
	print("--------------------------------------------------------------")
	print("---------------RUN THE TOOL AND GO CHILL----------------------")
	print("--------------------------------------------------------------")
	main()



  
