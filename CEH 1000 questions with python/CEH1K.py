'''
def question#():


'''


import os
from time import sleep
correct = 0

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 1

What does the -oX flag do in an Nmap scan?
\nA. Perform an express scan
B. Output the results in truncated format to the screen 
C. Perform an Xmas scan
D. Output the results in XML format to a file''')


com = input("Your Answer:  ")
answer = ('''D''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)


os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 2
    
You are a security officer of a company. You had an alert from IDS that indicates that one PC on your Intranet is connected to a blacklisted IP address (C2 Server)
on the Internet. The IP address was blacklisted just before the alert. You are staring an investigation to roughly analyze the severity of the situation. Which of the
following is appropriate to analyze?
\nA. Event logs on the PC
B. Internet Firewall/Proxy log
C. IDS log
D. Event logs on domain controller''')


com = input("Answer:  ")
answer = ('''B''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)
    

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 3
    
Which of the below hashing functions are not recommended for use?
\nA. SHA-1.ECC
B. MD5, SHA-1
C. SHA-2. SHA-3
D. MD5. SHA-5''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 4

You perform a scan of your company’s network and discover that TCP port 123 is open. What services by default run on TCP port 123?
\nA. Telnet
B. POP3
C. Network Time Protocol
D. DNS''')


com = input("Answer:  ")
answer = ('''C''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 5

Assume a business-crucial web-site of some company that is used to sell handsets to the customers worldwide. All the developed components are reviewed by the
security team on a monthly basis. In order to drive business further, the web-site developers decided to add some 3rd party marketing tools on it. The tools are
written in JavaScript and can track the customer’s activity on the site. These tools are located on the servers of the marketing company.
What is the main security risk associated with this scenario?
\nA. External script contents could be maliciously modified without the security team knowledge
B. External scripts have direct access to the company servers and can steal the data from there
C. There is no risk at all as the marketing services are trustworthy
D. External scripts increase the outbound company data traffic which leads greater financial losses''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 6

Code injection is a form of attack in which a malicious user:
\nA. Inserts text into a data field that gets interpreted as code
B. Gets the server to execute arbitrary code using a buffer overflow
C. Inserts additional code into the JavaScript running in the browser
D. Gains access to the codebase on the server and inserts new code''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 7

Which of the following scanning method splits the TCP header into several packets and makes it difficult for packet filters to detect the purpose of the packet?



\nA. ICMP Echo scanning
B. SYN/FIN scanning using IP fragments
C. ACK flag probe scanning
D. IPID scanning''')


com = input("Answer:  ")
answer = ('''B''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 8

Which of the following attacks exploits web age vulnerabilities that allow an attacker to force an unsuspecting user’s browser to send malicious requests they did
not intend?
\nA. Command Injection Attacks
B. File Injection Attack
C. Cross-Site Request Forgery (CSRF)
D. Hidden Field Manipulation Attack''')


com = input("Answer:  ")
answer = ('''C''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 9

Which of the following DoS tools is used to attack target web applications by starvation of available sessions on the web server?
The tool keeps sessions at halt using never-ending POST transmissions and sending an arbitrarily large content-length header value.
\nA. My Doom
B. Astacheldraht
C. R-U-Dead-Yet?(RUDY)
D. LOIC''')


com = input("Answer:  ")
answer = ('''C''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 10

Some clients of TPNQM SA were redirected to a malicious site when they tried to access the TPNQM main site. Bob, a system administrator at TPNQM SA, found
that they were victims of DNS Cache Poisoning.
What should Bob recommend to deal with such a threat?
\nA. The use of security agents in clients’ computers
B. The use of DNSSEC
C. The use of double-factor authentication
D. Client awareness''')


com = input("Answer:  ")
answer = ('''B''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 10

DHCP snooping is a great solution to prevent rogue DHCP servers on your network. Which security feature on switches leverages the DHCP snooping database
to help prevent man-in-the-middle attacks?
\nA. Port security
B. A Layer 2 Attack Prevention Protocol (LAPP)
C. Dynamic ARP inspection (DAI)
D. Spanning tree''')


com = input("Answer:  ")
answer = ('''C''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 13

You are the Network Admin, and you get a compliant that some of the websites are no longer accessible. You try to ping the servers and find them to be
reachable. Then you type the IP address and then you try on the browser, and find it to be accessible. But they are not accessible when you try using the URL.
What may be the problem?
\nA. Traffic is Blocked on UDP Port 53
B. Traffic is Blocked on UDP Port 80
C. Traffic is Blocked on UDP Port 54
D. Traffic is Blocked on UDP Port 80''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 15

You are looking for SQL injection vulnerability by sending a special character to web applications. Which of the following is the most useful for quick validation?
\nA. Double quotation
B. Backslash
C. Semicolon
D. Single quotation''')


com = input("Answer:  ")
answer = ('''D''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 19

The collection of potentially actionable, overt, and publicly available information is known as
\nA. Open-source intelligence
B. Human intelligence
C. Social intelligence
D. Real intelligence''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 22

An unauthorized individual enters a building following an employee through the employee entrance after the lunch rush. What type of breach has the individual just
performed?
\nA. Reverse Social Engineering
B. Tailgating
C. Piggybacking
D. Announced''')


com = input("Answer:  ")
answer = ('''B''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 23

Which of the following provides a security professional with most information about the system’s security posture?
\nA. Wardriving, warchalking, social engineering
B. Social engineering, company site browsing, tailgating
C. Phishing, spamming, sending trojans
D. Port scanning, banner grabbing, service identification''')


com = input("Answer:  ")
answer = ('''D''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 25

When a security analyst prepares for the formal security assessment - what of the following should be done in order to determine inconsistencies in the secure
assets database and verify that system is compliant to the minimum security baseline?
\nA. Data items and vulnerability scanning
B. Interviewing employees and network engineers
C. Reviewing the firewalls configuration
D. Source code review''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 29

What is the minimum number of network connections in a multi homed firewall?
\nA. 3
B. 5
C. 4
D. 2''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 31

Sam is working as s pen-tester in an organization in Houston. He performs penetration testing on IDS in order to find the different ways an attacker uses to evade
the IDS. Sam sends a large amount of packets to the target IDS that generates alerts, which enable Sam to hide the real traffic. What type of method is Sam using
to evade IDS?
\nA. Denial-of-Service
B. False Positive Generation
C. Insertion Attack
D. Obfuscating''')


com = input("Answer:  ")
answer = ('''B''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 34

What type of analysis is performed when an attacker has partial knowledge of inner-workings of the application?



\nA. Black-box
B. Announced
C. White-box
D. Grey-box''')


com = input("Answer:  ")
answer = ('''D''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 36

A hacker is an intelligent individual with excellent computer skills and the ability to explore a computer's software and hardware without the owner’s permission.
Their intention can either be to simply gain knowledge or to illegally make changes. Which of the following class of hacker refers to an individual who works both
offensively and defensively at various times?
\nA. Suicide Hacker
B. Black Hat
C. White Hat
D. Gray Hat''')


com = input("Answer:  ")
answer = ('''D''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 39

Identify the web application attack where the attackers exploit vulnerabilities in dynamically generated web pages to inject client-side script into web pages viewed
by other users.
\nA. SQL injection attack
B. Cross-Site Scripting (XSS)
C. LDAP Injection attack
D. Cross-Site Request Forgery (CSRF)''')


com = input("Answer:  ")
answer = ('''B''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 44

DNS cache snooping is a process of determining if the specified resource address is present in the DNS cache records. It may be useful during the examination of
the network to determine what software update resources are used, thus discovering what software is installed.
What command is used to determine if the entry is present in DNS cache?
\nA. nslookup -fullrecursive update.antivirus.com
B. dnsnooping –rt update.antivirus.com
C. nslookup -norecursive update.antivirus.com
D. dns --snoop update.antivirus.com''')


com = input("Answer:  ")
answer = ('''C''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 46

What network security concept requires multiple layers of security controls to be placed throughout an IT infrastructure, which improves the security posture of an
organization to defend against malicious attacks or potential vulnerabilities?
What kind of Web application vulnerability likely exists in their software?
\nA. Host-Based Intrusion Detection System
B. Security through obscurity
C. Defense in depth
D. Network-Based Intrusion Detection System''')


com = input("Answer:  ")
answer = ('''C''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 48

When tuning security alerts, what is the best approach?
\nA. Tune to avoid False positives and False Negatives
B. Rise False positives Rise False Negatives
C. Decrease the false positives
D. Decrease False negatives''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 51

Bob, your senior colleague, has sent you a mail regarding a deal with one of the clients. You are requested to accept the offer and you oblige. After 2 days. Bob
denies that he had ever sent a mail. What do you want to ""know"" to prove yourself that it was Bob who had send a mail?
\nA. Authentication
B. Confidentiality
C. Integrity



D. Non-Repudiation''')


com = input("Answer:  ")
answer = ('''D''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 53

Why containers are less secure that virtual machines?
\nA. Host OS on containers has a larger surface attack.
B. Containers may full fill disk space of the host.
C. A compromise container may cause a CPU starvation of the host.
D. Containers are attached to the same virtual network.''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 56

Developers at your company are creating a web application which will be available for use by anyone on the Internet, The developers have taken the approach of
implementing a Three-Tier Architecture for the web application. The developers are now asking you which network should the Presentation Tier (front- end web
server) be placed in?
\nA. isolated vlan network
B. Mesh network
C. DMZ network
D. Internal network''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 58

An attacker, using a rogue wireless AP, performed an MITM attack and injected an HTML code to embed a malicious applet in all HTTP connections.
When users accessed any page, the applet ran and exploited many machines. Which one of the following tools the hacker probably used to inject HTML code?
\nA. Wireshark
B. Ettercap
C. Aircrack-ng
D. Tcpdump''')


com = input("Answer:  ")
answer = ('''B''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 61

Email is transmitted across the Internet using the Simple Mail Transport Protocol. SMTP does not encrypt email, leaving the information in the message vulnerable
to being read by an unauthorized person. SMTP can upgrade a connection between two mail servers to use TLS. Email transmitted by SMTP over TLS is
encrypted. What is the name of the command used by SMTP to transmit email over TLS?
\nA. OPPORTUNISTICTLS STARTTLS
B. FORCETLS
C. UPGRADETLS''')


com = input("Answer:  ")
answer = ('''B''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 63

In which of the following password protection technique, random strings of characters are added to the password before calculating their hashes?
\nA. Keyed Hashing
B. Key Stretching
C. Salting
D. Double Hashing''')


com = input("Answer:  ")
answer = ('''C''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 64

The network team has well-established procedures to follow for creating new rules on the firewall. This includes having approval from a manager prior to
implementing any new rules. While reviewing the firewall configuration, you notice a recently implemented rule but cannot locate manager approval for it. What
would be a good step to have in the procedures for a situation like this?
\nA. Have the network team document the reason why the rule was implemented without prior manager approval.
B. Monitor all traffic using the firewall rule until a manager can approve it.
C. Do not roll back the firewall rule as the business may be relying upon it, but try to get manager approval as soon as possible.
D. Immediately roll back the firewall rule until a manager can approve it''')


com = input("Answer:  ")
answer = ('''D''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 65

Identify the UDP port that Network Time Protocol (NTP) uses as its primary means of communication?
\nA. 123
B. 161
C. 69
D. 113''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 69

If you want only to scan fewer ports than the default scan using Nmap tool, which option would you use?
\nA. -sP
B. -P
C. -r
D. -F''')


com = input("Answer:  ")
answer = ('''B''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 74

Which of the following is an adaptive SQL Injection testing technique used to discover coding errors by inputting massive amounts of random data and observing
the changes in the output?
\nA. Function Testing
B. Dynamic Testing
C. Static Testing
D. Fuzzing Testing''')


com = input("Answer:  ")
answer = ('''D''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 78

Company XYZ has asked you to assess the security of their perimeter email gateway. From your office in New York, you craft a specially formatted email message
and send it across the Internet to an employee of Company XYZ. The employee of Company XYZ is aware of your test.
Your email message looks like this: From: jim_miller@companyxyz.com
To: michelle_saunders@companyxyz.com Subject: Test message
Date: 4/3/2017 14:37
The employee of Company XYZ receives your email message. This proves that Company XYZ's email gateway doesn't prevent what?
\nA. Email Phishing
B. Email Masquerading
C. Email Spoofing
D. Email Harvesting''')


com = input("Answer:  ")
answer = ('''C''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 83

Analyst is investigating proxy logs and found out that one of the internal user visited website storing suspicious Java scripts. After opening one of them, he noticed
that it is very hard to understand the code and that all codes differ from the typical Java script. What is the name of this technique to hide the code and extend
analysis time?
\nA. Encryption
B. Code encoding
C. Obfuscation
D. Steganography''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 84

Which of the following Bluetooth hacking techniques does an attacker use to send messages to users without the recipient’s consent, similar to email spamming?
\nA. Bluesmacking
B. Bluesniffing
C. Bluesnarfing
D. Bluejacking''')


com = input("Answer:  ")
answer = ('''D''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 86

You are a Penetration Tester and are assigned to scan a server. You need to use a scanning technique wherein the TCP Header is split into many packets so that



it becomes difficult to detect what the packets are meant for.
Which of the below scanning technique will you use?
\nA. ACK flag scanning
B. TCP Scanning
C. IP Fragment Scanning
D. Inverse TCP flag scanning''')


com = input("Answer:  ")
answer = ('''C''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 91

A hacker named Jack is trying to compromise a bank’s computer system. He needs to know the operating
system of that computer to launch further attacks. What process would help him?
\nA. Banner Grabbing
B. IDLE/IPID Scanning
C. SSDP Scanning
D. UDP Scanning''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 93

What type of vulnerability/attack is it when the malicious person forces the user’s browser to send an authenticated request to a server?
\nA. Cross-site request forgery
B. Cross-site scripting
C. Session hijacking
D. Server side request forgery''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 97

Which Nmap option would you use if you were not concerned about being detected and wanted to perform a very fast scan?
\nA. –T0
B. –T5
C. -O
D. -A''')


com = input("Answer:  ")
answer = ('''B''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 100

Bob finished a C programming course and created a small C application to monitor the network traffic and produce alerts when any origin sends “many” IP
packets, based on the average number of packets sent by all origins and using some thresholds.
In concept, the solution developed by Bob is actually:
\nA. Just a network monitoring tool
B. A signature-based IDS
C. A hybrid IDS
D. A behavior-based IDS''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 105

The use of technologies like IPSec can help guarantee the following: authenticity, integrity, confidentiality and
\nA. non-repudiation.
B. operability.
C. security.
D. usability.''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 109

Which of the following processes evaluates the adherence of an organization to its stated security policy?
\nA. Vulnerability assessment
B. Penetration testing
C. Risk assessment
D. Security auditing''')


com = input("Answer:  ")
answer = ('''D''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 111

The precaution of prohibiting employees from bringing personal computing devices into a facility is what type of security control?
\nA. Physical
B. Procedural
C. Technical
D. Compliance''')


com = input("Answer:  ")
answer = ('''B''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 112

Which tool would be used to collect wireless packet data?
\nA. NetStumbler
B. John the Ripper
C. Nessus
D. Netcat''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 113

After gaining access to the password hashes used to protect access to a web based application, knowledge of which cryptographic algorithms would be useful to
gain access to the application?
\nA. SHA1
B. Diffie-Helman
C. RSA
D. AES''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 116

Which of the following open source tools would be the best choice to scan a network for potential targets?
\nA. NMAP
B. NIKTO
C. CAIN
D. John the Ripper''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 119

Which property ensures that a hash function will not produce the same hashed value for two different messages?
\nA. Collision resistance
B. Bit length
C. Key strength
D. Entropy''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 123

What is one thing a tester can do to ensure that the software is trusted and is not changing or tampering with critical data on the back end of a system it is loaded
on?
\nA. Proper testing
B. Secure coding principles
C. Systems security and architecture review
D. Analysis of interrupts within the software''')


com = input("Answer:  ")
answer = ('''D''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 126

What are the three types of authentication?
\nA. Something you: know, remember, prove



B. Something you: have, know, are
C. Something you: show, prove, are
D. Something you: show, have, prove''')


com = input("Answer:  ")
answer = ('''B''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 129

Which of the following resources does NMAP need to be used as a basic vulnerability scanner covering several vectors like SMB, HTTP and FTP?
\nA. Metasploit scripting engine
B. Nessus scripting engine
C. NMAP scripting engine
D. SAINT scripting engine''')


com = input("Answer:  ")
answer = ('''C''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 131

A tester has been hired to do a web application security test. The tester notices that the site is dynamic and must make use of a back end database.
In order for the tester to see if SQL injection is possible, what is the first character that the tester should use to attempt breaking a valid SQL request?
\nA. Semicolon
B. Single quote
C. Exclamation mark
D. Double quote''')


com = input("Answer:  ")
answer = ('''B''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 132

A security consultant decides to use multiple layers of anti-virus defense, such as end user desktop anti-virus and E-mail gateway. This approach can be used to
mitigate which kind of attack?
\nA. Forensic attack
B. ARP spoofing attack
C. Social engineering attack
D. Scanning attack''')


com = input("Answer:  ")
answer = ('''C''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 133

WPA2 uses AES for wireless data encryption at which of the following encryption levels?
\nA. 64 bit and CCMP
B. 128 bit and CRC
C. 128 bit and CCMP
D. 128 bit and TKIP''')


com = input("Answer:  ")
answer = ('''C''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 138

Which type of scan is used on the eye to measure the layer of blood vessels?
\nA. Facial recognition scan
B. Retinal scan
C. Iris scan
D. Signature kinetics scan''')


com = input("Answer:  ")
answer = ('''B''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 142

An attacker uses a communication channel within an operating system that is neither designed nor intended to transfer information. What is the name of the
communications channel?
\nA. Classified
B. Overt
C. Encrypted
D. Covert''')


com = input("Answer:  ")
answer = ('''D''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 147




Which protocol and port number might be needed in order to send log messages to a log analysis tool that resides behind a firewall?
\nA. UDP 123
B. UDP 541
C. UDP 514
D. UDP 415''')


com = input("Answer:  ")
answer = ('''C''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 148

During a wireless penetration test, a tester detects an access point using WPA2 encryption. Which of the following attacks should be used to obtain the key?
\nA. The tester must capture the WPA2 authentication handshake and then crack it.
B. The tester must use the tool inSSIDer to crack it using the ESSID of the network.
C. The tester cannot crack WPA2 because it is in full compliance with the IEEE 802.11i standard.
D. The tester must change the MAC address of the wireless network card and then use the AirTraf tool to obtain the key.''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 149

What is the main disadvantage of the scripting languages as opposed to compiled programming languages?
\nA. Scripting languages are hard to learn.
B. Scripting languages are not object-oriented.
C. Scripting languages cannot be used to create graphical user interfaces.
D. Scripting languages are slower because they require an interpreter to run the code.''')


com = input("Answer:  ")
answer = ('''D''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 152

A hacker, who posed as a heating and air conditioning specialist, was able to install a sniffer program in a switched environment network. Which attack could the
hacker use to sniff all of the packets in the network?
\nA. Fraggle
B. MAC Flood
C. Smurf
D. Tear Drop''')


com = input("Answer:  ")
answer = ('''B''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 153

Which of the following can the administrator do to verify that a tape backup can be recovered in its entirety?
\nA. Restore a random file.
B. Perform a full restore.
C. Read the first 512 bytes of the tape.
D. Read the last 512 bytes of the tape.''')


com = input("Answer:  ")
answer = ('''B
Explanation:
A full restore is required.''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 157

While conducting a penetration test, the tester determines that there is a firewall between the tester's machine and the target machine. The firewall is only
monitoring TCP handshaking of packets at the session layer of the OSI model. Which type of firewall is the tester trying to traverse?
\nA. Packet filtering firewall
B. Application-level firewall
C. Circuit-level gateway firewall
D. Stateful multilayer inspection firewall''')


com = input("Answer:  ")
answer = ('''C''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 160

A security consultant is trying to bid on a large contract that involves penetration testing and reporting. The company accepting bids wants proof of work so the
consultant prints out several audits that have been performed. Which of the following is likely to occur as a result?
\nA. The consultant will ask for money on the bid because of great work.
B. The consultant may expose vulnerabilities of other companies.



C. The company accepting bids will want the same type of format of testing.
D. The company accepting bids will hire the consultant because of the great work performed.''')


com = input("Answer:  ")
answer = ('''B''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 161

What is the outcome of the comm”nc -l -p 2222 | nc 10.1.0.43 1234"?
\nA. Netcat will listen on the 10.1.0.43 interface for 1234 seconds on port 2222.
B. Netcat will listen on port 2222 and output anything received to a remote connection on 10.1.0.43 port 1234.
C. Netcat will listen for a connection from 10.1.0.43 on port 1234 and output anything received to port 2222.
D. Netcat will listen on port 2222 and then output anything received to local interface 10.1.0.43.''')


com = input("Answer:  ")
answer = ('''B''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 164

Which results will be returned with the following Google search query? site:target.com -site:Marketing.target.com accounting
\nA. Results matching all words in the query
B. Results matching “accounting” in domain target.com but not on the site Marketing.target.com
C. Results from matches on the site marketing.target.com that are in the domain target.com but do not include the word accounting
D. Results for matches on target.com and Marketing.target.com that include the word “accounting”''')


com = input("Answer:  ")
answer = ('''B''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 168

A Network Administrator was recently promoted to Chief Security Officer at a local university. One of employee's new responsibilities is to manage the
implementation of an RFID card access system to a new server room on campus. The server room will house student enrollment information that is securely
backed up to an off-site location.
During a meeting with an outside consultant, the Chief Security Officer explains that he is concerned that the existing security controls have not been designed
properly. Currently, the Network Administrator is
responsible for approving and issuing RFID card access to the server room, as well as reviewing the electronic access logs on a weekly basis.
Which of the following is an issue with the situation?
\nA. Segregation of duties
B. Undue influence
C. Lack of experience
D. Inadequate disaster recovery plan''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 171

Which type of intrusion detection system can monitor and alert on attacks, but cannot stop them?
\nA. Detective
B. Passive
C. Intuitive
D. Reactive''')


com = input("Answer:  ")
answer = ('''B''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 176

Which of the following techniques does a vulnerability scanner use in order to detect a vulnerability on a target service?
\nA. Port scanning
B. Banner grabbing
C. Injecting arbitrary data
D. Analyzing service response''')


com = input("Answer:  ")
answer = ('''D''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 179

A consultant is hired to do physical penetration testing at a large financial company. In the first day of his assessment, the consultant goes to the company`s
building dressed like an electrician and waits in the lobby for an employee to pass through the main access gate, then the consultant follows the employee behind
to get into the restricted are\nA. Which type of attack did the consultant perform?
\nA. Man trap
B. Tailgating
C. Shoulder surfing
D. Social engineering''')


com = input("Answer:  ")
answer = ('''B''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 180

When an alert rule is matched in a network-based IDS like snort, the IDS does which of the following?
\nA. Drops the packet and moves on to the next one
B. Continues to evaluate the packet until all rules are checked
C. Stops checking rules, sends an alert, and lets the packet continue
D. Blocks the connection with the source IP address in the packet''')


com = input("Answer:  ")
answer = ('''B''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 181

A hacker is attempting to use nslookup to query Domain Name Service (DNS). The hacker uses the nslookup interactive mode for the search. Which command
should the hacker type into the command shell to request the appropriate records?
\nA. Locate type=ns
B. Request type=ns
C. Set type=ns
D. Transfer type=ns''')


com = input("Answer:  ")
answer = ('''C''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 184

Which of the following is used to indicate a single-line comment in structured query language (SQL)?
\nA. --
B. ||
C. %%
D. ''''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 188

When using Wireshark to acquire packet capture on a network, which device would enable the capture of all traffic on the wire?
\nA. Network tap
B. Layer 3 switch
C. Network bridge
D. Application firewall''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 192

What technique is used to perform a Connection Stream Parameter Pollution (CSPP) attack?
\nA. Injecting parameters into a connection string using semicolons as a separator
B. Inserting malicious Javascript code into input parameters
C. Setting a user's session identifier (SID) to an explicit known value
D. Adding multiple parameters with the same name in HTTP requests''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 195

A hacker is attempting to see which ports have been left open on a network. Which NMAP switch would the hacker use?
\nA. -sO
B. -sP
C. -sS
D. -sU''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 198

Which NMAP command combination would let a tester scan every TCP port from a class C network that is blocking ICMP with fingerprinting and service detection?
\nA. NMAP -PN -A -O -sS 192.168.2.0/24
B. NMAP -P0 -A -O -p1-65535 192.168.0/24



C. NMAP -P0 -A -sT -p0-65535 192.168.0/16
D. NMAP -PN -O -sS -p 1-1024 192.168.0/8''')


com = input("Answer:  ")
answer = ('''B''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 200

Which of the following is an example of an asymmetric encryption implementation?
\nA. SHA1
B. PGP
C. 3DES
D. MD5''')


com = input("Answer:  ")
answer = ('''B''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 205

A company is using Windows Server 2003 for its Active Directory (AD). What is the most efficient way to crack the passwords for the AD users?
\nA. Perform a dictionary attack.
B. Perform a brute force attack.
C. Perform an attack with a rainbow table.
D. Perform a hybrid attack.''')


com = input("Answer:  ")
answer = ('''C''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 208

A penetration tester was hired to perform a penetration test for a bank. The tester began searching for IP ranges owned by the bank, performing lookups on the
bank's DNS servers, reading news articles online about the bank, watching what times the bank employees come into work and leave from work, searching the
bank's job postings (paying special attention to IT related jobs), and visiting the local dumpster for the bank's corporate office. What phase of the penetration test is
the tester currently in?
\nA. Information reporting
B. Vulnerability assessment
C. Active information gathering
D. Passive information gathering''')


com = input("Answer:  ")
answer = ('''D''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 212

Which security control role does encryption meet?
\nA. Preventative
B. Detective
C. Offensive
D. Defensive''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 216

In order to show improvement of security over time, what must be developed?
\nA. Reports
B. Testing tools
C. Metrics
D. Taxonomy of vulnerabilities''')


com = input("Answer:  ")
answer = ('''C
Explanation:
Today, management demands metrics to get a clearer view of security.
Metrics that measure participation, effectiveness, and window of exposure, however, offer information the organization can use to make plans and improve
programs.
References:
http://www.infoworld.com/article/2974642/security/4-security-metrics-that-matter.html''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 220

How is sniffing broadly categorized?
\nA. Active and passive
B. Broadcast and unicast
C. Unmanaged and managed



D. Filtered and unfiltered''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 224

Fingerprinting VPN firewalls is possible with which of the following tools?
\nA. Angry IP
B. Nikto
C. Ike-scan
D. Arp-scan''')


com = input("Answer:  ")
answer = ('''C''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 229

Which tool can be used to silently copy files from USB devices?
\nA. USB Grabber
B. USB Dumper
C. USB Sniffer
D. USB Snoopy''')


com = input("Answer:  ")
answer = ('''B''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 232

Which of the following is a strong post designed to stop a car?
\nA. Gate
B. Fence
C. Bollard
D. Reinforced rebar''')


com = input("Answer:  ")
answer = ('''C''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 234

An NMAP scan of a server shows port 25 is open. What risk could this pose?
\nA. Open printer sharing
B. Web portal data leak
C. Clear text authentication
D. Active mail relay''')


com = input("Answer:  ")
answer = ('''D''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 236

To send a PGP encrypted message, which piece of information from the recipient must the sender have before encrypting the message?
\nA. Recipient's private key
B. Recipient's public key
C. Master encryption key
D. Sender's public key''')


com = input("Answer:  ")
answer = ('''B''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 240

Which of the following conditions must be given to allow a tester to exploit a Cross-Site Request Forgery (CSRF) vulnerable web application?
\nA. The victim user must open the malicious link with an Internet Explorer prior to version 8.
B. The session cookies generated by the application do not have the HttpOnly flag set.
C. The victim user must open the malicious link with a Firefox prior to version 3.
D. The web application should not use random tokens.''')


com = input("Answer:  ")
answer = ('''D''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 245

A hacker is attempting to see which IP addresses are currently active on a network. Which NMAP switch would the hacker use?
\nA. -sO



B. -sP
C. -sS
D. -sU''')


com = input("Answer:  ")
answer = ('''B''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 246

A penetration tester is attempting to scan an internal corporate network from the internet without alerting the border sensor. Which is the most efficient technique
should the tester consider using?
\nA. Spoofing an IP address
B. Tunneling scan over SSH
C. Tunneling over high port numbers
D. Scanning using fragmented IP packets''')


com = input("Answer:  ")
answer = ('''B''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 248

During a penetration test, the tester conducts an ACK scan using NMAP against the external interface of the DMZ firewall. NMAP reports that port 80 is unfiltered.
Based on this response, which type of packet inspection is the firewall conducting?
\nA. Host
B. Stateful
C. Stateless
D. Application''')


com = input("Answer:  ")
answer = ('''C''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 253

An NMAP scan of a server shows port 69 is open. What risk could this pose?
\nA. Unauthenticated access
B. Weak SSL version
C. Cleartext login
D. Web portal data leak''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 256

Which command line switch would be used in NMAP to perform operating system detection?
\nA. -OS
B. -sO
C. -sP
D. -O''')


com = input("Answer:  ")
answer = ('''D''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 260

What is the main difference between a “Normal” SQL Injection and a “Blind” SQL Injection vulnerability?
\nA. The request to the web server is not visible to the administrator of the vulnerable application.
B. The attack is called “Blind” because, although the application properly filters user input, it is still vulnerable to code injection.
C. The successful attack does not show an error message to the administrator of the affected application.
D. The vulnerable application does not display errors with information about the injection results to the attacker.''')


com = input("Answer:  ")
answer = ('''D''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 265

Which of the following programming languages is most vulnerable to buffer overflow attacks?
\nA. Perl
B. C++
C. Python
D. Java''')


com = input("Answer:  ")
answer = ('''B''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 266




A hacker searches in Google for filetype:pcf to find Cisco VPN config files. Those files may contain connectivity passwords that can be decoded with which of the
following?
\nA. Cupp
B. Nessus
C. Cain and Abel
D. John The Ripper Pro''')


com = input("Answer:  ")
answer = ('''C''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 270

Which tool is used to automate SQL injections and exploit a database by forcing a given web application to connect to another database controlled by a hacker?
\nA. DataThief
B. NetCat
C. Cain and Abel
D. SQLInjector''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 271

A company has hired a security administrator to maintain and administer Linux and Windows-based systems. Written in the nightly report file is the following:
Firewall log files are at the expected value of 4 MB. The current time is 12am. Exactly two hours later the size has decreased considerably. Another hour goes by
and the log files have shrunk in size again.
Which of the following actions should the security administrator take?
\nA. Log the event as suspicious activity and report this behavior to the incident response team immediately.
B. Log the event as suspicious activity, call a manager, and report this as soon as possible.
C. Run an anti-virus scan because it is likely the system is infected by malware.
D. Log the event as suspicious activity, continue to investigate, and act according to the site's security policy.''')


com = input("Answer:  ")
answer = ('''D''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 275

ICMP ping and ping sweeps are used to check for active systems and to check
\nA. if ICMP ping traverses a firewall.
B. the route that the ICMP ping took.
C. the location of the switchport in relation to the ICMP ping.
D. the number of hops an ICMP ping takes to reach a destination.''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 279

One way to defeat a multi-level security solution is to leak data via
\nA. a bypass regulator.
B. steganography.
C. a covert channel.
D. asymmetric routing.''')


com = input("Answer:  ")
answer = ('''C''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 283

What is the correct PCAP filter to capture all TCP traffic going to or from host 192.168.0.125 on port 25?
\nA. tcp.src == 25 and ip.host == 192.168.0.125
B. host 192.168.0.125:25
C. port 25 and host 192.168.0.125
D. tcp.port == 25 and ip.host == 192.168.0.125''')


com = input("Answer:  ")
answer = ('''D''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 285

Which of the following items of a computer system will an anti-virus program scan for viruses?
\nA. Boot Sector
B. Deleted Files
C. Windows Process List
D. Password Protected Files''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 288

What is the broadcast address for the subnet 190.86.168.0/22?
\nA. 190.86.168.255
B. 190.86.255.255
C. 190.86.171.255
D. 190.86.169.255''')


com = input("Answer:  ")
answer = ('''C''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 293

A bank stores and processes sensitive privacy information related to home loans. However, auditing has never been enabled on the system. What is the first step
that the bank should take before enabling the audit feature?
\nA. Perform a vulnerability scan of the system.
B. Determine the impact of enabling the audit feature.
C. Perform a cost/benefit analysis of the audit feature.
D. Allocate funds for staffing of audit log review.''')


com = input("Answer:  ")
answer = ('''B''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 294

Which of the following programs is usually targeted at Microsoft Office products?
\nA. Polymorphic virus
B. Multipart virus
C. Macro virus
D. Stealth virus''')


com = input("Answer:  ")
answer = ('''C
Explanation:
A macro virus is a virus that is written in a macro language: a programming language which is embedded inside a software application (e.g., word processors and
spreadsheet applications). Some applications, such as Microsoft Office, allow macro programs to be embedded in documents such that the macros are run
automatically when the document is opened, and this provides a distinct mechanism by which malicious computer instructions can spread.
References: https://en.wikipedia.org/wiki/Macro_virus''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 299

Which of the following is a client-server tool utilized to evade firewall inspection?
\nA. tcp-over-dns
B. kismet
C. nikto
D. hping''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 302

Which of the following viruses tries to hide from anti-virus programs by actively altering and corrupting the chosen service call interruptions when they are being
run?
\nA. Cavity virus
B. Polymorphic virus
C. Tunneling virus
D. Stealth virus''')


com = input("Answer:  ")
answer = ('''D''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 303

A large company intends to use Blackberry for corporate mobile phones and a security analyst is assigned to evaluate the possible threats. The analyst will use the
Blackjacking attack method to demonstrate how an attacker could circumvent perimeter defenses and gain access to the corporate network. What tool should the
analyst use to perform a Blackjacking attack?
\nA. Paros Proxy
B. BBProxy
C. BBCrack
D. Blooover''')


com = input("Answer:  ")
answer = (''' 



B
Explanation:
Blackberry users warned of hacking tool threat.
Users have been warned that the security of Blackberry wireless e-mail devices is at risk due to the availability this week of a new hacking tool. Secure Computing
Corporation said businesses that have installed Blackberry servers behind their gateway security devices could be vulnerable to a hacking attack from a tool call
BBProxy.
References:
http://www.computerweekly.com/news/2240062112/Technology-news-in-brief''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 306

Which system consists of a publicly available set of databases that contain domain name registration contact information?
\nA. WHOIS
B. IANA
C. CAPTCHA
D. IETF''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 311

Which of the following settings enables Nessus to detect when it is sending too many packets and the network pipe is approaching capacity?
\nA. Netstat WMI Scan
B. Silent Dependencies
C. Consider unscanned ports as closed
D. Reduce parallel connections on congestion''')


com = input("Answer:  ")
answer = ('''D''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 315

A computer science student needs to fill some information into a secured Adobe PDF job application that was received from a prospective employer. Instead of
requesting a new document that allowed the forms to be completed, the student decides to write a script that pulls passwords from a list of commonly used
passwords to try against the secured PDF until the correct password is found or the list is exhausted.
Which cryptography attack is the student attempting?
\nA. Man-in-the-middle attack
B. Brute-force attack
C. Dictionary attack
D. Session hijacking''')


com = input("Answer:  ")
answer = ('''C''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 317

While performing data validation of web content, a security technician is required to restrict malicious input. Which of the following processes is an efficient way of
restricting malicious input?
\nA. Validate web content input for query strings.
B. Validate web content input with scanning tools.
C. Validate web content input for type, length, and range.
D. Validate web content input for extraneous queries.''')


com = input("Answer:  ")
answer = ('''C''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 321

What is the main advantage that a network-based IDS/IPS system has over a host-based solution?
\nA. They do not use host system resources.
B. They are placed at the boundary, allowing them to inspect all traffic.
C. They are easier to install and configure.
D. They will not interfere with user interfaces.''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 322

Which of the following identifies the three modes in which Snort can be configured to run?
\nA. Sniffer, Packet Logger, and Network Intrusion Detection System
B. Sniffer, Network Intrusion Detection System, and Host Intrusion Detection System
C. Sniffer, Host Intrusion Prevention System, and Network Intrusion Prevention System
D. Sniffer, Packet Logger, and Host Intrusion Prevention System''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 326

Which vital role does the U.S. Computer Security Incident Response Team (CSIRT) provide?
\nA. Incident response services to any user, company, government agency, or organization in partnership with the Department of Homeland Security
B. Maintenance of the nation’s Internet infrastructure, builds out new Internet infrastructure, and decommissions old Internet infrastructure
C. Registration of critical penetration testing for the Department of Homeland Security and public and private sectors
D. Measurement of key vulnerability assessments on behalf of the Department of Defense (DOD) and State Department, as well as private sectors''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 329

A certified ethical hacker (CEH) is approached by a friend who believes her husband is cheating. She offers to pay to break into her husband's email account in
order to find proof so she can take him to court. What is the ethical response?
\nA. Say no; the friend is not the owner of the account.
B. Say yes; the friend needs help to gather evidence.
C. Say yes; do the job for free.
D. Say no; make sure that the friend knows the risk she’s asking the CEH to take.''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 330

If an e-commerce site was put into a live environment and the programmers failed to remove the secret entry point that was used during the application
development, what is this secret entry point known as?
\nA. SDLC process
B. Honey pot
C. SQL injection
D. Trap door''')


com = input("Answer:  ")
answer = ('''D''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 335

The fundamental difference between symmetric and asymmetric key cryptographic systems is that symmetric key cryptography uses which of the following?
\nA. Multiple keys for non-repudiation of bulk data
B. Different keys on both ends of the transport medium
C. Bulk encryption for data transmission over fiber
D. The same key on each end of the transmission medium''')


com = input("Answer:  ")
answer = ('''D''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 339

The Open Web Application Security Project (OWASP) testing methodology addresses the need to secure web applications by providing which one of the following
services?
\nA. An extensible security framework named COBIT
B. A list of flaws and how to fix them
C. Web application patches
D. A security certification for hardened web applications''')


com = input("Answer:  ")
answer = ('''B''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 341

Which element of Public Key Infrastructure (PKI) verifies the applicant?
\nA. Certificate authority
B. Validation authority
C. Registration authority
D. Verification authority''')


com = input("Answer:  ")
answer = ('''C''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 345

When comparing the testing methodologies of Open Web Application Security Project (OWASP) and Open Source Security Testing Methodology Manual
(OSSTMM) the main difference is



\nA. OWASP is for web applications and OSSTMM does not include web applications.
B. OSSTMM is gray box testing and OWASP is black box testing.
C. OWASP addresses controls and OSSTMM does not.
D. OSSTMM addresses controls and OWASP does not.''')


com = input("Answer:  ")
answer = ('''D''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 348

To reduce the attack surface of a system, administrators should perform which of the following processes to remove unnecessary software, services, and insecure
configuration settings?
\nA. Harvesting
B. Windowing
C. Hardening
D. Stealthing''')


com = input("Answer:  ")
answer = ('''C''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 353

Some passwords are stored using specialized encryption algorithms known as hashes. Why is this an appropriate method?
\nA. It is impossible to crack hashed user passwords unless the key used to encrypt them is obtained.
B. If a user forgets the password, it can be easily retrieved using the hash key stored by administrators.
C. Hashing is faster compared to more traditional encryption algorithms.
D. Passwords stored using hashes are non-reversible, making finding the password much more difficult.''')


com = input("Answer:  ")
answer = ('''D''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 358

For messages sent through an insecure channel, a properly implemented digital signature gives the receiver reason to believe the message was sent by the
claimed sender. While using a digital signature, the message digest is encrypted with which key?
\nA. Sender's public key
B. Receiver's private key
C. Receiver's public key
D. Sender's private key''')


com = input("Answer:  ")
answer = ('''D''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 359

Which of the following algorithms provides better protection against brute force attacks by using a 160-bit message digest?
\nA. MD5
B. SHA-1
C. RC4
D. MD4''')


com = input("Answer:  ")
answer = ('''B''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 364

Which security strategy requires using several, varying methods to protect IT systems against attacks?
\nA. Defense in depth
B. Three-way handshake
C. Covert channels
D. Exponential backoff algorithm''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 365

Which of the following is a characteristic of Public Key Infrastructure (PKI)?
\nA. Public-key cryptosystems are faster than symmetric-key cryptosystems.
B. Public-key cryptosystems distribute public-keys within digital signatures.
C. Public-key cryptosystems do not require a secure key distribution channel.
D. Public-key cryptosystems do not provide technical non-repudiation via digital signatures.''')


com = input("Answer:  ")
answer = ('''B''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 367




Which of the following descriptions is true about a static NAT?
\nA. A static NAT uses a many-to-many mapping.
B. A static NAT uses a one-to-many mapping.
C. A static NAT uses a many-to-one mapping.
D. A static NAT uses a one-to-one mapping.''')


com = input("Answer:  ")
answer = ('''D''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 371

A consultant has been hired by the V.P. of a large financial organization to assess the company's security posture. During the security testing, the consultant
comes across child pornography on the V.P.'s computer. What is the consultant's obligation to the financial organization?
\nA. Say nothing and continue with the security testing.
B. Stop work immediately and contact the authorities.
C. Delete the pornography, say nothing, and continue security testing.
D. Bring the discovery to the financial organization's human resource department.''')


com = input("Answer:  ")
answer = ('''B''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 373

Which of the following levels of algorithms does Public Key Infrastructure (PKI) use?
\nA. RSA 1024 bit strength
B. AES 1024 bit strength
C. RSA 512 bit strength
D. AES 512 bit strength''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 377

An attacker has captured a target file that is encrypted with public key cryptography. Which of the attacks below is likely to be used to crack the target file?
\nA. Timing attack
B. Replay attack
C. Memory trade-off attack
D. Chosen plain-text attack''')


com = input("Answer:  ")
answer = ('''D''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 381

While testing the company's web applications, a tester attempts to insert the following test script into the search area on the company's web site:
<script>alert(" Testing Testing Testing ")</script>
Afterwards, when the tester presses the search button, a pop-up box appears on the screen with the text: "Testing Testing Testing". Which vulnerability has been
detected in the web application?
\nA. Buffer overflow
B. Cross-site request forgery
C. Distributed denial of service
D. Cross-site scripting''')


com = input("Answer:  ")
answer = ('''D''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 383

A technician is resolving an issue where a computer is unable to connect to the Internet using a wireless access point. The computer is able to transfer files locally
to other machines, but cannot successfully reach the Internet. When the technician examines the IP address and default gateway they are both on the
192.168.1.0/24. Which of the following has occurred?
\nA. The gateway is not routing to a public IP address.
B. The computer is using an invalid IP address.
C. The gateway and the computer are not on the same network.
D. The computer is not using a private IP address.''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 385

Which NMAP feature can a tester implement or adjust while scanning for open ports to avoid detection by the network’s IDS?
\nA. Timing options to slow the speed that the port scan is conducted
B. Fingerprinting to identify which operating systems are running on the network



C. ICMP ping sweep to determine which hosts on the network are not available
D. Traceroute to control the path of the packets sent during the scan''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 388

Employees in a company are no longer able to access Internet web sites on their computers. The network administrator is able to successfully ping IP address of
web servers on the Internet and is able to open web sites by using an IP address in place of the URL. The administrator runs the nslookup command for
www.eccouncil.org and receives an error message stating there is no response from the server. What should the administrator do next?
\nA. Configure the firewall to allow traffic on TCP ports 53 and UDP port 53.
B. Configure the firewall to allow traffic on TCP ports 80 and UDP port 443.
C. Configure the firewall to allow traffic on TCP port 53.
D. Configure the firewall to allow traffic on TCP port 8080.''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 392

Which of the following network attacks takes advantage of weaknesses in the fragment reassembly functionality of the TCP/IP protocol stack?
\nA. Teardrop
B. SYN flood
C. Smurf attack
D. Ping of death''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 396

How do employers protect assets with security policies pertaining to employee surveillance activities?
\nA. Employers promote monitoring activities of employees as long as the employees demonstrate trustworthiness.
B. Employers use informal verbal communication channels to explain employee monitoring activities to employees.
C. Employers use network surveillance to monitor employee email traffic, network access, and to record employee keystrokes.
D. Employers provide employees written statements that clearly discuss the boundaries of monitoring activities and consequences.''')


com = input("Answer:  ")
answer = ('''D''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 400

Company A and Company B have just merged and each has its own Public Key Infrastructure (PKI). What must the Certificate Authorities (CAs) establish so that
the private PKIs for Company A and Company B trust one another and each private PKI can validate digital certificates from the other company?
\nA. Poly key exchange
B. Cross certification
C. Poly key reference
D. Cross-site exchange''')


com = input("Answer:  ")
answer = ('''B''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 405

An attacker sniffs encrypted traffic from the network and is subsequently able to decrypt it. The attacker can now use which cryptanalytic technique to attempt to
discover the encryption key?
\nA. Birthday attack
B. Plaintext attack
C. Meet in the middle attack
D. Chosen ciphertext attack''')


com = input("Answer:  ")
answer = ('''D''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 407

Which United States legislation mandates that the Chief Executive Officer (CEO) and the Chief Financial Officer (CFO) must sign statements verifying the
completeness and accuracy of financial reports?
\nA. Sarbanes-Oxley Act (SOX)
B. Gramm-Leach-Bliley Act (GLBA)
C. Fair and Accurate Credit Transactions Act (FACTA)
D. Federal Information Security Management Act (FISMA)''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 410

What is the primary drawback to using advanced encryption standard (AES) algorithm with a 256 bit key to share sensitive data?
\nA. Due to the key size, the time it will take to encrypt and decrypt the message hinders efficient communication.
B. To get messaging programs to function with this algorithm requires complex configurations.
C. It has been proven to be a weak cipher; therefore, should not be trusted to protect sensitive data.
D. It is a symmetric key algorithm, meaning each recipient must receive the key through a different channel than the message.''')


com = input("Answer:  ")
answer = ('''D''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 412

Which type of security document is written with specific step-by-step details?
\nA. Process
B. Procedure
C. Policy
D. Paradigm''')


com = input("Answer:  ")
answer = ('''B''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 416

Which of the following is the least-likely physical characteristic to be used in biometric control that supports a large company?
\nA. Height and Weight
B. Voice
C. Fingerprints
D. Iris patterns''')


com = input("Answer:  ")
answer = ('''A
Explanation:
There are two main types of biometric identifiers:
Examples of physiological characteristics used for biometric authentication include fingerprints; DNA; face, hand, retina or ear features; and odor. Behavioral
characteristics are related to the pattern of the behavior of a person, such as typing rhythm, gait, gestures and voice.
References:
http://searchsecurity.techtarget.com/definition/biometrics''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 420

Perspective clients want to see sample reports from previous penetration tests. What should you do next?
\nA. Decline but, provide references.
B. Share full reports, not redacted.
C. Share full reports with redactions.
D. Share reports, after NDA is signed.''')


com = input("Answer:  ")
answer = ('''A
Explanation:
Penetration tests data should not be disclosed to third parties.''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 422

You have successfully gained access to your client's internal network and successfully comprised a Linux server which is part of the internal IP network. You want
to know which Microsoft Windows workstations have file sharing enabled.
Which port would you see listening on these Windows machines in the network?
\nA. 445
B. 3389
C. 161
D. 1433''')


com = input("Answer:  ")
answer = ('''A
Explanation:
The following ports are associated with file sharing and server message block (SMB) communications: References: https://support.microsoft.com/en-us/kb/298804''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 426

You have successfully gained access to a linux server and would like to ensure that the succeeding outgoing traffic from this server will not be caught by a Network
Based Intrusion Detection Systems (NIDS).
What is the best way to evade the NIDS?
\nA. Encryption



B. Protocol Isolation
C. Alternate Data Streams
D. Out of band signalling''')


com = input("Answer:  ")
answer = ('''A
Explanation:
When the NIDS encounters encrypted traffic, the only analysis it can perform is packet level analysis, since the application layer contents are inaccessible. Given
that exploits against today's networks are primarily targeted against network services (application layer entities), packet level analysis ends up doing very little to
protect our core business assets.
References:
http://www.techrepublic.com/article/avoid-these-five-common-ids-implementation-errors/''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 427

The purpose of a _____ is to deny network access to local area networks and other information assets by unauthorized wireless devices.
\nA. Wireless Intrusion Prevention System
B. Wireless Access Point
C. Wireless Access Control List
D. Wireless Analyzer''')


com = input("Answer:  ")
answer = ('''A
Explanation:
A wireless intrusion prevention system (WIPS) is a network device that monitors the radio spectrum for the presence of unauthorized access points (intrusion
detection), and can automatically take countermeasures (intrusion prevention).
References: https://en.wikipedia.org/wiki/Wireless_intrusion_prevention_system''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 429

How does the Address Resolution Protocol (ARP) work?
\nA. It sends a request packet to all the network elements, asking for the MAC address from a specific IP.
B. It sends a reply packet to all the network elements, asking for the MAC address from a specific IP.
C. It sends a reply packet for a specific IP, asking for the MAC address.
D. It sends a request packet to all the network elements, asking for the domain name from a specific IP.''')


com = input("Answer:  ")
answer = ('''A
Explanation:
When an incoming packet destined for a host machine on a particular local area network arrives at a gateway, the gateway asks the ARP program to find a
physical host or MAC address that matches the IP address. The ARP program looks in the ARP cache and, if it finds the address, provides it so that the packet
can be converted to the right packet length and format and sent to the machine. If no entry is found for the IP address, ARP broadcasts a request packet in a
special format to all the machines on the LAN to see if one machine knows that it has that IP address associated with it. A machine that recognizes the IP address
as its own returns a reply so indicating. ARP updates the ARP cache for future reference and then sends the packet to the MAC address that replied.
References:
http://searchnetworking.techtarget.com/definition/Address-Resolution-Protocol-ARP''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 432

You are a Network Security Officer. You have two machines. The first machine (192.168.0.99) has snort installed, and the second machine (192.168.0.150) has
kiwi syslog installed. You perform a syn scan in your network, and you notice that kiwi syslog is not receiving the alert message from snort. You decide to run
wireshark in the snort machine to check if the messages are going to the kiwi syslog machine.
What wireshark filter will show the connections from the snort machine to kiwi syslog machine?
\nA. tcp.dstport==514 && ip.dst==192.168.0.150
B. tcp.srcport==514 && ip.src==192.168.0.99
C. tcp.dstport==514 && ip.dst==192.168.0.0/16
D. tcp.srcport==514 && ip.src==192.168.150''')


com = input("Answer:  ")
answer = ('''A
Explanation:
We need to configure destination port at destination ip. The destination ip is 192.168.0.150, where the kiwi syslog is installed.
References: https://wiki.wireshark.org/DisplayFilters''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 434

env x=`() :;;echo exploit` bash -c 'cat /etc/passwd'
What is the Shellshock bash vulnerability attempting to do on a vulnerable Linux host?
\nA. Display passwd content to prompt
B. Removes the passwd file
C. Changes all passwords in passwd
D. Add new user to the passwd file''')


com = input("Answer:  ")
answer = ('''A



Explanation:
To extract private information, attackers are using a couple of techniques. The simplest extraction attacks are in the form:
() ; /bin/cat /etc/passwd
That reads the password file /etc/passwd, and adds it to the response from the web server. So an attacker injecting this code through the Shellshock vulnerability
would see the password file dumped out onto their screen as part of the web page returned.
References: https://blog.cloudflare.com/inside-shellshock/''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 436

You have successfully compromised a machine on the network and found a server that is alive on the same network. You tried to ping it but you didn't get any
response back.
What is happening?
\nA. ICMP could be disabled on the target server.
B. The ARP is disabled on the target server.
C. TCP/IP doesn't support ICMP.
D. You need to run the ping command with root privileges.''')


com = input("Answer:  ")
answer = ('''A
Explanation:
The ping utility is implemented using the ICMP "Echo request" and "Echo reply" messages.
Note: The Internet Control Message Protocol (ICMP) is one of the main protocols of the internet protocol suite. It is used by network devices, like routers, to send
error messages indicating, for example, that a requested service is not available or that a host or router could not be reached.
References: https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 441

Which of the following is the BEST way to defend against network sniffing?
\nA. Using encryption protocols to secure network communications
B. Register all machines MAC Address in a Centralized Database
C. Restrict Physical Access to Server Rooms hosting Critical Servers
D. Use Static IP Address''')


com = input("Answer:  ")
answer = ('''A
Explanation:
A way to protect your network traffic from being sniffed is to use encryption such as Secure Sockets Layer (SSL) or Transport Layer Security (TLS). Encryption
doesn't prevent packet sniffers from seeing source and destination information, but it does encrypt the data packet's payload so that all the sniffer sees is
encrypted gibberish.
References:
http://netsecurity.about.com/od/informationresources/a/What-Is-A-Packet-Sniffer.htm''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 446

When you return to your desk after a lunch break, you notice a strange email in your inbox. The sender is someone you did business with recently, but the subject
line has strange characters in it.
What should you do?
\nA. Forward the message to your company’s security response team and permanently delete the message from your computer.
B. Reply to the sender and ask them for more information about the message contents.
C. Delete the email and pretend nothing happened
D. Forward the message to your supervisor and ask for her opinion on how to handle the situation''')


com = input("Answer:  ")
answer = ('''A
Explanation:
By setting up an email address for your users to forward any suspicious email to, the emails can be automatically scanned and replied to, with security incidents
created to follow up on any emails with attached malware or links to known bad websites.
References:
https://docs.servicenow.com/bundle/helsinki-security-management/page/product/threat-intelligence/task/t_Confi''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 451

It is a short-range wireless communication technology intended to replace the cables connecting portable of fixed devices while maintaining high levels of security.
It allows mobile phones, computers and other devices to connect and communicate using a short-range wireless connection.
Which of the following terms best matches the definition?
\nA. Bluetooth
B. Radio-Frequency Identification
C. WLAN
D. InfraRed''')


com = input("Answer:  ")
answer = ('''A
Explanation:
Bluetooth is a standard for the short-range wireless interconnection of mobile phones, computers, and other electronic devices.
References:



http://www.bbc.co.uk/webwise/guides/about-bluetooth''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 453

You are attempting to man-in-the-middle a session. Which protocol will allow you to guess a sequence number?
\nA. TCP
B. UPD
C. ICMP
D. UPX''')


com = input("Answer:  ")
answer = ('''A
Explanation:
At the establishment of a TCP session the client starts by sending a SYN-packet (SYN=synchronize) with a sequence number. To hijack a session it is required to
send a packet with a right seq-number, otherwise they are dropped.
References: https://www.exploit-db.com/papers/13587/''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 455

You are using NMAP to resolve domain names into IP addresses for a ping sweep later.
Which of the following commands looks for IP addresses?
\nA. >host -t a hackeddomain.com
B. >host -t soa hackeddomain.com
C. >host -t ns hackeddomain.com
D. >host -t AXFR hackeddomain.com''')


com = input("Answer:  ")
answer = ('''A
Explanation:
The A record is an Address record. It returns a 32-bit IPv4 address, most commonly used to map hostnames to an IP address of the host.
References: https://en.wikipedia.org/wiki/List_of_DNS_record_types''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 459

During a recent security assessment, you discover the organization has one Domain Name Server (DNS) in a Demilitarized Zone (DMZ) and a second DNS server
on the internal network.
What is this type of DNS configuration commonly called?
\nA. Split DNS
B. DNSSEC
C. DynDNS
D. DNS Scheme''')


com = input("Answer:  ")
answer = ('''A
Explanation:
In a split DNS infrastructure, you create two zones for the same domain, one to be used by the internal network, the other used by the external network. Split DNS
directs internal hosts to an internal domain name server for name resolution and external hosts are directed to an external domain name server for name
resolution.
References:
http://www.webopedia.com/TERM/S/split_DNS.html''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 462

The Open Web Application Security Project (OWASP) is the worldwide not-for-profit charitable organization focused on improving the security of software. What
item is the primary concern on OWASP's Top Ten Project Most Critical Web Application Security Risks?
\nA. Injection
B. Cross Site Scripting
C. Cross Site Request Forgery
D. Path disclosure''')


com = input("Answer:  ")
answer = ('''A
Explanation:
The top item of the OWASP 2013 OWASP's Top Ten Project Most Critical Web Application Security Risks is injection.
Injection flaws, such as SQL, OS, and LDAP injection occur when untrusted data is sent to an interpreter as part of a command or query. The attacker’s hostile
data can trick the interpreter into executing unintended commands or accessing data without proper authorization.
References: https://www.owasp.org/index.php/Top_10_2013-Top_10''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 467

Which regulation defines security and privacy controls for Federal information systems and organizations?
\nA. NIST-800-53
B. PCI-DSS



C. EU Safe Harbor
D. HIPAA''')


com = input("Answer:  ")
answer = ('''A
Explanation:
NIST Special Publication 800-53, "Security and Privacy Controls for Federal Information Systems and Organizations," provides a catalog of security controls for all
U.S. federal information systems except those related to national security.
References: https://en.wikipedia.org/wiki/NIST_Special_Publication_800-53''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 471

This tool is an 802.11 WEP and WPA-PSK keys cracking program that can recover keys once enough data packets have been captured. It implements the
standard FMS attack along with some optimizations like KoreK attacks, as well as the PTW attack, thus making the attack much faster compared to other WEP
cracking tools.
Which of the following tools is being described?
\nA. Aircrack-ng
B. Airguard
C. WLAN-crack
D. wificracker''')


com = input("Answer:  ")
answer = ('''A
Explanation:
Aircrack-ng is a complete suite of tools to assess WiFi network security.
The default cracking method of Aircrack-ng is PTW, but Aircrack-ng can also use the FMS/KoreK method, which incorporates various statistical attacks to discover
the WEP key and uses these in combination with brute forcing.
References:
http://www.aircrack-ng.org/doku.php?id=aircrack-ng''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 472

Which of the following is assured by the use of a hash?
\nA. Integrity
B. Confidentiality
C. Authentication
D. Availability''')


com = input("Answer:  ")
answer = ('''A
Explanation:
An important application of secure hashes is verification of message integrity. Determining whether any changes have been made to a message (or a file), for
example, can be accomplished by comparing message digests calculated before, and after, transmission (or any other event).
References: https://en.wikipedia.org/wiki/Cryptographic_hash_function#Verifying_the_integrity_of_files_or_messages''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 474

Which tool allows analysts and pen testers to examine links between data using graphs and link analysis?
\nA. Maltego
B. Cain & Abel
C. Metasploit
D. Wireshark''')


com = input("Answer:  ")
answer = ('''A
Explanation:
Maltego is proprietary software used for open-source intelligence and forensics, developed by Paterv\nA. Maltego focuses on providing a library of transforms for
discovery of data from open sources, and visualizing that information in a graph format, suitable for link analysis and data mining.
References: https://en.wikipedia.org/wiki/Maltego''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 475

Which mode of IPSec should you use to assure security and confidentiality of data within the same LAN?
\nA. ESP transport mode
B. AH permiscuous
C. ESP confidential
D. AH Tunnel mode''')


com = input("Answer:  ")
answer = ('''A
Explanation:
When transport mode is used, IPSec encrypts only the IP payload. Transport mode provides the protection of an IP payload through an AH or ESP header.
Encapsulating Security Payload (ESP) provides confidentiality (in addition to authentication, integrity, and anti-replay protection) for the IP payload.''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 479

Which of the following is the greatest threat posed by backups?
\nA. A backup is the source of Malware or illicit information.
B. A backup is unavailable during disaster recovery.
C. A backup is incomplete because no verification was performed.
D. An un-encrypted backup can be misplaced or stolen.''')


com = input("Answer:  ")
answer = ('''D
Explanation:
If the data written on the backup media is properly encrypted, it will be useless for anyone without the key.
References:
http://resources.infosecinstitute.com/backup-media-encryption/''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 481

What is the process of logging, recording, and resolving events that take place in an organization?
\nA. Incident Management Process
B. Security Policy
C. Internal Procedure
D. Metrics''')


com = input("Answer:  ")
answer = ('''A
Explanation:
The activities within the incident management process include:
References: https://en.wikipedia.org/wiki/Incident_management_(ITSM)#Incident_management_procedure''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 485

Jimmy is standing outside a secure entrance to a facility. He is pretending to have a tense conversation on his cell phone as an authorized employee badges in.
Jimmy, while still on the phone, grabs the door as it begins to close.
What just happened?
\nA. Piggybacking
B. Masqurading
C. Phishing
D. Whaling''')


com = input("Answer:  ")
answer = ('''A
Explanation:
In security, piggybacking refers to when a person tags along with another person who is authorized to gain entry into a restricted area, or pass a certain
checkpoint.
References: https://en.wikipedia.org/wiki/Piggybacking_(security)''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 490

You just set up a security system in your network. In what kind of system would you find the following string of characters used as a rule within its configuration?
alert tcp any any -> 192.168.100.0/24 21 (msg: "FTP on the network!";)
\nA. An Intrusion Detection System
B. A firewall IPTable
C. A Router IPTable
D. FTP Server rule''')


com = input("Answer:  ")
answer = ('''A
Explanation:
Snort is an open source network intrusion detection system (NIDS) for networks . Snort rule example:
This example is a rule with a generator id of 1000001.
alert tcp any any -> any 80 (content:"BOB"; gid:1000001; sid:1; rev:1;)
References:
http://manual-snort-org.s3-website-us-east-1.amazonaws.com/node31.html''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 493

While using your bank’s online servicing you notice the following string in the URL bar: “http://www.MyPersonalBank.com/account?id=368940911028389
&Damount=10980&Camount=21”
You observe that if you modify the Damount & Camount values and submit the request, that data on the web page reflect the changes.
Which type of vulnerability is present on this site?
\nA. Web Parameter Tampering
B. Cookie Tampering
C. XSS Reflection
D. SQL injection''')


com = input("Answer:  ")
answer = ('''A
Explanation:
The Web Parameter Tampering attack is based on the manipulation of parameters exchanged between client and server in order to modify application data, such
as user credentials and permissions, price and quantity of products, etc. Usually, this information is stored in cookies, hidden form fields, or URL Query Strings,
and is used to increase application functionality and control.
References: https://www.owasp.org/index.php/Web_Parameter_Tampering''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 494

An attacker changes the profile information of a particular user (victim) on the target website. The attacker uses this string to update the victim’s profile to a text file
and then submit the data to the attacker’s database.
<iframe src="http://www.vulnweb.com/updateif.php" style="display:none"></iframe>
What is this type of attack (that can use either HTTP GET or HTTP POST) called?
\nA. Cross-Site Request Forgery
B. Cross-Site Scripting
C. SQL Injection
D. Browser Hacking''')


com = input("Answer:  ")
answer = ('''A
Explanation:
Cross-site request forgery, also known as one-click attack or session riding and abbreviated as CSRF (sometimes pronounced sea-surf) or XSRF, is a type of
malicious exploit of a website where unauthorized commands are transmitted from a user that the website trusts.
Different HTTP request methods, such as GET and POST, have different level of susceptibility to CSRF attacks and require different levels of protection due to
their different handling by web browsers.
References: https://en.wikipedia.org/wiki/Cross-site_request_forgery''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 497

You are tasked to perform a penetration test. While you are performing information gathering, you find an employee list in Google. You find the receptionist's email,
and you send her an email changing the source email to her boss's email( boss@company ). In this email, you ask for a pdf with information. She reads your email
and sends back a pdf with links. You exchange the pdf links with your malicious links (these links contain malware) and send back the modified pdf, saying that the
links don't work. She reads your email, opens the links, and her machine gets infected. You now have access to the company network.
What testing method did you use?
\nA. Social engineering
B. Tailgating
C. Piggybacking
D. Eavesdropping''')


com = input("Answer:  ")
answer = ('''A
Explanation:
Social engineering, in the context of information security, refers to psychological manipulation of people into performing actions or divulging confidential
information. A type of confidence trick for the purpose of information gathering, fraud, or system access, it differs from a traditional "con" in that it is often one of
many steps in a more complex fraud scheme.''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 501

The network administrator contacts you and tells you that she noticed the temperature on the internal wireless router increases by more than 20% during weekend
hours when the office was closed. She asks you to investigate the issue because she is busy dealing with a big conference and she doesn’t have time to perform
the task.
What tool can you use to view the network traffic being sent and received by the wireless router?
\nA. Wireshark
B. Nessus
C. Netcat
D. Netstat''')


com = input("Answer:  ")
answer = ('''A
Explanation:
Wireshark is a Free and open source packet analyzer. It is used for network troubleshooting, analysis, software and communications protocol development, and
education.''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 502

Your company was hired by a small healthcare provider to perform a technical assessment on the network. What is the best approach for discovering
vulnerabilities on a Windows-based computer?
\nA. Use a scan tool like Nessus
B. Use the built-in Windows Update tool
C. Check MITRE.org for the latest list of CVE findings
D. Create a disk image of a clean Windows installation''')


com = input("Answer:  ")
answer = ('''A



Explanation:
Nessus is an open-source network vulnerability scanner that uses the Common Vulnerabilities and Exposures architecture for easy cross-linking between
compliant security tools.
The Nessus server is currently available for Unix, Linux and FreeBSD. The client is available for Unix- or Windows-based operating systems.
Note: Significant capabilities of Nessus include: References: http://searchnetworking.techtarget.com/definition/Nessus''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 504

You are performing a penetration test. You achieved access via a buffer overflow exploit and you proceed to find interesting data, such as files with usernames
and passwords. You find a hidden folder that has the administrator's bank account password and login information for the administrator's bitcoin account.
What should you do?
\nA. Report immediately to the administrator
B. Do not report it and continue the penetration test.
C. Transfer money from the administrator's account to another account.
D. Do not transfer the money but steal the bitcoins.''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 506

While performing online banking using a Web browser, a user receives an email that contains a link to an interesting Web site. When the user clicks on the link,
another Web browser session starts and displays a video of cats playing a piano. The next business day, the user receives what looks like an email from his bank,
indicating that his bank account has been accessed from a foreign country. The email asks the user to call his bank and verify the authorization of a funds transfer
that took place.
What Web browser-based security vulnerability was exploited to compromise the user?
\nA. Cross-Site Request Forgery
B. Cross-Site Scripting
C. Clickjacking
D. Web form input validation''')


com = input("Answer:  ")
answer = ('''A
Explanation:
Cross-site request forgery, also known as one-click attack or session riding and abbreviated as CSRF or XSRF, is a type of malicious exploit of a website where
unauthorized commands are transmitted from a user that the website trusts.
Example and characteristics
If an attacker is able to find a reproducible link that executes a specific action on the target page while the victim is being logged in there, he is able to embed such
link on a page he controls and trick the victim into opening it. The attack carrier link may be placed in a location that the victim is likely to visit while logged into the
target site (e.g. a discussion forum), sent in a HTML email body or attachment.''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 508

Which of the following areas is considered a strength of symmetric key cryptography when compared with asymmetric algorithms?
\nA. Scalability
B. Speed
C. Key distribution
D. Security''')


com = input("Answer:  ")
answer = ('''B''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 510

Which of the following is a protocol specifically designed for transporting event messages?
\nA. SYSLOG
B. SMS
C. SNMP
D. ICMP''')


com = input("Answer:  ")
answer = ('''A
Explanation:
syslog is a standard for message logging. It permits separation of the software that generates messages, the system that stores them, and the software that
reports and analyzes them. Each message is labeled with a facility code, indicating the software type generating the message, and assigned a severity label.
References: https://en.wikipedia.org/wiki/Syslog#Network_protocol''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 512

Internet Protocol Security IPSec is actually a suite of protocols. Each protocol within the suite provides different functionality. Collective IPSec does everything
except.
\nA. Protect the payload and the headers
B. Authenticate
C. Encrypt
D. Work at the Data Link Layer''')


com = input("Answer:  ")
answer = ('''D''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 517

Which of the following is designed to identify malicious attempts to penetrate systems?
\nA. Intrusion Detection System
B. Firewall
C. Proxy
D. Router''')


com = input("Answer:  ")
answer = ('''A
Explanation:
An intrusion detection system (IDS) is a device or software application that monitors network or system activities for malicious activities or policy violations and
produces electronic reports to a management station.
References: https://en.wikipedia.org/wiki/Intrusion_detection_system''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 521

What network security concept requires multiple layers of security controls to be placed throughout an IT infrastructure, which improves the security posture of an
organization to defend against malicious attacks or potential vulnerabilities?
\nA. Security through obscurity
B. Host-Based Intrusion Detection System
C. Defense in depth
D. Network-Based Intrusion Detection System''')


com = input("Answer:  ")
answer = ('''C''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 525

The company ABC recently discovered that their new product was released by the opposition before their premiere. They contract an investigator who discovered
that the maid threw away papers with confidential information about the new product and the opposition found it in the garbage. What is the name of the technique
used by the opposition?
\nA. Hack attack
B. Sniffing
C. Dumpster diving
D. Spying''')


com = input("Answer:  ")
answer = ('''C''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 529

Craig received a report of all the computers on the network that showed all the missing patches and weak passwords. What type of software generated this report?
\nA. a port scanner
B. a vulnerability scanner
C. a virus scanner
D. a malware scanner''')


com = input("Answer:  ")
answer = ('''B''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 530

PGP, SSL, and IKE are all examples of which type of cryptography?
\nA. Public Key
B. Secret Key
C. Hash Algorithm
D. Digest''')


com = input("Answer:  ")
answer = ('''A
Explanation:
Public-key algorithms are fundamental security ingredients in cryptosystems, applications and protocols. They underpin various Internet standards, such as Secure
Sockets Layer (SSL),Transport Layer Security (TLS), S/MIME, PGP, Internet Key Exchange (IKE or IKEv2), and GPG.
References: https://en.wikipedia.org/wiki/Public-key_cryptography''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 534

In Risk Management, how is the term "likelihood" related to the concept of "threat?"
\nA. Likelihood is the probability that a threat-source will exploit a vulnerability.
B. Likelihood is a possible threat-source that may exploit a vulnerability.



C. Likelihood is the likely source of a threat that could exploit a vulnerability.
D. Likelihood is the probability that a vulnerability is a threat-source.''')


com = input("Answer:  ")
answer = ('''A
Explanation:
The ability to analyze the likelihood of threats within the organization is a critical step in building an effective security program. The process of assessing threat
probability should be well defined and incorporated into a broader threat analysis process to be effective.
References:
http://www.mcafee.com/campaign/securitybattleground/resources/chapter5/whitepaper-on-assessing-threat-attac''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 537

In both pharming and phishing attacks an attacker can create websites that look similar to legitimate sites with the intent of collecting personal identifiable
information from its victims. What is the difference between pharming and phishing attacks?
\nA. In a pharming attack a victim is redirected to a fake website by modifying their host configuration file or by exploiting vulnerabilities in DN
B. In a phishing attack an attacker provides the victim with a URL that is either misspelled or looks similar to the actual websites domain name.
C. Both pharming and phishing attacks are purely technical and are not considered forms of social engineering.
D. Both pharming and phishing attacks are identical.
E. In a phishing attack a victim is redirected to a fake website by modifying their host configuration file or by exploiting vulnerabilities in DN
F. In a pharming attack an attacker provides the victim with a URL that is either misspelled or looks very similar to the actual websites domain name.''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 538

Which protocol is used for setting up secured channels between two devices, typically in VPNs?
\nA. IPSEC
B. PEM
C. SET
D. PPP''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 539

You are an Ethical Hacker who is auditing the ABC company. When you verify the NOC one of the machines has 2 connections, one wired and the other wireless.
When you verify the configuration of this Windows system you find two static routes.
route add 10.0.0.0 mask 255.0.0.0 10.0.0.1
route add 0.0.0.0 mask 255.0.0.0 199.168.0.1 What is the main purpose of those static routes?
\nA. Both static routes indicate that the traffic is external with different gateway.
B. The first static route indicates that the internal traffic will use an external gateway and the second static route indicates that the traffic will be rerouted.
C. Both static routes indicate that the traffic is internal with different gateway.
D. The first static route indicates that the internal addresses are using the internal gateway and the second static route indicates that all the traffic that is not
internal must go to an external gateway.''')


com = input("Answer:  ")
answer = ('''D''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 544

Due to a slowdown of normal network operations, IT department decided to monitor internet traffic for all of the employees. From a legal stand point, what would
be troublesome to take this kind of measure?
\nA. All of the employees would stop normal work activities
B. IT department would be telling employees who the boss is
C. Not informing the employees that they are going to be monitored could be an invasion of privacy.
D. The network could still experience traffic slow down.''')


com = input("Answer:  ")
answer = ('''C''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 546

A large mobile telephony and data network operator has a data that houses network elements. These are essentially large computers running on Linux. The
perimeter of the data center is secured with firewalls and IPS systems. What is the best security policy concerning this setup?
\nA. Network elements must be hardened with user ids and strong password
B. Regular security tests and audits should be performed.
C. As long as the physical access to the network elements is restricted, there is no need for additional measures.
D. There is no need for specific security measures on the network elements as long as firewalls and IPS systems exist.
E. The operator knows that attacks and down time are inevitable and should have a backup site.''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 551




Which of the following tools is used to detect wireless LANs using the 802.11a/b/g/n WLAN standards on a linux platform?
\nA. Kismet
B. Nessus
C. Netstumbler
D. Abel''')


com = input("Answer:  ")
answer = ('''A
Explanation:
Kismet is a network detector, packet sniffer, and intrusion detection system for 802.11 wireless LANs. Kismet will work with any wireless card which supports raw
monitoring mode, and can sniff 802.11a, 802.11b, 802.11g, and 802.11n traffic. The program runs under Linux, FreeBSD, NetBSD, OpenBSD, and Mac OS X.
References: https://en.wikipedia.org/wiki/Kismet_(software)''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 554

Which method of password cracking takes the most time and effort?
\nA. Brute force
B. Rainbow tables
C. Dictionary attack
D. Shoulder surfing''')


com = input("Answer:  ")
answer = ('''A
Explanation:
Brute-force cracking, in which a computer tries every possible key or password until it succeeds, is typically very time consuming. More common methods of
password cracking, such as dictionary attacks, pattern checking, word list substitution, etc. attempt to reduce the number of trials required and will usually be
attempted before brute force.
References: https://en.wikipedia.org/wiki/Password_cracking''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 558

You are the Systems Administrator for a large corporate organization. You need to monitor all network traffic on your local network for suspicious activities and
receive notifications when an attack is occurring. Which tool would allow you to accomplish this goal?
\nA. Network-based IDS
B. Firewall
C. Proxy
D. Host-based IDS''')


com = input("Answer:  ")
answer = ('''A
Explanation:
A network-based intrusion detection system (NIDS) is used to monitor and analyze network traffic to protect a system from network-based threats.
A NIDS reads all inbound packets and searches for any suspicious patterns. When threats are discovered, based on its severity, the system can take action such
as notifying administrators, or barring the source IP address from accessing the network.
References: https://www.techopedia.com/definition/12941/network-based-intrusion-detection-system-nids''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 559

Which of the following security operations is used for determining the attack surface of an organization?
\nA. Running a network scan to detect network services in the corporate DMZ
B. Training employees on the security policy regarding social engineering
C. Reviewing the need for a security clearance for each employee
D. Using configuration management to determine when and where to apply security patches''')


com = input("Answer:  ")
answer = ('''A
Explanation:
For a network scan the goal is to document the exposed attack surface along with any easily detected vulnerabilities.
References:
http://meisecurity.com/home/consulting/consulting-network-scanning/''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 564

Which of the following tools is used to analyze the files produced by several packet-capture programs such as tcpdump, WinDump, Wireshark, and EtherPeek?
\nA. tcptrace
B. tcptraceroute
C. Nessus
D. OpenVAS''')


com = input("Answer:  ")
answer = ('''A
Explanation:



tcptrace is a tool for analysis of TCP dump files. It can take as input the files produced by several popular packet-capture programs, including
tcpdump/WinDump/Wireshark, snoop, EtherPeek, and Agilent NetMetrix.
References: https://en.wikipedia.org/wiki/Tcptrace''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 565

What is the correct process for the TCP three-way handshake connection establishment and connection termination?
\nA. Connection Establishment: FIN, ACK-FIN, ACKConnection Termination: SYN, SYN-ACK, ACK
B. Connection Establishment: SYN, SYN-ACK, ACKConnection Termination: ACK, ACK-SYN, SYN
C. Connection Establishment: ACK, ACK-SYN, SYNConnection Termination: FIN, ACK-FIN, ACK
D. Connection Establishment: SYN, SYN-ACK, ACKConnection Termination: FIN, ACK-FIN, ACK''')


com = input("Answer:  ")
answer = ('''D''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 570

You want to do an ICMP scan on a remote computer using hping2. What is the proper syntax?
\nA. hping2 host.domain.com
B. hping2 --set-ICMP host.domain.com
C. hping2 -i host.domain.com
D. hping2 -1 host.domain.com''')


com = input("Answer:  ")
answer = ('''D''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 573

Sophia travels a lot and worries that her laptop containing confidential documents might be stolen. What is the best protection that will work for her?
\nA. Password protected files
B. Hidden folders
C. BIOS password
D. Full disk encryption.''')


com = input("Answer:  ")
answer = ('''D''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 574

What does a firewall check to prevent particular ports and applications from getting packets into an organization?
\nA. Transport layer port numbers and application layer headers
B. Presentation layer headers and the session layer port numbers
C. Network layer headers and the session layer port numbers
D. Application layer port numbers and the transport layer headers''')


com = input("Answer:  ")
answer = ('''A
Explanation:
Newer firewalls can filter traffic based on many packet attributes like source IP address, source port, destination IP address or transport layer port, destination
service like WWW or FTP. They can filter based on protocols, TTL values, netblock of originator, of the source, and many other attributes.
Application layer firewalls are responsible for filtering at 3, 4, 5, 7 layer. Because they analyze the application layer headers, most firewall control and filtering is
performed actually in the software.
References: https://en.wikipedia.org/wiki/Firewall_(computing)#Network_layer_or_packet_filters
http://howdoesinternetwork.com/2012/application-layer-firewalls''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 578

Which tier in the N-tier application architecture is responsible for moving and processing data between the tiers?
\nA. Application Layer
B. Data tier
C. Presentation tier
D. Logic tier''')


com = input("Answer:  ")
answer = ('''D''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 583

Bob learned that his username and password for a popular game has been compromised. He contacts the company and resets all the information. The company
suggests he use two-factor authentication, which option below offers that?
\nA. A new username and password
B. A fingerprint scanner and his username and password.
C. Disable his username and use just a fingerprint scanner.
D. His username and a stronger password.''')


com = input("Answer:  ")
answer = ('''B''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 584

Which Intrusion Detection System is best applicable for large environments where critical assets on the network need extra security and is ideal for observing
sensitive network segments?
\nA. Network-based intrusion detection system (NIDS)
B. Host-based intrusion detection system (HIDS)
C. Firewalls
D. Honeypots''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 585

Attempting an injection attack on a web server based on responses to True/False questions is called which of the following?
\nA. Blind SQLi
B. DMS-specific SQLi
C. Classic SQLi
D. Compound SQLi''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 590

A company's security policy states that all Web browsers must automatically delete their HTTP browser cookies upon terminating. What sort of security breach is
this policy attempting to mitigate?
\nA. Attempts by attackers to access Web sites that trust the Web browser user by stealing the user's authentication credentials.
B. Attempts by attackers to access the user and password information stored in the company's SQL database.
C. Attempts by attackers to access passwords stored on the user's computer without the user's knowledge.
D. Attempts by attackers to determine the user's Web browser usage patterns, including when sites were visited and for how long.''')


com = input("Answer:  ")
answer = ('''A
Explanation:
Cookies can store passwords and form content a user has previously entered, such as a credit card number or an address.
Cookies can be stolen using a technique called cross-site scripting. This occurs when an attacker takes advantage of a website that allows its users to post
unfiltered HTML and JavaScript content.
References: https://en.wikipedia.org/wiki/HTTP_cookie#Cross-site_scripting_.E2.80.93_cookie_theft''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 592

What is correct about digital signatures?
\nA. A digital signature cannot be moved from one signed document to another because it is the hash of the original document encrypted with the private key of the
signing party.
B. Digital signatures may be used in different documents of the same type.
C. A digital signature cannot be moved from one signed document to another because it is a plain hash of the document content.
D. Digital signatures are issued once for each user and can be used everywhere until they expire.''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 596

What term describes the amount of risk that remains after the vulnerabilities are classified and the countermeasures have been deployed?
\nA. Residual risk
B. Inherent risk
C. Deferred risk
D. Impact risk''')


com = input("Answer:  ")
answer = ('''A
Explanation:
The residual risk is the risk or danger of an action or an event, a method or a (technical) process that, although being abreast with science, still conceives these
dangers, even if all theoretically possible safety measures would be applied (scientifically conceivable measures); in other words, the amount of risk left over after
natural or inherent risks have been reduced by risk controls.
References: https://en.wikipedia.org/wiki/Residual_risk''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 597

What is the role of test automation in security testing?



\nA. It can accelerate benchmark tests and repeat them with a consistent test setu
B. But it cannot replace manual testing completely.
C. It is an option but it tends to be very expensive.
D. It should be used exclusivel
E. Manual testing is outdated because of low speed and possible test setup inconsistencies.
F. Test automation is not usable in security due to the complexity of the tests.''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 600

Which of the following is a low-tech way of gaining unauthorized access to systems?
\nA. Social Engineering
B. Sniffing
C. Eavesdropping
D. Scanning''')


com = input("Answer:  ")
answer = ('''A
Explanation:
Social engineering, in the context of information security, refers to psychological manipulation of people into performing actions or divulging confidential
information. A type of confidence trick for the purpose of information gathering, fraud, or system access.
References: https://en.wikipedia.org/wiki/Social_engineering_(security)''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 602

In many states sending spam is illegal. Thus, the spammers have techniques to try and ensure that no one knows they sent the spam out to thousands of users at
a time. Which of the following best describes what spammers use to hide the origin of these types of e-mails?
\nA. A blacklist of companies that have their mail server relays configured to allow traffic only to theirspecific domain name.
B. Mail relaying, which is a technique of bouncing e-mail from internal to external mails servers continuously.
C. A blacklist of companies that have their mail server relays configured to be wide open.
D. Tools that will reconfigure a mail server's relay component to send the e-mail back to the spammers occasionally.''')


com = input("Answer:  ")
answer = ('''B''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 607

Which of the following tools performs comprehensive tests against web servers, including dangerous files and CGIs?
\nA. Nikto
B. Snort
C. John the Ripper
D. Dsniff''')


com = input("Answer:  ")
answer = ('''A
Explanation:
Nikto is an Open Source (GPL) web server scanner which performs comprehensive tests against web servers for multiple items, including over 6700 potentially
dangerous files/CGIs, checks for outdated versions of over 1250 servers, and version specific problems on over 270 servers. It also checks for server configuration
items such as the presence of multiple index files, HTTP server options, and will attempt to identify installed web servers and software. Scan items and plugins are
frequently updated and can be automatically updated.
References: https://en.wikipedia.org/wiki/Nikto_Web_Scanner''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 610

An Internet Service Provider (ISP) has a need to authenticate users connecting using analog modems, Digital Subscriber Lines (DSL), wireless data services, and
Virtual Private Networks (VPN) over a Frame Relay network.
Which AAA protocol is most likely able to handle this requirement?
\nA. RADIUS
B. DIAMETER
C. Kerberos
D. TACACS+''')


com = input("Answer:  ")
answer = ('''A
Explanation:
Because of the broad support and the ubiquitous nature of the RADIUS protocol, it is often used by ISPs and enterprises to manage access to the Internet or
internal networks, wireless networks, and integrated e-mail services. These networks may incorporate modems, DSL, access points, VPNs, network ports, web
servers, etc.
References: https://en.wikipedia.org/wiki/RADIUS''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 614

A well-intentioned researcher discovers a vulnerability on the web site of a major corporation. What should he do?



\nA. Ignore it.
B. Try to sell the information to a well-paying party on the dark web.
C. Notify the web site owner so that corrective action be taken as soon as possible to patch the vulnerability.
D. Exploit the vulnerability without harming the web site owner so that attention be drawn to the problem.''')


com = input("Answer:  ")
answer = ('''C''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 619

Jimmy is standing outside a secure entrance to a facility. He is pretending to have a tense conversation on his cell phone as an authorized employee badges in.
Jimmy, while still on the phone, grabs the door as it begins to close.
What just happened?
\nA. Phishing
B. Whaling
C. Tailgating
D. Masquerading''')


com = input("Answer:  ")
answer = ('''C''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 623

Which of these is capable of searching for and locating rogue access points?
\nA. HIDS
B. WISS
C. WIPS
D. NIDS''')


com = input("Answer:  ")
answer = ('''C''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 624

The security concept of "separation of duties" is most similar to the operation of which type of security device?
\nA. Firewall
B. Bastion host
C. Intrusion Detection System
D. Honeypot''')


com = input("Answer:  ")
answer = ('''A
Explanation:
In most enterprises the engineer making a firewall change is also the one reviewing the firewall metrics for unauthorized changes. What if the firewall administrator
wanted to hide something? How would anyone ever find out? This is where the separation of duties comes in to focus on the responsibilities of tasks within
security.
References:
http://searchsecurity.techtarget.com/tip/Modern-security-management-strategy-requires-security-separation-of-d''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 627

An Intrusion Detection System (IDS) has alerted the network administrator to a possibly malicious sequence of packets sent to a Web server in the network's
external DMZ. The packet traffic was captured by the IDS and saved to a PCAP file.
What type of network tool can be used to determine if these packets are genuinely malicious or simply a false positive?
\nA. Protocol analyzer
B. Intrusion Prevention System (IPS)
C. Network sniffer
D. Vulnerability scanner''')


com = input("Answer:  ")
answer = ('''A
Explanation:
A packet analyzer (also known as a network analyzer, protocol analyzer or packet sniffer—or, for particular types of networks, an Ethernet sniffer or wireless sniffer)
is a computer program or piece of computer hardware that can intercept and log traffic that passes over a digital network or part of a network. A packet analyzer
can analyze packet traffic saved in a PCAP file.
References: https://en.wikipedia.org/wiki/Packet_analyzer''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 631

To determine if a software program properly handles a wide range of invalid input, a form of automated testing can be used to randomly generate invalid input in
an attempt to crash the program.
What term is commonly used when referring to this type of testing?
\nA. Fuzzing
B. Randomizing
C. Mutating
D. Bounding''')


com = input("Answer:  ")
answer = ('''A
Explanation:
Fuzz testing or fuzzing is a software testing technique, often automated or semi-automated, that involves providing invalid, unexpected, or random data to the
inputs of a computer program. The program is then monitored for exceptions such as crashes, or failing built-in code assertions or for finding potential memory
leaks. Fuzzing is commonly used to test for security problems in software or computer systems. It is a form of random testing which has been used for testing
hardware or software.
References: https://en.wikipedia.org/wiki/Fuzz_testing''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 636

A hacker has managed to gain access to a Linux host and stolen the password file from /etc/passwd. How can he use it?
\nA. The password file does not contain the passwords themselves.
B. He can open it and read the user ids and corresponding passwords.
C. The file reveals the passwords to the root user only.
D. He cannot read it because it is encrypted.''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 637

While performing online banking using a Web browser, Kyle receives an email that contains an image of a well-crafted art. Upon clicking the image, a new tab on
the web browser opens and shows an animated GIF of bills and coins being swallowed by a crocodile. After several days, Kyle noticed that all his funds on the
bank was gone. What Web browser-based security vulnerability got exploited by the hacker?
\nA. Clickjacking
B. Web Form Input Validation
C. Cross-Site Request Forgery
D. Cross-Site Scripting''')


com = input("Answer:  ")
answer = ('''C''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 639

Matthew received an email with an attachment named “YouWon$10Grand.zip.” The zip file contains a file named “HowToClaimYourPrize.docx.exe.” Out of
excitement and curiosity, Matthew opened the said file. Without his knowledge, the file copies itself to Matthew’s APPDATA\IocaI directory and begins to beacon
to a Command-and-control server to download additional malicious binaries. What type of malware has Matthew encountered?
\nA. Key-logger
B. Trojan
C. Worm
D. Macro Virus''')


com = input("Answer:  ")
answer = ('''B''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 640

Shellshock had the potential for an unauthorized user to gain access to a server. It affected many internet-facing services, which OS did it not directly affect?
\nA. Windows
B. Unix
C. Linux
D. OS X''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 643

Which Type of scan sends a packets with no flags set?
\nA. Open Scan
B. Null Scan
C. Xmas Scan
D. Half-Open Scan''')


com = input("Answer:  ")
answer = ('''B''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 644

Which of the following is a wireless network detector that is commonly found on Linux?
\nA. Kismet
B. Abel
C. Netstumbler
D. Nessus''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 645

A server has been infected by a certain type of Trojan. The hacker intended to utilize it to send and host junk mails. What type of Trojan did the hacker use?
\nA. Turtle Trojans
B. Ransomware Trojans
C. Botnet Trojan
D. Banking Trojans''')


com = input("Answer:  ")
answer = ('''C''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 648

As an Ethical Hacker you are capturing traffic from your customer network with Wireshark and you need to find and verify just SMTP traffic. What command in
Wireshark will help you to find this kind of traffic?
\nA. request smtp 25
B. tcp.port eq 25
C. smtp port
D. tcp.contains port 25''')


com = input("Answer:  ")
answer = ('''B''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 649

What is the term coined for logging, recording and resolving events in a company?
\nA. Internal Procedure
B. Security Policy
C. Incident Management Process
D. Metrics''')


com = input("Answer:  ")
answer = ('''C''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 651

You are manually conducting Idle Scanning using Hping2. During your scanning you notice that almost every query increments the IPID regardless of the port
being queried. One or two of the queries cause the IPID to increment by more than one value. Why do you think this occurs?
\nA. The zombie you are using is not truly idle.
B. A stateful inspection firewall is resetting your queries.
C. Hping2 cannot be used for idle scanning.
D. These ports are actually open on the target system.''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 654

You’ve just gained root access to a Centos 6 server after days of trying. What tool should you use to maintain access?
\nA. Disable Key Services
B. Create User Account
C. Download and Install Netcat
D. Disable IPTables''')


com = input("Answer:  ")
answer = ('''B''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 655

A hacker was able to easily gain access to a website. He was able to log in via the frontend user login form of the website using default or commonly used
credentials. This exploitation is an example of what Software design flaw?
\nA. Insufficient security management
B. Insufficient database hardening
C. Insufficient input validation
D. Insufficient exception handling''')


com = input("Answer:  ")
answer = ('''B''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 657

........is an attack type for a rogue Wi-Fi access point that appears to be a legitimate one offered on the premises, but actually has been set up to eavesdrop on
wireless communications. It is the wireless version of the phishing scam. An attacker fools wireless users into connecting a laptop or mobile phone to a tainted



hotspot by posing as a legitimate provider. This type of attack may be used to steal the passwords of unsuspecting users by either snooping the communication
link or by phishing, which involves setting up a fraudulent web site and luring people there.
Fill in the blank with appropriate choice.
\nA. Collision Attack
B. Evil Twin Attack
C. Sinkhole Attack
D. Signal Jamming Attack''')


com = input("Answer:  ")
answer = ('''B''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 662

Which of the following commands runs snort in packet logger mode?
\nA. ./snort -dev -h ./log
B. ./snort -dev -l ./log
C. ./snort -dev -o ./log
D. ./snort -dev -p ./log''')


com = input("Answer:  ")
answer = ('''B''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 663

SNMP is a protocol used to query hosts, servers, and devices about performance or health status dat\nA. This protocol has long been used by hackers to gather
great amount of information about remote hosts. Which of the following features makes this possible? (Choose two.)
\nA. It used TCP as the underlying protocol.
B. It uses community string that is transmitted in clear text.
C. It is susceptible to sniffing.
D. It is used by all network devices on the market.''')


com = input("Answer:  ")
answer = ('''BD''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 664

An enterprise recently moved to a new office and the new neighborhood is a little risky. The CEO wants to monitor the physical perimeter and the entrance doors
24 hours. What is the best option to do this job?
\nA. Use fences in the entrance doors.
B. Install a CCTV with cameras pointing to the entrance doors and the street.
C. Use an IDS in the entrance doors and install some of them near the corners.
D. Use lights in all the entrance doors and along the company's perimeter.''')


com = input("Answer:  ")
answer = ('''B''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 668

In which phase of the ethical hacking process can Google hacking be employed? This is a technique that involves manipulating a search string with specific
operators to search for vulnerabilities.
Example:
allintitle: root passwd
\nA. Maintaining Access
B. Gaining Access
C. Reconnaissance
D. Scanning and Enumeration''')


com = input("Answer:  ")
answer = ('''C''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 671

The practical realities facing organizations today make risk response strategies essential. Which of the following is NOT one of the five basic responses to risk?
\nA. Accept
B. Mitigate
C. Delegate
D. Avoid''')


com = input("Answer:  ")
answer = ('''C''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 675

While performing ping scans into a target network you get a frantic call from the organization's security team. They report that they are under a denial of service
attack. When you stop your scan, the smurf attack event stops showing up on the organization's IDS monitor.
How can you modify your scan to prevent triggering this event in the IDS?



\nA. Scan more slowly.
B. Do not scan the broadcast IP.
C. Spoof the source IP address.
D. Only scan the Windows systems.''')


com = input("Answer:  ")
answer = ('''B''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 676

Which of the following will perform an Xmas scan using NMAP?
\nA. nmap -sA 192.168.1.254
B. nmap -sP 192.168.1.254
C. nmap -sX 192.168.1.254
D. nmap -sV 192.168.1.254''')


com = input("Answer:  ")
answer = ('''C''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 679

While doing a technical assessment to determine network vulnerabilities, you used the TCP XMAS scan. What would be the response of all open ports?
\nA. The port will send an ACK
B. The port will send a SYN
C. The port will ignore the packets
D. The port will send an RST''')


com = input("Answer:  ")
answer = ('''C''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 684

You want to analyze packets on your wireless network. Which program would you use?
\nA. Wireshark with Airpcap
B. Airsnort with Airpcap
C. Wireshark with Winpcap
D. Ethereal with Winpcap''')


com = input("Answer:  ")
answer = ('''A''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 689

Sandra has been actively scanning the client network on which she is doing a vulnerability assessment test. While conducting a port scan she notices open ports
in the range of 135 to 139.
What protocol is most likely to be listening on those ports?
\nA. Finger
B. FTP
C. Samba
D. SMB''')


com = input("Answer:  ")
answer = ('''D''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 694

Which of the following security policies defines the use of VPN for gaining access to an internal corporate network?
\nA. Network security policy
B. Remote access policy
C. Information protection policy
D. Access control policy''')


com = input("Answer:  ")
answer = ('''B''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 699

Which of the following is a restriction being enforced in “white box testing?”
\nA. Only the internal operation of a system is known to the tester
B. The internal operation of a system is completely known to the tester
C. The internal operation of a system is only partly accessible to the tester
D. Only the external operation of a system is accessible to the tester''')


com = input("Answer:  ")
answer = ('''B''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 701




In order to prevent particular ports and applications from getting packets into an organization, what does a firewall check?
\nA. Network layer headers and the session layer port numbers
B. Presentation layer headers and the session layer port numbers
C. Application layer port numbers and the transport layer headers
D. Transport layer port numbers and application layer headers''')


com = input("Answer:  ")
answer = ('''D''')
if com.lower() == answer.lower():
    print("Correct!")
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 704

A company recently hired your team of Ethical Hackers to test the security of their network systems. The company wants to have the attack be as realistic as
possible. They did not provide any information besides the name of their company. What phase of security testing would your team jump in right away?
\nA. Scanning
B. Reconnaissance
C. Escalation
D. Enumeration''')


com = input("Answer:  ")
answer = ('''B''')
if com.lower() == answer.lower():
    print("Correct!")    
    correct += 1
    sleep(1)
else:
    print('Wrong!')
    sleep(1)

os.system('cls')
print(f'''\n\nCorrect: {correct}\t\tQUESTION: 708''')
sleep(1)