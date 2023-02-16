---
title: "AIOps Log Spike analysis"
weight: 60
pre: "<b>2.c </b>"
---
## Task 3

In the third task you have to find the reason for some anomalous log spikes. Every now and then the application is logging much more than usual. From a technical perspective there is no obvious reason for it, e.g. no cron job running.

![Start Task 3](/images/task3-start.png)

{{%expand "Hint | Only use this if you have no idea how to proceed." %}}
### Hint

Within the Machine Learning menu in Kibana you can find "Explain Log Rate Spikes". Use this with the Python Logs saved search. Make sure that you set Deviation and Baseline based on your needs.

{{% /expand%}}

{{%expand "Solution | Open here if you think you found the issue and want to check your result." %}}
### Solution

The expected finding is the user named hack0r, that tries to get enrichment data from the data base.
![Solution Task 3](/images/task3-solution.png)

After finding the result it would be a good idea to create a case about it. IT Security will take care from that point.
You can do this under Observability -> Cases

{{% /expand%}}

### After task 3
When you've found the issue. Think about what you should do with that information to make sure its handled appropriatly.

