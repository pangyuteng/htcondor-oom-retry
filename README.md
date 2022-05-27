
```

htcondor-oom-retry


https://www-auth.cs.wisc.edu/lists/htcondor-users/2022-March/msg00012.shtml

testing out above h/t mm


```


sample log proving retrying mechanism works:

```
...
006 (2456301.000.000) 2022-05-27 10:08:57 Image size of job updated: 1223
	1223  -  MemoryUsage of job (MB)
	1252748  -  ResidentSetSize of job (KB)
...
006 (2456301.000.000) 2022-05-27 10:13:57 Image size of job updated: 8034
	8034  -  MemoryUsage of job (MB)
	8227760  -  ResidentSetSize of job (KB)
...
007 (2456301.000.000) 2022-05-27 10:37:20 Shadow exception!
	Error from xxx@xxx.xxx.xxx: Docker job has gone over memory limit of 8055 Mb
	0  -  Run Bytes Sent By Job
	163  -  Run Bytes Received By Job
...
012 (2456301.000.000) 2022-05-27 10:37:20 Job was held.
	Error from xxx@xxx.xxx.xxx: Docker job has gone over memory limit of 8055 Mb
	Code 34 Subcode 0
...
013 (2456301.000.000) 2022-05-27 10:37:21 Job was released.
	The job attribute PeriodicRelease expression '(JobStatus == 5) && (HoldReasonCode == 34) && (NumJobStarts < 5)' evaluated to TRUE
...
040 (2456301.000.000) 2022-05-27 10:37:45 Started transferring input files
	Transferring to host: <xxx.xxx.xxx:9618?addrs=xxx.xxx.xxx-9618&alias=xxx.xxx.xxx&noUDP&sock=slot15_4029_8b7d_3450>
...
040 (2456301.000.000) 2022-05-27 10:37:45 Finished transferring input files
...
001 (2456301.000.000) 2022-05-27 10:37:46 Job executing on host: <xxx.xxx.xxx:9618?addrs=xxx.xxx.xxx-9618&alias=xxx.xxx.xxx&noUDP&sock=startd_2952_67aa>
...
006 (2456301.000.000) 2022-05-27 10:43:09 Image size of job updated: 19497
	19497  -  MemoryUsage of job (MB)
	19965156  -  ResidentSetSize of job (KB)
...

```