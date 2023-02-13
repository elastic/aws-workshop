---
title: "Observe apps running in AWS"
weight: 32
---

While apps running in AWS use many of the available AWS services they all have their custom code as well. Consequently observing the AWS services and platform is only one part of the story. The other necessary part to get full visibility is to have the ability to look deep into what's happening in your application as well by observing your individual logs, metrics and application traces.  

### Application logs
In order to get your individual logs to Elastic you need to consider two things. First how to get the logs of all parts of the application in. If your application is using container or kubernetes technology this is quite simple.

If your application is running on EC2 instances you might need to collect custom log sources.

Independently of the log collection your also need to consider the log parsing. Per default custom logs will be collected as is. But most often the interesting information are within the log line itself. Therefore it can be helpful to parse the relevant information within the log lines and store them in separate fields. This makes it really handy to create visualizations and filters based on these extracted values.

If you are not sure whether you need something to parse out or not the best option is use a runtime field. A runtime field can be generated after the data is loaded and will extract the necessary information from any document that exists. However this comes with some performance drawbacks.
If you know which kind of information you would like to extract the better option is to use pre index parsing using ingest node pipelines. Within an ingest node pipeline you can configure so-called processors to extract and fine tune the parsing before the data gets indexed to Elastic. The big advantage is that this will happen only once per document. In comparison to the runtime fields where the extraction happens on every query for every affected document.

Having a look into the integrations page within Elastic there are multiple possibilities to get your custom logs in.
![Elastic integration page](/images/integration-page-2.png)
Elastic offers Serverless log forwarding using Lambda functions, as well as Log collection from S3, CloudWatch and directly from the EC2 machine. In addition to that you also could use the diverse language clients to directly send the logs to Elastic from your application.

After you added the integration based on your need you can change the parsing like described above using the Ingest Pipelines (Under Stack Management).  

### APM (Traces)
The collection and analysis of Application transactions and traces help you to get a deep understanding of what is happening within your application and how the different parts communicate to each other.

Using distributed tracing you also can have a look into the service map that will be created automatically based on the data and the service map also incorporates Elastic Machine Learning results.
![Elastic service map](/images/service-map.png)

### Lambda functions
Many of the modern application within the AWS ecosystem also using Lambda function. With Elastic APM its also possible to collect the traces from the Lamdba functions in additions to the CloudWatch metrics that you can collect.
The following pictures illustrates how Elastic APM integrates into your Lambda processes.
![Lambda to Elastic](/images/lambda-to-elastic.png)

