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
