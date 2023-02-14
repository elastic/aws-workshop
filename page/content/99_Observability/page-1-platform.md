---
title: "Observe the AWS platform"
weight: 94
---
### Platform Logs

In AWS you have three options to collect logs. This also holds for the platform / service specific logs. You can collect the data via the Serverless Log forwarder, via CloudWatch or collect the data from an S3 bucket.

If you decide for the S3 bucket you need to configure SQS notifications that get triggered whenever new data is written to the bucket. This approach is best practice to avoid significant lagging with polling. Elastic Agent combines notification and polling together by using Amazon SQS for Amazon S3 notification when a new Amazon S3 object is created.

To configure SQS Event Notifications click into the bucket that is holding your log data and navigate to “Properties”. Within the Properties section look for Event notifications and create a new entry.

#### Cloudtrail
AWS CloudTrail enables governance, compliance, operational auditing, and risk auditing of your AWS account. This is helpful to observe the activities happening within your AWS environment(s).
![AWS cloudtrail](/images/cloudtrail.png)

#### VPC Flow logs
Elastic Observability allows you to quickly search, view, and filter Amazon Virtual Private Cloud (Amazon VPC) Flow Logs to monitor network traffic within your Amazon VPC with Kibana. With this integration, you can analyze the flow log data and compare it with your security group configurations to maintain and improve your cloud security.
![AWS vpc flow](/images/vpc-flow.png)

### CloudWatch metrics
With Elastic’s integrations and pre-built dashboards for AWS, you can collect AWS metrics such as usage, performance and more to see how every signal correlates — enabling you to make more informed business decisions.
![AWS CloudWatch metrics](/images/metrics.png)

In order to collect AWS CloudWatch metrics you need to navigate to the installed integrations and change the AWS integration. Click on AWS → Integration policies → aws-1 (Default name)
![Elastic integration page](/images/integration-page.png)
Just enable every integration that is delivering metrics. Screenshot is not showing all possible options.
![Elastic aws metric integrations](/images/metric-integrations.png)
After enabling all the metrics you should be able to see the data in the out of the box dashboards.

You can also extend the out of the box dashboards by downloading pre-built dashboards from the Elastic Community.

### Billing data
The AWS Billing data is a special part of the metric data from the previous chapter. The purpose of this data is to get mutual understanding of the current spending within the observed AWS accounts / organizations.
Per default AWS only sends service level billing data which is nice to get a high level overview. However if your target is to reduce costs by correlating the usage data (logs and metrics) with the billing data this might be not enough details. AWS also offers to export more detailed billing data within the API or into a separate S3 bucket. Collecting this resource level billing data is very useful to compare the usage and the actual cost and therefore identify possible savings.

![Elastic aws billing integration](/images/billing-integration.png)

The AWS billing data is just another AWS integration that is available for the Elastic Agent. Just enable this integration and make sure that the access you are using has appropriate rights in order to get the data.

