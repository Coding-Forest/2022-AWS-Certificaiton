# 🗄️ Storage  

[1. 🗄️Storage](#1)  
[2. Data Backup](#2)  
[3. Snapshot](#3)  
[4. S3 & Glacier](#4)  
[5. AMI & Marketplace](#5)  

<br>  

## ⚙ Key Components & Key Concepts  

**<span id="1">1. 🗄️ Storage**</span>  

  - A computer component that stores data (= hard disc💽)
    - You can connect your storage directly to your server (DAS) or
    - build a dedicated storage network for large-scale data storage (NAS, SAN)
  - Server connection methods
    - `DAS` (Direct Attached Storage)
    - `NAS` (Network Attached Storage)
      - cheap as this uses LAN (Local Area Network)
      - 🗃️file storage 
    - `SAN` (Storage Area Network): higher scalability
      - 🧱block storage 

<br>  

**<span id="2">2. Data Backup**</span>  

  Backups are required against...
  - ⚡Failure or damage to hardware
  - ⚡Failure or damage to DB, software, OS
  - 🌪️Data loss or human mistake, query error 

<br>  

**<span id="3">3. Snapshot**</span>  

  Purposes
  - used for data analysis, data protection. amd data replication
  - Data recovery

  **AWS EBS (Elastic 🧱Block Storage)** 
  - supports snapshot
  - Instance Migration: EC2/Regional migration of EBSs

<br>  

**<span id="4">4. S3 & Glacier**</span>  

  - `S3` (Simple Storage Services)
    - Highly scalable, unlimited internet-based object storage service
    - `Bucket`: unique storage space within a Region
      - data is stored in `'key':'value'` object format.
      - Does NOT replace EBS: S3 is a storage technology for file access only.
      - Pricing is determined by data size, access request count, data download count (network out).
        - Free Tier: 5GB, 20,000 GETs, 2,000 PUTs

<br>  

  **Characteristics**
  - Backup & recovery
  - Data archiving 
    - Offers a variety of storage class for data archiving
  - Data lake 
    - Big data (financial data, multimedia files) stored on S3 can be used as data lake for big data analytics📊.
  - ☁️Hybrid cloud storage 
  - Disaster recovery
    - Cross-regional copy
  
  - Applications:
    - 🌐Web service
    - 🩹Backup and recovery
    - 🗄️Storage 
    - 🩺Disaster recovery
    - 📊Big data (data lake, hybrid cloud storage)
    - 🏢Enterprise IT
    - 📲Sending contents
    - 💰Finance
    - 🖥️High-performance computing 
    - 💲E-commerce
    - 🎤Media & entertainment
    - 📈Business Application
    - 📱Mobile
  
<br>  

  **🗄️ Storage classes**
  - Amazon S3 Standard - FA
    - Frequent-access data
    - Up to 20% cheaper than EBS
    - SSL for data transfer and data encryption
  - Amazon S3 Standard - IA 
    - Infrequent acess
    - 58% cheaper than S3 standard
  - Amazon S3 One Zone - IA
    - 20% cheaper than S3 Standard-IA
    - Single AZ storage (other classes use three or more AZs)
  - Amazon Glacier 
    - up to 77% cheaper than S3 standard
    - Automatic object migration
  
  - 🧊Glacier 
    - offers a long-term data archiving using `Vault` 
    - secure, durable, highly-scalable
    - Properties
      - direct access using API/SDK 
      - S3 life-cycle integration: old data in S3 will be automatically moved to 🐻‍❄️Glacier.
      - 3rd party tools + AWS Storage Gateway
      - Access types: emergency access, current model, batch/bulk access

**<span id="5">5. AMI & Marketplace**</span>  

  - AMI (Amazon Machine Image)
  - Marketplace: application/software shopping place 🛍️🛒

<br>  

## 🙌⌨ Hands-on Practice   

  - 1) ⏫Upload/⏬download files on S3
  - 2) Backup PC data on S3
  - 3) Recover instance using AMI

<br>  

<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Discovery%20Book/3%20Storage/3-6%20S3%20bucket1.png" width=750 />
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Discovery%20Book/3%20Storage/3-6%20S3%20bucket2.png" width=750 />
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Discovery%20Book/3%20Storage/3-6%20S3%20bucket3.png" width=750 />
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Discovery%20Book/3%20Storage/3-6-2%20Backup%20data1.png" width=750 />
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Discovery%20Book/3%20Storage/3-6-2%20Backup%20data2.png" width=750 />
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Discovery%20Book/3%20Storage/3-6-2%20Backup%20data3.png" width=750 />
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Discovery%20Book/3%20Storage/3-6-2%20Backup%20data4.png" width=750 />
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Discovery%20Book/3%20Storage/3-7%20AMI%20recovery1.png" width=750 />
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Discovery%20Book/3%20Storage/3-7%20AMI%20recovery2.png" width=750 />

<br>

### References}  

  - Yeonghwan Gwon(2021) AWS Discovery Book

