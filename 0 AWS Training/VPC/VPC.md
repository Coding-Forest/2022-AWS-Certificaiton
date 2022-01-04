# 📝Notes 

## Basics

  - CIDR (Classless Inter-Domain Routing)
    - `172.31.0.0/16`
      - a total of 32-bit address system (four binary octets)
      - `/16`: subnet mask

  RFC1918
    - `10.0.0.0` (10/8 prefix)
    - `172.16.0.0` (172.16/12 prefix) 
    - `192.168.0.0` (192.168/16 prefix)
  
  Packet 
    - "In networking, a packet is a small segment of a larger message. Data sent over computer networks*, such as the Internet, is divided into packets. These packets are then recombined by the computer or device that receives them."

  Route table
  
  Network ACLs (Stateless firewalls)
    - default: allow and deny all traffic 
    - Security group, however, is set to deny all inbound/outbound traffic to and from the VPC by default.

  Security group
    - AWS' autoscaling: 
      - Without autoscaling, you have to allocate IP addresses for additional servers; update security group (this applies to both cases where you add a server and remove a server).
      - With autoscaling, the security group is automatically updated (because we know the traffic is bottlenecked at which port range).
        - This is also helpful in enhancing 🔥firewall security🛡️.  

<br>

## Recap

  - 1) Set IP address.
  - 2) Allocate subnets.
  - 3) Route table + Gateway (create a path to the entry point)
  - 4) Security group (Network ACL, configure the conditions for network  connection) 

<br> 

<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Training/VCP/VPC%2001%20IP%20makeup.png" width=750/>
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Training/VCP/VPC%2002%20RFC1918.png" width=750/>
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Training/VCP/VPC%2003%20subnets.png" width=750/>
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Training/VCP/VPC%2004%20VPC%20recommendations.png" width=750/>
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Training/VCP/VPC%2005%20security%20group.png" width=750/>
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Training/VCP/VPC%2006%20security%20group%20example%20backend.png" width=750/>
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Training/VCP/VPC%2006%20security%20group%20example.png" width=750/>
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Training/VCP/VPC%2007%20NAT%20gateway.png" width=750/>
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Training/VCP/VPC%2008%20NAT%20gateway%20config.png" width=750/>

<br> 

### References

  - Amazon Web Services Korea (2017) Create virtual data centre - VPC basics and connection options - Solutions Architect YANG Seungdo (AWS Korea) https://www.youtube.com/watch?v=R1UWYQYTPKo&ab_channel=AmazonWebServicesKorea
  - CloudFlare (n.d.) Packet https://www.cloudflare.com/ko-kr/learning/network-layer/what-is-a-packet/
