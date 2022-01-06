
## Availability    
  
The server/application is up and running. It keeps serving the visitors;  
Host your application across multiple regions for disaster recovery.  
  
  
- 🔑Key concepts 
  - high availabilty
    - fault-tolerance
    - failure-resistant
    - instance-level horizontality (often across multiple AZs)
  - global availability
    - regional-level horizontality 


- **High availability**
  - Fault-tolerant (failure-resistant)
  - Your system continues operating despite failures or malfunctions.
    - AWS acheves this through instance multiplication. 
- **Global availability** 
  - Horizontal, geographical, across physical areas  
  
- 💬Example statements 
  - Global availability 
    - You have a mission-critical application which must be _**globally available**_ at all times.
      - Multiple regions   
    - An international company needs to provide low-latency applications for **_customers around the world_**.
        - Global reach (vs. high availability?)
  - High availabilty
    - You can design your systems in the AWS cloud to withstand the failure of an individual or multiple components. 

<br>

## Elasticity

Quantitative in nature;  
About traffic volume - how many users? how much traffic? 

- 💬Example statements 

<br>

## ☁️Cloud Architecture & Principles

Loose coupling - even if one component fails, the entire system won't fail.  
Everything will fail - helps build a highly available + fault-tolerant system. 

- Example statements 

<br>



## Database 

- 🔑Key concepts 
  - **MySQL**   
  - **NoSQL**   
  - Horizontal scalability
  - Verticla scalability
  
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/images/database%20sql-nosql.png" width=500 />
  
**MySQL**   
**NoSQL** (AI Holic, 2020)  
  - Scalability
    - Horisonzal scalailbity
      - Data access speed: O(1) using hashing 
      - Horizontal scalability - Throughput will increase if you increase the number of servers. 
        - Reliable scalability owing to the data access speed (O(1)) 
        - Horizontal scalability reduces risks in terms of engineering. 
      - DynamoDB is a NoSQL databased fully managed by AWS. 

- SQL language
  - Unified SQL language vs no language
  - SQL for structured data
  - NoSQL for UNstructured data
  
- Schema 
  - Strict schema vs Schema-free
  - Strict schema for structured data
  - Schema-free for UNstructured data
 
- 💬Example statements 

<br>

## DDoS attack

  🛡️The following services as DDoS attack mitigation features.
  - Route 53
  - WAF 

- 💬Example statements 

<br>



## EC2 instance classes 

- 🔑Key concepts 
  - On-demand: (no plan)
  - Reserved: comes with a plan for a specified period of time (1 or 3 years)
  - Spot
  - Dedicated: launch instances in the VPC on customer's dedicated hardware 

- Dedicated instance
  - "_Dedicated Instances are Amazon EC2 instances that run in a VPC on hardware that's dedicated to a single customer. Your Dedicated instances are physically isolated at the host hardware level from instances that belong to other AWS accounts_" (AWS).


- 💬Example statements 
  -  Spot instances are a cost-effective choice if you can be flexible about when your applications run and if your applications can be interrupted.
  -  Reserved instances are the most cost-effective solution if you want to migrate to AWS your non-interruptible application for a 3-year period. 

<br>



## Traffic 🚙🚗🚓🛻🚒

- 🔑Key concepts 
  - ELB (elastic load balancing)
  - Autoscaling

- ELB (elastic load balancing)
  - As the name suggests, it deals with the traffic load, not the EC2 instances.
  - It divides the traffic load into smaller chuncks and allocate them to different existing EC2 instances.
  - (horizontally) distributes incoming traffic across existing healthier EC2 instances.
  - Increases the fault tolerance of your application.

- Autoscaling
  - Increases or decreases the number of instances to serve the traffic according to the scaling policy to manage both peak and off-peak hour loads.
  - Autoscaling ensures that you have the correct number of instances available to handle the load for your application. 


- 💬Example statements 
  -  

<br>




## 🗄️Storage 

- 🔑Key concepts 
  - EBS: per-EC2 hard drive (images are not shared).
  - EFS: inter-EC2 hard drive and images can be shared.
  - S3: stand-alone storage that can be accessed via internet. 


- 💬Example statements 
  -  

<br>



## CloudTrail👣 vs. CloudWatch👀

- 🔑Key concepts 
  - CloudTrail👣
  - CloudWatch👀

**CloudTrail🚋**
  - Who did what on AWS?
  - Concerned wiht 🧑‍🤝‍🧑 within your account.
  - Enables governance, compliance, operational auditing, and risk auditing of your AWS account. 

**CloudWatch👀**

- Example statements 
  - ________ monitors and retains AWS account activity related to actions across your AWS infrastcuture (CloudTrail👣)

<br>



## Fault tolerance

"_Fault tolerance is a process that enables an operating system to respond to a failure in hardware or software. This fault-tolerance definition refers to the system's ability to continue operating despite failures or malfunctions._ (Fortinet, n.d.)"


- 🔑Key concepts 
  - 

- 💬Example statements 
  -  

<br>




## Other services

### ⚙️AWS Config 

- 🔑Key concepts 
  - 

- 💬Example statements 
  - ______ enables you to assess, audit, and evaluate the configurations of your AWS resources.

<br>



## 📝More notes 

Time required for searching data in a sorted list 
- Log(n) using binary search



<br>



### References

  - AI Holic (2020) NoSQL vs SQL https://www.youtube.com/watch?v=CjsVx9sARDU&ab_channel=AIHolic
  - Agira Technologies (2019) The key differences between SQL and NoSQL databases https://www.agiratech.com/the-key-differences-between-sql-and-nosql-database
  - AWS Training Center (2021) AWS Storage - EBS vs S3 vs EFS https://www.youtube.com/watch?v=6vNC_BCqFmI&ab_channel=AWSTrainingCenter
  - Fortinet (n.d.) What is Fault Tolerance? https://www.fortinet.com/resources/cyberglossary/fault-tolerance
  - AWS (n.d.) Amazon EC2 Dedicated Instances https://aws.amazon.com/ec2/pricing/dedicated-instances/
