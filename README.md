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


-- Project_Sentinel.ipynb --

Project Sentinel is an end-to-end natural language processing and machine learning pipeline built to analyze and classify social media discourse surrounding the 2020 U.S. presidential election. The system preprocesses raw tweet text through tokenization, lemmatization, and TF-IDF vectorization, while integrating geospatial mapping to visualize political engagement and extremist rhetoric. It evaluates a comprehensive range of classifiers, comparing traditional algorithms like Naive Bayes, XGBoost, and Linear SVC against an advanced Bidirectional LSTM deep learning model.

The project addresses the challenge of large-scale content moderation and the spread of radicalization during high-stakes political events. By benchmarking multiple modeling approaches, it identifies the most effective architectures for detecting subtle toxic language online and offers actionable data insights into how extremist discourse is geographically distributed.


-- Project_Janus.ipynb --

Project Janus is an advanced computer vision and facial recognition pipeline designed to detect, classify, and verify facial images across various visual conditions. The system integrates multiple machine learning architectures, including custom Convolutional Neural Networks (CNNs), YOLOv8 for efficient face detection, and InsightFace's ArcFace implementation to generate high-precision facial embeddings and calculate cosine similarity matching between subjects.

The project addresses the technical challenges of reliable biometric identification and automated visual classification in unstructured environments. By benchmarking traditional CNN models against state-of-the-art YOLOv8 and metric-learning embedding frameworks, it evaluates which deep learning techniques are most effective for accurate face recognition and identity verification.


-- Project_Skywatch.ipynb --

Operation Skywatch is a computer vision pipeline designed to classify and identify different models of Russian fighter jets from visual and aerial imagery. The system implements data preprocessing pipelines and aggressive data augmentation to handle varying angles, utilizing a MobileNetV2 transfer learning architecture alongside a YOLOv8 classification model for high-speed inference. It incorporates comprehensive evaluation tools, including confusion matrices and classification reports, to assess model performance across multiple deep learning frameworks.

The project solves the challenge of automated aerial reconnaissance and aircraft identification in aerospace monitoring applications. By benchmarking lightweight convolutional neural networks and state-of-the-art YOLOv8 models, it provides a reliable, high-speed solution for classifying military assets accurately from unstructured image data.
