# 🌐 Network Traffic Load Balancing 🚙🚗🚓🚚🚒🏍️🚴

  - create 2 web servers
  - create a web page for load balance test
  - configure ELB and add an instance
    - test if ELB works in case of server failure 
    - examine post-recovery behaviour

<br>

## Virtualisation and Virtual machine⚡🖥️ 

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

### References

  - Yeonghwan Gwon (2021) AWS Discovery Book
