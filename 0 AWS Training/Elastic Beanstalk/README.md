# 🌴 Elastic Beanstalk

## Notes 

  - No extra charge. Pay for the AWS resources (EC2, S3, etc)
  - Applications:
    - 🌐web site
    - 📲mobile backend
    - API backend

## Deploy methods

  - 1) Rolling with additional batch
    -
  - 2) Immutable 
    - Immutable + Blue/Green do not change the existing env.
    - However, Immutable do not create a new env (DNS) but creates a new group within the existing env. 
  - 3) Blue/Green
    - Copy the entire environment 
    - Then swap environment URLs
    - Browser cache may be a bit of an issue :P
    - Pros & Cons
      - Pros
        - The previous env is still running. Roll back fast, any time. 
        - Deploy without downtime
        - Failing to deploy the new env does not affect the existing instance. 
      - Cons
        - Slow batch (~ 5 mins) due to creating a new env.
        - Manual RDS copy required (no automatic cloning)

<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Training/Elastic%20Beanstalk/Elastic%20Beanstalk%2001.png" width=730 />
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Training/Elastic%20Beanstalk/Elastic%20Beanstalk%2002.png" width=730 />
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Training/Elastic%20Beanstalk/Elastic%20Beanstalk%2003.png" width=730 />
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Training/Elastic%20Beanstalk/Elastic%20Beanstalk%2004.png" width=730 />
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Training/Elastic%20Beanstalk/Elastic%20Beanstalk%2005.png" width=730 />
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Training/Elastic%20Beanstalk/Elastic%20Beanstalk%2006.png" width=730 />
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Training/Elastic%20Beanstalk/Elastic%20Beanstalk%2007.png" width=730 />
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Training/Elastic%20Beanstalk/Elastic%20Beanstalk%2008.png" width=730 />
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Training/Elastic%20Beanstalk/Elastic%20Beanstalk%2009.png" width=730 />
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Training/Elastic%20Beanstalk/Elastic%20Beanstalk%2010.png" width=730 />
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Training/Elastic%20Beanstalk/Elastic%20Beanstalk%2011.png" width=730 />
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Training/Elastic%20Beanstalk/Elastic%20Beanstalk%2012.png" width=730 />
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Training/Elastic%20Beanstalk/Elastic%20Beanstalk%2013.png" width=730 />
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Training/Elastic%20Beanstalk/Elastic%20Beanstalk%2014.png" width=730 />
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Training/Elastic%20Beanstalk/Elastic%20Beanstalk%2015.png" width=730 />
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Training/Elastic%20Beanstalk/Elastic%20Beanstalk%2016.png" width=730 />
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Training/Elastic%20Beanstalk/Elastic%20Beanstalk%2017.png" width=730 />
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Training/Elastic%20Beanstalk/Elastic%20Beanstalk%2018.png" width=730 />
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Training/Elastic%20Beanstalk/Elastic%20Beanstalk%2019.png" width=730 />
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Training/Elastic%20Beanstalk/Elastic%20Beanstalk%2020.png" width=730 />
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Training/Elastic%20Beanstalk/Elastic%20Beanstalk%2021.png" width=730 />
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Training/Elastic%20Beanstalk/Elastic%20Beanstalk%2022.png" width=730 />
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Training/Elastic%20Beanstalk/Elastic%20Beanstalk%2023.png" width=730 />
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Training/Elastic%20Beanstalk/Elastic%20Beanstalk%2024.png" width=730 />
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Training/Elastic%20Beanstalk/Elastic%20Beanstalk%2025.png" width=730 />
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Training/Elastic%20Beanstalk/Elastic%20Beanstalk%2026.png" width=730 />
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Training/Elastic%20Beanstalk/Elastic%20Beanstalk%2027.png" width=730 />
<img src="https://github.com/Coding-Forest/2022-AWS-Certificaiton/blob/main/0%20AWS%20Training/Elastic%20Beanstalk/Elastic%20Beanstalk%2028.png" width=730 />

Process finished with exit code 0


<br>

## ✍️Hands-on project   

  Dev Day Seoul Elastic Beanstalk - Deploy and update sample app on Elastic Beanstalk

- Installed
    - Git
    - Nodejs command prompt

- `zip -r app-ver2.zip` 
  - Once you updated your code, re-package your code by zipping (https://youtu.be/AfRnvsRxZ_0)
- `unzip -l app-ver2.zip`
  - Double-check if the code has been re-packaged successfully.


<br>

### References

  - Amazon Web Services Korea (2018) Seoul Dev Day - AWS Elastic Beanstalk https://www.youtube.com/watch?v=AfRnvsRxZ_0&t=442s
