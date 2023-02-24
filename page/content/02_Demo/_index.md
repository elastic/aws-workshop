---
title: "Root Cause Analysis"
chapter: true
weight: 30
pre: "<b>2. </b>"
---

[Monitoring the AWS environment](https://www.elastic.co/observability/aws-monitoring) is a very common use case for Elastic. You can download the complete [ebook](https://www.elastic.co/aws/the-elastic-observability-guide-for-aws) about that topic.

![AWS overview](/images/aws-overview.png)

Elastic observes cross-VPC, cross-region, cross-AZ, cross-Account. No matter how you organize your environment, Elastic will fit into it. Collect everything in a single Elastic environment and authorize only the relevant team(s) to it. Even if you are responsible for observing multiple different cloud providers or hybrid environments, Elastic can help you get better insights into what is happening in one single tool.

Elastic supports collecting data via different ways. Using the Elastic Agent, but [agentless](https://serverlessrepo.aws.amazon.com/applications/eu-central-1/267093732750/elastic-serverless-forwarder) and native integrations are also available. In the introduction, we already learned about the Elastic Agent and how it can be used. We will continue using the agent to observe the AWS platform and the apps you are running in it.

However, if you prefer not to use the Elastic Agent, you can collect the same data using the [Elastic serverless forwarder](https://serverlessrepo.aws.amazon.com/applications/eu-central-1/267093732750/elastic-serverless-forwarder) which is a Lambda function that is able to collect the same data without the need to deploy an agent.

![AWS serverless overview](/images/aws-serverless-overview.png)
