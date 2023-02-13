---
title: "The environment"
weight: 31
---
## Architecture

We’ve prepared an AWS + Elastic environment for you. Within the AWS environment there is a simple python application deployed on EC2. This application is accessing DynamoDB and uses Lambda functions to enrich an object with more information. All the monitoring information including metrics and logs from the entire system are collected in Elastic. This is done by using one Elastic Agent at the EC2 instance and the Elastic Serverless forwarder for the logs. While the Elastic Agent would be also able to collect the different logs types this architecture has the advantage of running log monitoring on different hardware. 

The architecture of the sample app looks like this
![Elastic environment](/images/aws_workshop_arch.png)

While running the workshop you have access to your Elastic Cluster and to the EC2 instances that are running the application. In your Elastic Cluster you can find a dashboard called **Workshop Dashboard**. Use this dashboard as a starting point for all your tasks. You can solve all the tasks by using these components. You don’t need anything else.
It's expected that you find the issues using the Elastic Cluster and fix the issues within the EC2 environment(s).

The code that is running the application is downloaded from this [GitHub Repo](https://github.com/LucaWintergerst/workshop-draft) to the EC2 environment(s). 
