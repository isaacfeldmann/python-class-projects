This repository contains several Python projects completed for coursework. Each project demonstrates concepts ranging from web scraping to basic network scanning. Brief descriptions and highlighted skills are included below


-- course_catalog.py --

This project is a web scraper designed to interact with the Mercyhurst University course catalog. The program retrieves all academic departments from the catalog webpage, prompts the user to select a department, then displays all associated programs. After the user selects a program, the script outputs the program’s dedicated webpage and lists all related courses.

This project highlights practical experience with web scraping, including fetching URLs, parsing HTML tags, and navigating page structure to extract targeted information. It also demonstrates the ability to analyze webpage layout and identify where relevant content is located within the DOM.


-- IP_scanning.py --

This program functions similarly to the ping command by using the Scapy library to create and send ICMP echo requests. The script allows users to define an IPv4 prefix (first three octets) and automatically scans all possible hosts in the chosen range. For each address, it sends an ICMP packet, waits for a response, and reports whether the host is reachable. The script can be customized for different networks and extended with threading or additional scanning features.

This project shows the ability to build common networking utilities from scratch using packet-crafting libraries. It demonstrates understanding of ICMP behavior, basic network enumeration techniques, and how such tools can be adapted for automation, diagnostics, or security testing workflows.


-- student_form_database.py --

This program focuses on the creation of a simple graphical interface for entering student information. Through the use of the Tkinter library, the program creates a basic GUI form. The script takes the information entered by the user and writes it into an SQL database file through integrated SQL queries using the SQLite3 library. The program also allows the user to browse the entered data with a "view records" option within the interface.

The project showcases the ability to create a basic graphical interface that could be customized for a variety of use cases. It also demonstrates an understanding of SQL databases and how to integrate SQL queries directly into Python scripts.
