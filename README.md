# FMC Tools
A repository of python scripts to perform some routine changes in a quicker way than FMC typically allows via GUI. This is built upon a fork from [kaisero/fireREST](https://github.com/kaisero/fireREST) with some of my own changes to the functions. The tools were also inspired by [this post by the same person](http://dependencyhell.net/2017/08/27/Automating-ACP-Bulk-Changes/).

## Requirements
Clone this repo and install the requirements for [fireREST](https://github.com/kaisero/fireREST):
``` bash
git clone https://github.com/rnwolfe/fmc-tools/fmc-tools.git
pip install -r fireREST/requirements.txt
```
Afterwards, you can use the specific tool script you want.

## Table of Contents
1. [export-acp-to-csv.py](#export-acp-to-csvpy)
2. [update-all-rules.py](#update-all-rulespy)
## export-acp-to-csv.py
### Why
The basis for this script was to export all of the rules in a specific access policy to a CSV spreadsheet for use in analyzing the ruleset for consolidation, optimization, or otherwise. It could also be used as a form of version control / comparison over time. For example, this script could be run as a cron job and a diff run on two different iterations of the policy for troubleshooting purposes.
### Usage
#### FMC Details
In this script, just update the top of file variables with your FMC information and the access policy name you wish to export. The domain is normally `Global` in most cases:
```python
device = 'fmc.domain.com'
username = 'api-user'
password = 'api-password'
# With child domain (note the spacing):
# domain = 'Global/ NAME-OF-CHILD'
domain = 'Global'
ac_policy = 'api-test-policy'
```

**Note**: If using a child domain, add a `/ ` (note the space after the slash) between parent/child, e.g. `Global/ Child-Domain`. This is due to how the domains are formatted by the FMC

### Execution
```bash
$ python export-acp-to-csv.py
-------------------------------------------------------------------------------------
Domain: e276abec-e0f2-11e3-8169-6d9ed49b625f
-------------------------------------------------------------------------------------
Access control policy: api-test-policy: 0050568C-D66C-0ed3-0000-171798708124
-------------------------------------------------------------------------------------
Writing rule #1 to CSV...
Writing rule #2 to CSV...
Writing rule #3 to CSV...
Writing rule #4 to CSV...
Writing rule #5 to CSV...
File is at: ./api-test-policy.csv
```

#### Example Results
Please see [example CSV output file here](https://github.com/rnwolfe/fmc-tools/blob/master/api-test-policy.csv).
## update-all-rules.py
### Why
The basis for creating this script was to update all the rules in a specified access policy with inspection and logging settings.

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
ac_policy = 'api-test-policy'
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
$ python update-all-rules.py
-------------------------------------------------------------------------------------
Domain: e276abec-e0f2-11e3-8169-6d9ed49b625f
-------------------------------------------------------------------------------------
Access control policy: api-test-policy: 0050568C-D66C-0ed3-0000-171798708124
 Intrusion policy: api-intrusion-policy: 0ce70864-7eeb-11e8-8f7e-9ede74934a97
 File policy: api-file-policy: f0781542-7f03-11e8-8f7e-9ede74934a97
 Variable Set: api-variable-set: e1658ab2-7f03-11e8-8f7e-9ede74934a97
 Log server: api-syslog-server: 573468de-7f05-11e8-971f-b0981aec49c1
 Log to event viewer: true
 Log at beginning: false
 Log at end: true
-------------------------------------------------------------------------------------
Rule: test rule 1, in Policy: api-test-policy.
  Syslog configuration already exists, or not specified. Skipping syslog config.
  Intrusion Policy configuration already exists, or not specified. Skipping intrusion policy.
  File Policy configuration already exists, or not specified. Skipping file policy configuration.
  Variable Set configuration already exists, or not specified. Skipping variable set.
  Sending updated rule configuration...
 [SUCCESS]
Rule: test rule 2, in Policy: api-test-policy.
  Syslog configuration already exists, or not specified. Skipping syslog config.
  Intrusion Policy configuration already exists, or not specified. Skipping intrusion policy.
  File Policy configuration already exists, or not specified. Skipping file policy configuration.
  Variable Set configuration already exists, or not specified. Skipping variable set.
  Sending updated rule configuration...
 [SUCCESS]
Rule: test rule 3, in Policy: api-test-policy.
  Syslog configuration already exists, or not specified. Skipping syslog config.
  Intrusion Policy configuration already exists, or not specified. Skipping intrusion policy.
  File Policy configuration already exists, or not specified. Skipping file policy configuration.
  Variable Set configuration already exists, or not specified. Skipping variable set.
  Sending updated rule configuration...
 [SUCCESS]
Rule: test rule 4, in Policy: api-test-policy.
  Syslog configuration already exists, or not specified. Skipping syslog config.
  Rule not set to ALLOW, clearing intrusion settings. Overwriting log settings with log at beginning and send to event viewer.
  Sending updated rule configuration...
 [SUCCESS]
Rule: test rule 5, in Policy: api-test-policy.
  Variable Set configuration already exists, or not specified. Skipping variable set.
  Sending updated rule configuration...
 [SUCCESS]
```

#### Example Results in GUI
##### Before
![before](https://imgur.com/ELof6xB.png)

##### After
![after](https://imgur.com/Hk9Vzof.png)
