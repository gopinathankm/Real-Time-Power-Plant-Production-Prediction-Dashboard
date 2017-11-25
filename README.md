# Real-Time-Power-Plant-Production-Prediction-Dashboard
Real time predicting power plant production and dashboard
File: README.md                                                                             
1. Objective: Predict real time power product and monitoringoptimized accuracy.

2. Requirments:
Ubuntu 16.04 LTS
Java 8
Apache Zookeeper
Apache Kafka
Kafka-python
Python 3.6.3, Anaconda 5.0.1
Flask
Flask_SocketIO
Matplotlib
Numpy
Pandas
scikit-learn
scipy
sklearn-pandas
sklearn-pmml
sklearn2pmml
xlrd

3. Steps & Usage:
A. Start Apache Zookeeper
B. Start Apache Kafka
C. Create a topic
D. A Logistic Regression  Prediction model(For that matter any algorithms of any sort) is created off-line for power plant production predicti$
   historical live data, optimized accuracy using Scikit-Learn.
E. Serialized model and converted to PMML format for on-line prediction using JPMML.
F. Sensor data generated real time power plant for features.
G. Pumped into Kafka topics.
H. Real time Kafka consumer, (Which is actually a Openscoring python client and Python_SocketIO client) consumes data.
I. Predict on-line using Openscoring server using consumed data.
J. Dynamically update flask web page dashboard with on-line features and predicted data for that features on line.



