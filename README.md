This README contains an explanation of each project uploaded to this repository

-- course_catelog.py --
This project is a simple web scraper. The program takes the Mercyhurst University course catalog URL and fetches the name of each department. It then prompts the user to enter a department name. After entering the department name, all program names within that department are displayed, and the user is again prompted to choose one. After selecting one, the code outputs a link to the page about that particular program and all the classes that are associated with that program.

The program effectively shows how to use specific imports for opening a URL and fetching different tags in HTML. It also showcases my ability to analyze HTML and identify the location of specific content on a web page.

-- IP_scanning.py --
This project functions like a ping command in a terminal using the scapy library to build packets. The way this one is configured, it is set to scan a range of IPv4 addresses based on an IP "prefix". The prefix in this setup is the first three octets of the IP, and then scans all IPs based on the last address. The first part of the program builds the ping function. It first creates an ICMP echo request packet. The next part of the function sets up the output based on whether there is a response or not. If there is no response because the device is offline or the ping has been blocked by a firewall, the program prints "{ip} is not reachable". If there is a response, the program prints "{ip} is reachable". The second part of this program is the main function that can be configured to best fit the user's use case. The function begins by defining the IP prefix for a particular network. Then, using a for loop, the function finds each last octet of the IP prefix, setting that value as the target IP. Using the ping function created in the program and the target IP, the program sends packets to that IP and waits for a response. After receiving a response, the for loop continues to the next IP until it has sent a ping to all IPs within the defined range.

The program showcases the ability to make common network tools from scratch. This sort of tool can also be configured for various uses, such as pentesting, when combined with other tools.

