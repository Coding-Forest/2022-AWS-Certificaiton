# Database  

[1. RDBMS](#1)  
[2. RDS](#2)  
[3. RDS characteristics](#3)  

<br>  

## ⚙ Key Components & Key Concepts  

**<span id="1">1. RDBMS (Relational Database Management System)**</span>  

  - Relation DB is a type of database where datasets have specifically defined relationships between them.
  - RDB concepts: primary key, foreign key, SQL
  - RDBMS: Oracle, MySQL, Microsoft SQL Server, PostgreSQL, MariaDB

<br>  

**<span id="2">2. RDS (Relational Database Services)**</span>  

  - cloud RDBMS that is easily configured, maanged and scaled.
  - Amazon RDS:
    - Automating time-consuming operation tasks (hardware provisioning, database configuration, patching and backup)
    - Cost-effective and scalable DB 

<br>  

**<span id="3">3. RDS characteristics**</span>  

  1) Elastic scaling of instance and storage
    - CPU and memory options 
    - integrate with CloudWatch (elastic scaling according to traffic volume)
    - General Purpose (SSD) for normal workload
    - Provisioned IOPS (SSD) for high speed and large-scale processing
    - Magnetic for infrequent small workload

  2) Easy backup and recovery
    - Inter-AZ DB synchronisation
    - High availability: automatic db failover  

  3) High availability across multiple AZs
  4) Enhanced security with RDS encryption 
  5) DB migration 


<br>  

## 🙌⌨ Hands-on Practice   

  - 1) Create MySQL database on AWS RDS
    - Download MySQL workbench and try connecting to the AWS db (failed😿) 🐰🥕
    - Try video tutorial (Be a Better Dev, 2019)
      - 
  - 2) Connect MySQL database to PHP application running on web server

  - 3) 

<br>  

<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Discovery%20Book/5%20Database/5-5-1%20mysql%20connection%20successful.png" width=750/>
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Discovery%20Book/5%20Database/5-5-2%20mysql%20connection%20detail.png" width=750/>

<br>

### References}  

  - Yeonghwan Gwon(2021) AWS Discovery Book
  - Be A Better Dev (2019) AWS RDS MySQL Database Setup | Step by Step Tutorial https://www.youtube.com/watch?v=Ng_zi11N4_c&ab_channel=BeABetterDev

Process finished with exit code 0
