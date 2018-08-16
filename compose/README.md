Prerequisites:
- Install Docker on Windows (https://docs.docker.com/docker-for-windows/)

Note: I have set up and tested the applications on Windows 10 Pro laptop. 
Using Docker for Windows on Windows 10 Pro, you must also switch to Linux containers.

============= SETUP =============
- Open a Windows PowerShell
- Go to your application directory (where you store the directories and files of your 
message queue project) and run the running_services.sh script

e.g. PS D:\github\mq-app\compose> .\running_services.sh


============= TEST =============
1. Open a command prompt window (CMD), and execute curl command to do HTTP Post to 
the localhost at port 443 http://127.0.0.1:443/

C:\Users\T901>curl -k --data "text=HELLO" http://127.0.0.1:443/

2. Open web browser, e.g. Chrome, and browser to the localhost at port 5000 http://127.0.0.1:5000
You would see the text, for example: HELLO, on the web page.

3. Change the text parameter in the curl command, then repeat the curl command on the command prompt and 
check the web page is updated with the new message
