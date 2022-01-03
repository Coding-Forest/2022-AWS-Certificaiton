# 🌐Network  

[1. VPN](#1)  
[2. VPC](#2)  
[3. VPC components](#3)  
[4. VPC services](#4)  

<br>  

## ⚙ Key Components & Key Concepts  

**<span id="1">1. VPN**</span>  

  - A private network /communication service featuring higher stability and security.
  - Migrating IDCs (Internet Data Centres) is a challenging task that requires inter-system communication for data transfer.
  - Hybrid cloud in Amazon
    - VPC (Virtual Private Cloud)
    - VPC Gateway

<br>  

**<span id="2">2. VPC**</span>  

  - Virtual Private Cloud
    - allocates logically isolated network space to a virtual network that uses AWS resources.
    - allows a complete control of network configuration
      - IP address range, subnet, route table, network gateway configuration
      - IPv4, IPv6 
      - Safe access to resources and applications
    - Characteristics
      - it is establishing a private network in AWS
      - Hybrid environment: the company and AWS are connected through VPN or virtual networking
      - Other AWS services deploy into VPC: AWS resources can be used like the company's internal system. It is easy to integrate internal software to AWS (mailing system, groupware, file server)
      - Available in all Regions

<br>  

**<span id="3">3. VPC components**</span>  

  1) Private IP
    - IP address used only inside the VPC (cannot be accessed via internet)
    - automatically assigned within the instance' subnets
    - allows for inter-instance communication within the same network
    
  2) Public IP
    - address that can be accessed via internet
    - on EC2 creation, you can choose the public IP option.

  3) Elastic IP
    - fixed public IP address for dynamic computing

  4) VPC and Subnets
  
  - **Subnet**
    - a VPC can be further broken down into IP blocks. Subnet is this group of certain IP blocks.

  - **VPC**
    - VPC applies to all AZs in the Region.
    - can add one or more subnets to each AZ.
    - Conversely, a subnet can be created within a single AZ only, and is not extensible to multiple AZs.
    - VPC IP address: in CIDR (Classless Inter-Domain Routing)
 
  - **Public subnet & private subnet**
    - Public subnet: routed to IGW (Internet GateWay)
      - ex) 🌐web server
    - Private subnet: NOT routed to IGW
      - ex) 🗄️DB server (as it requires stronger security)
  
  - Route table
    - Each subnet should be connected to the routing table which allocates the permitted path to the outbound traffic (which goes out of subnet)
    - Each created subnet is connected to the default routing table by default.

<br>  

**<span id="4">4. VPC services**</span>  

  - VPC allows or blocks communication based on IPs and ports.
    - Security Group
    - Network ACL (Network Aces Control List)

  - VPC Peering Connection 
    - Traffic routing (network connection) between two VPCs
      - The two different VPC instances can communicate with each other as if they belonged to the same network.

  - NAT (Network Address Translation) Gateway
    - In an internal network that uses different IP addrss system, translates the internal IP address into public IP addresses
    - When is NAT useful? 
      - An important internal (security) service that does not need public communication. However, if it requires software update online or Windows patch, NAT gateway ir NAT instance is required.
    - Conditions:
      - 1) Assign a public subnet in order to create a NAT gateway.
      - 2) Elastic IP address is required which will be connected to the NAT gateway.
      - 3) After creating a NAT gateway, update the routing table connected to the private subnet to allow for the internet traffec via NAT gateway.

<br>  

## 🙌⌨ Hands-on Practice   

  1) Create a VPC with 2 subnets (1 private, 1 public)
  2) Inter-Region VPC peering
    - Create VPCs in Seoul and London, respectively.
      - Seoul: VPC with a public and private subnets
      - London: VPC with a public subnet only
    - Create an EC2 in Seoul and London, respectively.
      - When creating, be sure to configure the network in instance detail setup. 
    - Test the peering connection between Seoul and London through PuTTY.

<br>

<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Discovery%20Book/4%20Network/4-1%20VPC%20services.png" width=900/>
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Discovery%20Book/4%20Network/4-2%20VPCs.png" width=900/>
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Discovery%20Book/4%20Network/4-7-1%20create%20VPC.png" width=900/>
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Discovery%20Book/4%20Network/4-7-2%20Peering%20request%20sent.png" width=900/>
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Discovery%20Book/4%20Network/4-7-3%20Accept%20peering%20request.png" width=900/>
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Discovery%20Book/4%20Network/4-7-4%20Route%20tablepng.png" width=900/>
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Discovery%20Book/4%20Network/4-7-5%20inter-region%20peering%20successful.png" width=900/>

<br>  

### References}  

  - Yeonghwan Gwon(2021) AWS Discovery Book
  - Cobalt Ridge (2017) Simple Concepts: CIDR Notation https://www.youtube.com/watch?v=u13AdjAUNmA&ab_channel=CobaltRidge

Process finished with exit code 0

