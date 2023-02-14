---
title: "Observe apps running in Kubernetes (EKS)"
weight: 93
---
### Observe apps running in Kubernetes (EKS)

This guide will cover how to use the Elastic Stack to provide comprehensive monitoring of your EKS Kubernetes environment including:
* Container Logging
* Container Metrics
* Kubernetes posture management
* Kubernetes process and session monitoring
* EKS Audit Logging
* Kubernetes SIEM rules

To be able to tell the Elastic Agent what data to collect we will create a policy with the relevant kubernetes integrations. 
1. In the left navigation menu, select “Fleet”
2. Select the “Agent policies” tab 
3. Select “Create agent policy”
4. Call the policy something like  “k8s” and leave the default to gather system logs and metrics. 

![Kubernetes agent policy](/images/create-agent-policy.png)

### Kubernetes Integration
Let's start adding integrations to our new policy. 
1. Click the policy name.
2. Click “Add integration”
3. In the search bar lets search for “kubernetes”. This should give us the “Kubernetes“ and “Kubernetes Security Posture Management” integrations
4. Let's start with the Kubernetes integration. 
5. Click the integration and then “Add integration”.
6.  Leave all of the defaults and click “Save and continue”. This will do two things, it will add the assets for this integration and also create an instance of this integration within your policy.
7. It will prompt you to add agents but we want to add some extra integrations first so select “Add Elastic Agent later”. 

### Kubernetes Security Posture Management integration
Now let's add the Kubernetes Security Posture Management integration. Click “Add integration” again then find and click on the integration. You will see from the documentation that to be able to check the EKS cluster the integration will need an IAM user and it provides the required permissions.

In a new tab go to your AWS Console, go to the IAM dashboard and select “Policies” and “Create policy” 
Select the “JSON” tab and paste the permissions from the documentation.

```json
{
   "Version": "2012-10-17",
   "Statement": [
       {
           "Sid": "VisualEditor0",
           "Effect": "Allow",
           "Action": [
               "ecr:GetRegistryPolicy",
               "eks:ListTagsForResource",
               "elasticloadbalancing:DescribeTags",
               "ecr-public:DescribeRegistries",
               "ecr:DescribeRegistry",
               "elasticloadbalancing:DescribeLoadBalancerPolicyTypes",
               "ecr:ListImages",
               "ecr-public:GetRepositoryPolicy",
               "elasticloadbalancing:DescribeLoadBalancerAttributes",
               "elasticloadbalancing:DescribeLoadBalancers",
               "ecr-public:DescribeRepositories",
               "eks:DescribeNodegroup",
               "ecr:DescribeImages",
               "elasticloadbalancing:DescribeLoadBalancerPolicies",
               "ecr:DescribeRepositories",
               "eks:DescribeCluster",
               "eks:ListClusters",
               "elasticloadbalancing:DescribeInstanceHealth",
               "ecr:GetRepositoryPolicy"
           ],
           "Resource": "*"
       }

   ]
}
```

Select “Next:Tags”, then “Review” give the policy a name of “elastic-kubernetes-posture” and click “Create policy”.
Now we have a policy with the correct permissions, we can create the service account for the agent to access EKS.
Go to “Users” and “Add users”. Let’s name it “elastic-kubernetes-posture-user” and select “Access key” as the credentials. In the permissions screen we can select “Attach existing policies directly” and find the policy we just created called “elastic-kubernetes-posture”. Then go through the “Tags” and “Review” screens before confirming with “Create user”.
We now have our user. You should be immediately given access key credentials. Copy both the  Access key ID and Secret access key and we can head back to Elastic.

Back in the posture management integration, click “Add Kubernetes Security Posture Management”. In the configuration screen, in “Kubernetes deployment” select “Kubernetes Security Posture Management“. You can then add the credentials for the user we just created. Your screen should look like the below image with the correct credentials.

![Kubernetes integration](/images/add-kubernetes-integration.png)
Select “Save and continue” then again pick to deploy agents later.

### Endpoint and Cloud Security

Back to your policy, let’s add one final integration. Back in “Add integration” select “Endpoint and Cloud Security” and then “Add Endpoint and Cloud Security”. Let’s call the integration “k8s-endpoint”. Click “save and continue”, again, choose to deploy agents later.

We now have 3 integrations in our policy so it should look like this.

![Kubernetes agent policy](/images/kubernetes-monitoring.png)

We would like to collect session information from kubernetes hosts so let's add that. Click on the name of the Endpoint integration we just created “k8s-endpoint” and you will be taken to the extensive configuration options. Scroll to the bottom and turn on “Include session data”.

![Include session data](/images/session-viewer.png)

### Deploying Elastic Agent in EKS

To enable the Endpoint and Cloud Security integration to capture the required information we can follow the steps outlined in the documentation here: [Elastic Kubernetes Documentation](https://www.elastic.co/guide/en/security/current/kubernetes-dashboard.html)

This provides an OOTB manifest to deploy Elastic Agent, with Endpoint added, as a Daemonset to our EKS cluster.  Download this example manifest file here:
[Example manifest](https://raw.githubusercontent.com/elastic/endpoint/main/releases/8.4.0/kubernetes/deploy/elastic-endpoint-security.yaml)

1. Fill in the manifest’s `FLEET_URL` field with your Fleet server’s Host URL. To find it, go to Kibana → Management → Fleet → Settings. 
![Fleet server URL](/images/fleet-server.png)

2. Fill in the manifest’s `FLEET_ENROLLMENT_TOKEN` field with a Fleet enrollment token. To find one, go to Kibana → Management → Fleet → Enrollment tokens. Make sure to use or generate a token which is associated with the k8s policy.
![Fleet enrollment token](/images/enrollment-token.png)

We can now apply the updated manifest to our EKS cluster to deploy our Elastic Agent Daemonset. E.g. `kubectl apply -f elastic-endpoint-security.yaml`
Everything that is within your Kubernetes cluster will be monitored using Elastic now.
