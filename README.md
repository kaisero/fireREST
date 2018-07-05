# FMC Tools
A repository of python scripts to perform some routine changes in a quicker way than FMC typically allows via GUI. This is built upon a fork from [kaisero/fireREST](https://github.com/kaisero/fireREST) with some of my own changes to the functions. The tools were also inspired by [this post by the same person](http://dependencyhell.net/2017/08/27/Automating-ACP-Bulk-Changes/).

## Requirements
Clone this repo and install the requirements for [fireREST](https://github.com/kaisero/fireREST):
``` bash
git clone https://github.com/rnwolfe/fmc-tools/fmc-tools.git
pip install -r fireREST/requirements.txt
```
Afterwards, you can use the specific tool script you want.
## update-all-rules.py
### Why
The bases for creating this script was to update all the rules in a specified access policy with inspection and logging settings.

When migrating a firewall to Firepower Threat Defense using the Firepower Management Center Migration Tool, the access rules are all converted to a pre-filter policy or an access policy depending on your selection. If you select access policy, the rules don't get any inspection or logging settings. Afterwards, you'd have to manually go in and update each rule which is not scalable for large rulesets.

This tool allows you to specify *already configured* intrusion policies, file policies, variable sets, and syslog alert objects as well as define when to log the connection (at beginning and/or end) and whether to log connection events to the FMC log viewer.
### Usage
#### FMC Details
In this script, just update the top of file variables with your FMC information. The domain is normally `Global` in most cases: 
```python
device = 'fmc.domain.com'
username = 'api-user'
password = 'api-password'
domain = 'Global'
```
#### Define Inspection and Logging Settings
Then specify the objects you want to apply to the rules, as well as the settings for the logging.
```python
# Inspection settings
#  Leave variable empty (var = '') if you don't want to include the setting
intrusion_policy = 'api-intrusion-policy'
file_policy = 'api-file-policy'
variable_set = 'api-variable-set'

# Logging settings
#  Leave variable empty (var = '') if you don't want to include the setting
syslog_to_server = 'api-syslog-server'
log_to_fmc = 'true'
log_at_begin = 'false'
log_at_end = 'true'
```

### Execution
```bash
(fire) [rwolfe@devbox bulk-rule-update]$ python update-intrusion-policy.py
--------------------------------------------------------------------------------
Domain: e276abec-e0f2-11e3-8169-6d9ed49b625f
--------------------------------------------------------------------------------
Access control policy: api-test-policy: 0050568C-D66C-0ed3-0000-171798708124
 Intrusion policy: api-intrusion-policy: 0ce70864-7eeb-11e8-8f7e-9ede74934a97
 File policy: api-file-policy: f0781542-7f03-11e8-8f7e-9ede74934a97
 Log server: api-syslog-server: 573468de-7f05-11e8-971f-b0981aec49c1
 Log at beginning: false
 Log at end: true
--------------------------------------------------------------------------------
Rule: test rule 1, in Policy: api-test-policy.
  Log to FMC already set to true, or not specified. Skipping sending logs to FMC.
  Sending updated rule configuration...
 [SUCCESS]
Rule: test rule 2, in Policy: api-test-policy.
  Log to FMC already set to true, or not specified. Skipping sending logs to FMC.
  Sending updated rule configuration...
 [SUCCESS]
Rule: test rule 3, in Policy: api-test-policy.
  Log to FMC already set to true, or not specified. Skipping sending logs to FMC.
  Sending updated rule configuration...
 [SUCCESS]
(fire) [rwolfe@devbox bulk-rule-update]$
```

#### Results in GUI
##### Before
![before](https://imgur.com/ELof6xB.png)

##### After
![after](https://imgur.com/Hk9Vzof.png)
