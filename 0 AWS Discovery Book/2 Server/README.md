# Server

Revision: 29~34p

[1. 🖥️Server & 🗄️Storage](#1)  
[2. 🛡️Security & 🔥🧱Firewall](#2)  
[3. ☁️Cloud terms](#3)  
[4. 🛡️Security Groups🔥🧱](#4)  

### ⚙ Key Components & Key Concepts

<span id="1">**1. 🖥️Server & 🗄️Storage**</span>

  - `Server`: a computer designed to perform specific tasks 
    - Depending on the types of tasks given, a notebook or a desktop computer can serve as a server.
    - As it is designed to serve for specialised tasks, it is more expensive than general PCs
    - Runs on a server OS (UNIX, Linux, Windows Server, etc). 
      - ☁️`AWS EC2 (Elastic Compute Cloud)`: a virtual computer to set up and run a server. You can also install software on this virtual EC2.
  - `Storage`: a device or component that serves as a space to store information and data
    - 💽`Hard disk`: a group of round discs (platters) made of aluminium alloy or tempered glass coated with magnetic thin film . The CPU performs store, search, and delete operations to 'permanently store (🔌electricity is off)' data. 
      - Mechanical drive (uses spindle motor)
      - SSD (Solid-State Drive): based on flash memory. Faster with lower latency, and lesser noise compared to the mechanical drive, however costs more than its counterpart for the same storage capacity.
    - More failure-tolerant with higher performance than general-purpose computers
      - DAC (Disk Array Controller)
      - RAID (Redundant Array of Independent Disks)
    - `EBS (Elastic Block Storage)`: discs that can be added to `EC2` to increase the prformance
  
<br>

<span id="2">**2. 🛡️Security & 🔥🧱Firewall**</span>

  - 🔥🧱Firewall in information systems
    - a system that protects important internal information assets against illegal external attacks

  🐠🌳🌴AWS services for 🛡️security
  - `IAM` (Identity & Access Management)
  - `Amazon GuardDuty`
  - 🛡️`Shield` against DDos
  - 🔥`WAF` (Web Application Firewall): filters malicious web traffic 

<br>

**<span id="3">3. ☁️Cloud terms**</span>  

  - Region
  - Availability Zone: IDC (Internet Data Centre)
  - Edge Location: a group of cache servers for the CDN service ☁️`CloudFront`
  
  - `CDN` (Content Delivery Network): Amazon CloudFront is a content delivery network operated by Amazon Web Services. Content delivery networks provide a globally-distributed network of proxy servers that cache content, such as web videos or other bulky media, more locally to consumers, thus improving access speed for downloading the content ([Wikipedia](https://en.wikipedia.org/wiki/Amazon_CloudFront)).

  - `EBS` (Elastic Block Storage): 

<br>  

**<span id="4">4. 🌴Amazon Security Groups🔥🧱**</span>  

  - A virtual 🔥🧱firewall that controls inbound/outbound network traffic to and from the `EC2 instances`.
  - can allocate up to 5 security groups per `instance`.
    - 1) limisted number of group instances up to 500 groups
      - up to 50 rules per group
      - up to 5 security groups per network interface
    - 2) Only Allow policy available for network traffic and NO Deny policy
      - Use `VPC` (Virtual Private Cloud)'s `ACL` (Network ACL) instead
    - 3) Control inbound / outbound traffic separately

<br>

## 🙌⌨ Hands-on Practice   

<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Discovery%20Book/2%20Server/2-6%20EC2%20Linux%20instance.png" width=600/>
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Discovery%20Book/2%20Server/2-6%20EC2%20Linux%20instance%202.png" width=600/>

<br>  

### References}  

  - Yeonghwan Gwon(2021) AWS Discovery Book
 
