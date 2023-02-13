---
title: "Run the Cloud Formation script"
weight: 23
---

Now we have everything in place in order to create your environment using Cloud Formation. 
Just click on the following button and enter the API key that you have created within your Elastic Cloud via AWS Marketplace environment (step 4)

{{% button href="https://eu-central-1.console.aws.amazon.com/cloudformation/home?region=eu-central-1#/stacks/create/review?templateURL=https://s3.eu-central-1.amazonaws.com/cf-templates-1co02imbb4wen-eu-central-1/2023-02-06T123446.553Zbvm-cloudformation.yaml&stackName=myElasticWorkshopEnvironment" icon="fas fa-wrench" %}}Create your environment{{% /button %}}

Add your Elastic API Key to the template:
![Enter Elastic API Key](/images/CloudFormation-Stack.png)

Acknowledge the creation of resources:
![acknowledge](/images/acknowledge.png)

And finally click on create stack. Afterwards we will create the environment for you. This can take some time.


