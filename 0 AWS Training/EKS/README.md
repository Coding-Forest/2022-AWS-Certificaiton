# Elastic Kubernetis Services (EKS)

## Notes 

  - `kubectl run nginx --image=nginx`

## 

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



<br>

## ✍️Hands-on project   

  Dev Day Seoul Elastic Kubernetis Serviecs 

<br>

### References

  - Amazon Web Services Korea (2020) EKS AWS Cloud Week https://www.youtube.com/watch?v=TFWNl1rzpxY
  - Amazon Web Services Korea (2020) Nexon Korea AWS Community Day 2020 https://www.youtube.com/watch?v=O3znWPUdt18&t=48s
  - Shiraz Hazrat (2020) Deploy Kubernetes From Scratch On AWS In 5 Min! (Plus Intro To Kubernetes) https://www.youtube.com/watch?v=vpEDUmt_WKA