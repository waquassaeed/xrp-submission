# IE Tech Challenge Submission

The package includes a python script for calling rippled's server_info command along with a text file for plotting the graph using the gnuplot program. The output result set is stored in two different files: data.csv stores data being captured through server_info and dataplot.csv is being used for plotting the data point. 


**Script Files:** xrpcode.py and xrpgnuplot.text

**Output Files:** data.csv and dataplot.csv

**Graph Image:** graph.png file for showing data points



**1. How does your script work?**

The python script has 4 functions and is responsible for performing small tasks such as sending a request, writing data, and reading the data points. The script starts with startTimer() function where a loop is initiated for calling server_info command at a certain interval using myPeriodicFunction() function. The result set is then written off in a file (data.csv) with comma-separated values. Subsequently, dataManipulation() function is being called for calculating the min, max, and average time and lastly getTimeSeq() is executed for storing data points in a file (dataplot.csv) being used for the gnuplot program.

**2. How did youdecide on your polling interval?**

I have tried sending server_info requests at a different interval and observed a few points:
  - If an interval is short then the data remains unchanged and the same ledger sequence is being received. 
  - If an interval is prolonged then there is a chance that someone of the ledgers' sequence is skipped during the subsequent request. 
  - The request, response and network time is also an important factor for interval selection. The network time and geographic location are most important as there could be scenarios where a similar or different response is being sent by the rippled server.

Based on the factors and analysis by sending multiple requests at a different time with interval, the polling interval is set to 4 seconds. At this polling interval, data received has an incremented sequence but in a few cases, the ledger's sequence is skipped.

**3. What do the results tell you?**

The results show how many transactions are submitted in the ledger over time basked on the computation by other network computers and are stored in the rippled database. This is the current ledger state in the ripple network where ledger information is received by querying server_info command from the rippled database. The different elements of server_info command response depict valuable information as ledger sequence, validators, connected peers, and validated ledger details such as fee, current ledger sequence, and minimum validators.

**4. Whatmight explain the variation in time between new ledgers?**

XRP Ledger is a decentralized network creating a peer to peer transaction model where a transaction is validated based on the general rules. This has brought a concept of consensus problem where a vast majority is agreed to accept a value that is required in order to make system fault-tolerant. A similar concept is being used in XRP Ledger which ensures that participant can submit their transaction and can be validated based on the consensus rule and principles with a majority of votes to become the part of the validated ledger on the network. If we look at the data being received by server_info command, it is clearly stated that each validated sequence is a block or set of transactions were submitted and were available for consensus rounds by the participants and validators who were going to validate all transaction or a group of transactions to make them available as a validated ledger. This requires connected peers to work on the computation model that takes time in accepting, agreeing, and validating the block into the rippled database and due to that, every ledger sequence is timely varied with a few seconds.



**Bonus questions # 1**

The calculations are included in the xrpcode.py script and results are displayed when the code execution is completed.

**Bonus questions # 2**

There is an API method (method name: ledger) available that can be used to retrieve the ledger information based on ledger_index parameter value such as validated, closed, and current. By using this parameter, time can be calculated for the closed or validated ledger. There is an optional parameter that can also be used to fetch queued transactions and is only applicable when ledger_index is set to current. Reference link: https://xrpl.org/ledger.html
