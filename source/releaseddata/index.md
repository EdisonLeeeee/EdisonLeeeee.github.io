---
title: Released Data
date: 2021-06-11 16:12:00
---

These datasets are part of Liang Chen's Ph.D. research work. The main goal of these datasets are to off real-world data for future research. Our datasets are freely available for research purpose. Redistribution of this dataset to any other third party or in the Web is not permitted.


### Dataset 1: 15,361 real-world Web services dataset. [Download]

We crawl 15,361 real-world Web services from the Internet. For each service, we crawl the corresponding WSDL document and some other information. Each line in the .csv file is a Web service information record, where the following table provides the information form.

ID	Name	Provider	Country	WSDL Address	Availability	Wiki Description	Tags
It should be noted that there are 1,814 Web services with user-annotated tags, and the whole .zip file is 34MB. If you use this dataset, please use the following reference in citing the dataset:

"WTCluster: Utilizing Tags for Web Services Clustering", Liang Chen, Liukai Hu, Zibin Zheng, Jian Wu, Jianwei Yin, Ying Li, and Shuiguang Deng. 9th International Conference on Service Oriented Computing [ICSOC], Paphos, Cyprus, December 5-8, 2011, pp.204-218.

"Titan: A System for Effective Web Service Discovery", Jian Wu, Liang Chen, Yanan Xie, and Zibin Zheng. 21th International World Wide Web Conference [WWW], Demo Track, Lyon, France, April 16-20, 2012, pp.441-444.



### Dataset 2: 185 real-world Web services dataset. [Download]

We extract 185 Web services from dataset1 for the service clustering evaluation. Specifically, there are 28 Web services in "Weather" category, 21 Web services in "Stock" category, 37 Web services in "SMS" category, 21 Web services in "Finance" category, 31 Web services in "Tourism" category, 27 Web services in "University" category, and 20 "noise" Web services. The .zip file includes 185 .xml files (WSDL documents), tag.txt (service name and the corresponding tags), groundtruth.txt (groundtruth for evaluation). For each service, there are two corresponding lines in the tag.txt. For example, the first two lines in the tag.txt includes the information in service 1 (i.e., 1.xml), and the third and forth line includes the information in service 2 (i.e., 2.xml). As for the lines in tag.txt, taking the first two lines as a example:

us weather
tags:report,company,free,zip code,weather,usa

Where "us weather" is the word segmentation result of the service name of 1.xml, and the second line includes the corresponding tags.If you use this dataset, please use the following reference in citing the dataset:

"WT-LDA: User Tagging Augmented LDA for Web Service Clustering", Liang Chen, Yilun Wang, Qi Yu, Zibin Zheng, and Jian Wu. 11st International Conference on Service Oriented Computing [ICSOC], Berlin, Germany, Dec 2 - 5, 2013. pp.162-176.


### Dataset 3: 1,283 real-world Web services datasets. [Download]

We select 1283 Web services from Dataset 1 for the service co-clustering. Specifically, we divide these Web services into 3 datasets, D1, D2 and D3. In D1 there are 30 Web services in “Business” category, 20 Web services in “Weather” category, 10 Web services in “Bioinformatics” category, 10 Web services in “Music” category, 20 Web services in “Translation” category, and 24 Web services in “HR” category. In D2, there are 23 Web services in “Academic” category, 10 Web services in “Genetics” category, 30 Web services in “HR” category, 31 web services in “Tourism” category, and 26 Web services in “University” category. D1 file includes 114 .xml files (WSDL documents). D2 file includes 120 .xml files and 120 .txt files (the corresponding tags). D3 file includes 1049 .xml files and a tag.xls file. For each Web service, the first column in tag.xls is the service name, the second column is the unique id and the forth column is the tags. If you use this dataset, please use the following reference in citing the dataset:

"Co-clustering WSDL Documents to Bootstrap Service Discovery", Tingting Liang, Liang Chen, Haochao Ying, Jian Wu. The 7th International Conference on Service Oriented Computing and Applications [SOCA], Matsue, Japan, Nov. 17-19, 2014, pp. 215-222.
