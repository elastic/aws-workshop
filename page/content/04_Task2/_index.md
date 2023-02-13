---
title: "Analyze performance issues"
weight: 50
---
## Task 2

In the second task you have to find the reason for some bad performing transactions. The performance issue becomes visible after the first task is fixed. So it may take a bit of time until you can clearly see it in the charts. It's also okay to reduce the time window of the Kibana charts to only get and see the data after the fix of task 1. 

You know that you’ve fixed the issue when there is no transaction that takes longer than a couple of milliseconds.

{{%expand "Hint | Only use this if you have no idea how to proceed." %}}

In order to find the issue you need to navigate to the APM Service of the Python App.
The Python App only has one trace to analyze. Navigate into that trace and perform the Latency correlation. Make sure that you include enough data. The best would be to have 15 min of data after you fixed the issue in task 1. However if you are quicker you can use the time picker in Kibana to only use more recent data. 

When there is enough data you will find the concrete next step to do in order to fix the performance issue.

{{% /expand%}}
