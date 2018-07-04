# import required dependencies
from __future__ import print_function
from fireREST import FireREST

# Set variables for execution.
# Make sure your credentials are correct.
# Make sure ACP and all logging and inspection objects already exist.

loglevel = 'DEBUG'
device = '10.12.100.34'
username = 'api-user'
password = 'Ir0n1234!@#$'
domain = 'Global'
ac_policy = 'api-test-policy'

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

# Initialize a new api object
api = FireREST(hostname=device, username=username, password=password)

# Get IDs for specified objects. API PK = UUID, so we have to find the matching api object for the name specified.
acp_id = api.get_acp_id_by_name(ac_policy)
syslog_server_id = api.get_syslogalert_id_by_name(syslog_to_server)
intrusion_policy_id = api.get_intrusion_policy_id_by_name(intrusion_policy)
file_policy_id = api.get_file_policy_id_by_name(file_policy)
variable_set_id = api.get_variable_set_id_by_name(variable_set)


print("-" * 80)
print("Domain: " + api.get_domain_id(domain))
print("-" * 80)
print("Access control policy: {0}: {1}".format(ac_policy, acp_id))
print(" Intrusion policy: {0}: {1}".format(intrusion_policy, intrusion_policy_id))
print(" File policy: {0}: {1}".format(file_policy, file_policy_id))
print(" Log server: {0}: {1}".format(syslog_to_server, syslog_server_id))
print(" Log at beginning: {0} ".format(log_at_begin))
print(" Log at end: {0} ".format(log_at_end))
print("-" * 80)

# Get all access control rules for the access control policy specified
acp_rules = api.get_acp_rules(acp_id, expanded=True)

# Loop through HTTP response objects
for response in acp_rules:
    # Loop through access control rules in http response object
    for acp_rule in response.json()['items']:
        # Grab ACP Rule name for use in debugging
        acp_rule_name = acp_rule['name']

        # Set payload baseline as existing ACP Rule settings.
        payload = acp_rule

        # Print rule name for status messages
        print('Rule: {0}, in Policy: {1}.'.format(acp_rule_name, ac_policy))

        # Only change each setting if a configuration doesn't already exist, and a value is specified in top of file.
        if syslog_to_server and 'syslogConfig' not in acp_rule:
            # Get the existing rule configuration
            # Set syslog configuration
            payload['syslogConfig'] = {
                'id': syslog_server_id
            }
        else:
            print('  Syslog configuration already exists, or not specified. Skipping syslog config.')

        if log_to_fmc and 'sendEventsToFMC' not in acp_rule and 'sendEventsToFMC' != log_to_fmc:
            payload['sendEventsToFMC'] = log_to_fmc
        else:
            print('  Log to FMC already set to {0}, or not specified. Skipping sending logs to FMC.'.format(log_to_fmc))

        if log_at_begin and ('logBegin' not in acp_rule or 'logBegin' != log_at_begin):
            payload['logBegin'] = log_at_begin
        else:
            print('  Log at beginning of connection already set, or not specified. Skipping log at beginning.')

        if log_at_end and ('logEnd' not in acp_rule or 'logEnd' != log_at_end):
            payload['logEnd'] = log_at_end
        else:
            print('  Log at end of connection not already set, or not specified. Skipping log at end.')

        if intrusion_policy and 'ipsPolicy' not in acp_rule:
            # Set IPS policy config
            payload['ipsPolicy'] = {
                "id": intrusion_policy_id
            }
        else:
            print('  Intrusion Policy configuration already exists, or not specified. Skipping intrusion policy.')

        if file_policy and 'filePolicy' not in acp_rule:
            # Set file policy configuration
            payload['filePolicy'] = {
                "id": file_policy_id
            }
        else:
            print('  File Policy configuration already exists, or not specified. Skipping file policy configuration.')

        # Remove metadata fields from existing rule. This is required since the API does not support
        # PATCH operations as of version 6.2.1 of FMC. That's why we have to delete metadata before we use a PUT
        # operation to change our ACP rule.

        del payload['metadata']
        del payload['links']

        print('  Sending updated rule configuration...')
        # print('Sent payload: ' + str(payload))

        # Send json payload to FMC REST API
        result = api.update_acp_rule(policy_id=acp_id, rule_id=acp_rule['id'], data=payload)
        # Verify that the PUT operation has been successful
        if result.status_code == 200:
            print(' [SUCCESS]'.format(acp_rule_name))
        else:
            print(' [ERROR] Could not update settings. Status code: {0}'.format(result.status_code))
