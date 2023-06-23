# Self_API_Azure

#Build as docker
#docker build -t Self_API .

#Run as docker
#docker run -e sub=cb91faf5-edaf-468d-a748-9a7e833ab3f5 -e client=<Client ID for Azure service principle> -e tenant=<tenant ID for Azure service principle> -e secret=<secret for Azure service principle> -e auth=<page auth> -p 9898:9898 test:latest

#Visit
#Post for start VM and stop
#curl -X POST -H "Content-Type: application/json" -d "{\"VM\": \"<VM name>\", \"RG\": \"<Resource Group name>\"}" http://<IP>:9898/<page auth>/startvm
#curl -X POST -H "Content-Type: application/json" -d "{\"VM\": \"<VM name>\", \"RG\": \"<Resource Group name>\"}" http://<IP>:9898/<page auth>/stopvm

#post for WOL for PC:
#curl -X POST -H "Content-Type: application/json" -d "{\"mac\": \"<Mac address>"}" http://<IP>:9898/<page auth>/wol
