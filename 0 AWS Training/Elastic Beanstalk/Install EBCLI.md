# EBCLI

  Steps for EB CLI
   
  - EBCLI [download here👉](https://awscli.amazonaws.com/AWSCLIV2.msi)
    After installing the required version of python (3.7.0) and pip 
    - `pip install awsebcli --upgrade --ignore-installed`
    - then `eb init` (initiates the environment)
   
          Select a default region
          1) us-east-1 : US East (N. Virginia)
          2) us-west-1 : US West (N. California)
          3) us-west-2 : US West (Oregon)
          4) eu-west-1 : EU (Ireland)
          5) eu-central-1 : EU (Frankfurt)
          6) ap-south-1 : Asia Pacific (Mumbai)
          7) ap-southeast-1 : Asia Pacific (Singapore)
          8) ap-southeast-2 : Asia Pacific (Sydney)
          9) ap-northeast-1 : Asia Pacific (Tokyo)
          10) ap-northeast-2 : Asia Pacific (Seoul)
          11) sa-east-1 : South America (Sao Paulo)
          12) cn-north-1 : China (Beijing)
          13) cn-northwest-1 : China (Ningxia)
          14) us-east-2 : US East (Ohio)
          15) ca-central-1 : Canada (Central)
          16) eu-west-2 : EU (London)
          17) eu-west-3 : EU (Paris)
          18) eu-north-1 : EU (Stockholm)
          19) eu-south-1 : EU (Milano)
          20) ap-east-1 : Asia Pacific (Hong Kong)
          21) me-south-1 : Middle East (Bahrain)
          22) af-south-1 : Africa (Cape Town)
          (default is 3): 10
  
          ☑️ Enter Application Name 
          (default is "eb-node-express-sample"):
          Application eb-node-express-sample has been created.

          ☑️It appears you are using Node.js. Is this correct?
          (Y/n): y
          Select a platform branch.
          1) Node.js 14 running on 64bit Amazon Linux 2
          2) Node.js 12 running on 64bit Amazon Linux 2
          3) Node.js 10 running on 64bit Amazon Linux 2 (Deprecated)
          4) Node.js running on 64bit Amazon Linux (Deprecated)
          ☑️(default is 1):

          ☑️ Do you wish to continue with CodeCommit? (Y/n): n
          Do you want to set up SSH for your instances?
          (Y/n): y

          ☑️Select a keypair.
          1) AWS_Study_Key
          2) [ Create new KeyPair ]
          (default is 1): 1
   
  
  
  Steps for AWS CLI
    - Create a user and set up a local profile on aws.amazon.com
      - using AWS configure command 
      - in order to interact with EB CLI.
    - IAM >> Users >> Add users
      - give: 
        - user name
        - Access key - Programmatic access (Enables an access key ID and secret access key for the AWS API, CLI, SDK, and other development tools).
      - then you get:
        - Access key ID
        - Secret access key
    - Now go to `cmd`
