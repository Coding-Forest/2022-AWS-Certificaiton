# 🌐 Network Traffic Load Balancing 🚙🚗🚓🚚🚒🏍️🚴

### ⚙️Key Components & Key Concepts

  - `SSH`: Secure Shell is a cryptographic network protocol for operating network services securely over an unsecured network. Typical applications include remote command-line, login, and remote command execution, but any network service can be secured with SSH.
  - `EC2`: Amazon Elastic Compute Cloud is a part of Amazon.com's cloud-computing platform, Amazon Web Services, that allows users to rent virtual computers on which to run their own computer applications.

<br>

## 🖥️⚡ Virtualisation and Virtual machine 

  - Creating a virtual computer using Hypervisor
  - Abstracts away the OS

  **Benefits of virtualisation**
  Personal 
   - Learn and experiment with new OS
   - Test your app on different OS
  Company
   - High risk: one point of failure
     - >> include OS and all applications on it 
 

  **Hypervisor**
  - Type 1: {Hardware + Hypervisor = Bare Metal}
    - Examples: VMware, Microsoft Hyper-v
    - Use cases: Big companies, ☁️Cloud service platforms☁️
    - Benefits
      - Use all the resources of a performant big server
      - Users can choose any resource combinations
  - Type 2: Host OS + Hypervisor (i.g. Virtual Box) + Guest OS 
    - Borrows the hardware resources of the host OS
   
   <br>
   
   **👐Hands-on Practice**
   - 🛡️ A security group is a set of firewall🔥🧱 rules that control the traffic for your instance.  

<br>

## 🙌⌨️ Hands-on Practice Guidelines

    - create 2 web servers
    - create a web page for load balance test
    - configure ELB and add an instance
      - test if ELB works in case of server failure 
      - examine post-recovery behaviour


### References

  - Yeonghwan Gwon (2021) AWS Discovery Book
