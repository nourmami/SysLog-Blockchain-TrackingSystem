# SysLog-Blockchain-TrackingSystem




## Description

To better understand the concept of Tracking Syslogs , let's put ourselves in a situation
where we have our node as a machine , an attacker wants to get privileged access but fails to get the
password several times. However , this event is obviously logged within the system logs, but our
ultimate goal is to add it to a decentralized immutable ledger . So that every node can see it and it can’t
be removed or deleted, which is one of the main blockchain characteristics.
That’s where we thought of adding logs as our assets . This will give us the ability to record everything
in the blockchain with several parameters such as (facility, severity , time ,hostname, syslogtag, msg),
and with many tools like SIEM , we will be able to monitor daily activity on a private blockchain network,
and track any unusual event.


## Edit your SysLog file ( `/etc/rsyslog.conf ` file)
we add a specific template so that it can be saved to our filname.txt as shown below

```shell $template class, "%syslogseverity%, %syslogfacility%, %timegenerated%,
%HOSTNAME%, %syslogtag%, %msg%\n"
*.* {{your-directory }}/test-network/filename.txt;class 
```

## start your rsyslog service 
``` sudo service rsyslog start ```
## Implementing the test network
``` ./network.sh down ``` This command removes any containers or artifacts from any previous runs

``` ./network.sh up ``` This command creates a Fabric network that consists of two peer nodes

``` ./network.sh createChannel ``` This command creates a channel between Org1 and Org2 and join their
peers to the channel

``` ./network.sh deployCC -ccn basic -ccp ../asset-transfer-basic/chaincode-go -ccl go ``` This command will install the asset-transfer chaincode on peer0.org1.example.com and
peer0.org2.example.com and then deploy the chaincode on the channel (or mychannel if no channel is
specified).


## Python Script  [here](../scripts/mine.py)
          section_title<a name="section_name"></a>
```python import os
import time
lines=5
with open("filename.txt") as file:
for line in file:
pass
last_line = line
while(1):
with open("filename.txt") as file:
for line in file:
pass
if (last_line != line):
splited = last_line.split(', ')
msg = splited[2]+ splited[4]+splited[5]
msg = msg.replace(' ', '_')
msg = msg.replace('(', '_')
msg = msg.replace(')', '_')
shell='LOG'+str(lines)+' '+msg.strip()+' '+str(splited[0])+'
'+str(splited[3])+' '+str(splited[1])
#print (shell)
os.system('./shell.sh '+shell)
lines+=1
time.sleep(3)
last_line=line
```

This script calls the [shell.sh](../scripts/shell.sh) (shell script ) in which we find the following commands:

```python
peer chaincode invoke -o localhost:7050 --ordererTLSHostnameOverrideorderer.example.com --tls --cafile
${PWD}/organizations/ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/tlsca.example.com-cert.pem -C mychannel -n basic --peerAddresseslocalhost:7051 --tlsRootCertFiles
${PWD}/organizations/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt --peerAddresses localhost:9051 --tlsRootCertFiles
${PWD}/organizations/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.crt -c '{"function":"CreateAsset","Args ["'$1'","'$2'","'$3'","'$4'","'$5'"]}'
```

The previous command initializes the ledger with assets, query it with special arguments specified in
the miner.py (like the severity, facility and time of each log).

## changing go files 
[assetTransfer.go](..\asset-transfer-ledger-queries\chaincode-go\asset_transfer_ledger_chaincode.go)
[smartcontract.go](..\asset-transfer-abac\chaincode-go\smartContract.go)

## deployement 

An attacker wants to get privileged access with the wrong password.
![alt text](https://github.com/nourmami/SysLog-Blockchain-TrackingSystem/src/readme-images/1.png"image 1")
![alt text](https://github.com/nourmami/SysLog-Blockchain-TrackingSystem/src/readme-images/2.png"image 2")
The log is then added in the filename.txt as follows:
![alt text](https://github.com/nourmami/SysLog-Blockchain-TrackingSystem/src/readme-images/1.png"image 1")
After setting up our network as explained previously, the python script mine.py will add new blocks
4
of system Logs into our blockchain (invoking chaincode queries).


