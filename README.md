![alt text](https://github.com/maketheworldsecure/Thechillar/blob/main/chillarlogo.jpg)
# The chillar
#### Automation tool used to run multiple tools in single script, basically you can run this script and go chill.The script have the feature to add your custom tools to the execution list.
---------------------------
## Tools in the list

* NAMP
* NIKTO

## Instruction to add new tool
#### Step 1 : Install the tool **eg:Testssl** in your linux machine
#### Step 2 : Add the functiion to the script
```python
def NAMEOFYOURTOOL(url):
	with open ('NAMEOFYOURTOOL.txt','w')as f1:
		t1 =subprocess.run(['COMMAND','COMMAND',url],stdout=f1,text= 'true') 
		# eg : t1 =subprocess.run(['nmap','-sV',url],stdout=f1,text= 'true')		
```
#### Step 3 : Now call the function 
```python
# default last function in Thechillar script is Nikto
def nikto(url):
	with open ('nikto.txt','w')as f1:
		t1 =subprocess.run(['nikto','-host',url],stdout=f1,text= 'true')
		print("(+) Running NAMEOFYOURTOOL")
		NAMEOFYOURTOOL(url). # Add your function name created above
```
## How to run the tool

#### Step 1 : Download the Thechillar.py from repo

#### Step 2 : Run the Below command from terminal
eg:Python3 Thechillar.py www.google.com
