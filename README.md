![alt text](https://github.com/maketheworldsecure/Thechillar/blob/main/chillarlogo.jpg)
# The chillar
#### Automation tool used to run multiple tools in single script, basically you can run this script and go chill.The script have the feature to add your custom tools to the execution list.
---------------------------
## Tools in the list
* NAMP
* NIKTO
* GOBUSTER
* TESTSSL
## Instruction to add new tool
#### Step 1 : Install the tool **eg:Testssl** in your linux machine
#### Step 2 : Add the functiion to the script
```python
def NAMEOFYOURTOOL(url):
	with open ('NAMEOFYOURTOOL.txt','w')as f1:
		t1 =subprocess.run(['COMMAND','COMMAND',url],stdout=f1,text= 'true')  # eg : t1 =subprocess.run(['nmap','-sV',url],stdout=f1,text= 'true')		
```
