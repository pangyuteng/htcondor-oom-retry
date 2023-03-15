


tldr if GPUS are occupied, condor will stil submit a job to the host!!

so you should let condor know node is occupied per below post.


https://www-auth.cs.wisc.edu/lists/htcondor-users/2021-March/msg00177.shtml
```
On 3/12/2021 9:17 AM, ervikrant06@xxxxxxxxx wrote:
Worker nodes accept the jobs if the START condition evaluates to True, start should evaluate False for node(s) to not accept new jobs, existing jobs will keep on running.

START = False

condor_reconfig (to reflect the change)

From condor master node for multiple worker nodes you may use this:

condor_config_val -set 'START = False' -startd -name $host
condor_reconfig -name $host

```