# import required dependencies
from __future__ import print_function
from fireREST import FireREST

# Set variables for execution.
# Make sure your credentials are correct.
device = '10.12.100.36'
username = 'api-user'
password = 'api-password'
# With child domain (note the spacing):
# domain = 'Global/ NAME-OF-CHILD'
domain = 'Global'
ac_policy = 'api-test-policy'

policyFile = open(ac_policy + ".csv", "w")

# Initialize a new api object
api = FireREST(hostname=device, username=username, password=password)

# Get IDs for specified objects. API PK = UUID, so we have to find the matching api object for the name specified.
if ac_policy:
    acp_id = api.get_acp_id_by_name(ac_policy)
else:
    acp_id = "Not defined"

print("-" * 85)
print("Domain: " + api.get_domain_id(domain))
print("-" * 85)
print("Access control policy: {0}: {1}".format(ac_policy, acp_id))
print("-" * 85)

# Write CSV Header
policyFile.write("#, name, enabled, action, sourceZones, destZones, sourceNetworks, destNetworks, sourcePorts, "
                 "destPorts, ipsPolicy, variableSet, filePolicy, logBegin, logEnd, sendEventsToFMC, syslogConfig\n")

# Get all access control rules for the access control policy specified
acp_rules = api.get_acp_rules(acp_id, expanded=True)

# Loop through HTTP response objects
for response in acp_rules:
    # Loop through access control rules in http response object
    for rule in response.json()['items']:
        # Initialize empty line dictionary
        line = {}

        # Build dictionary of rule info
        # Start with keys that always exist
        line['ruleNum'] = rule['metadata']['ruleIndex']
        line['name'] = rule['name']
        line['enabled'] = rule['enabled']
        line['action'] = rule['action']
        line['logBegin'] = rule['logBegin']
        line['logEnd'] = rule['logEnd']
        line['sendEventsToFMC'] = rule['sendEventsToFMC']

        # Then handle getting keys that might not exist
        # Starting with items that may have multiple objects
        # Source Zones
        line['sourceZones'] = []
        try:
            for item in rule['sourceZones']['objects']:
                # Put each object in a list, will join to str when printing to CSV
                line['sourceZones'].append(item['name'])
        except KeyError:
            line['sourceZones'] = ['any']

        # Destination Zones
        line['destZones'] = []
        try:
            for item in rule['destinationZones']['objects']:
                # Put each object in a list, will join to str when printing to CSV
                line['destZones'].append(item['name'])
        except KeyError:
            line['destZones'] = ['any']

        # Source Networks
        line['sourceNetworks'] = []
        try:
            for item in rule['sourceNetworks']['objects']:
                # Put each object in a list, will join to str when printing to CSV
                line['sourceNetworks'].append(item['name'])
        except KeyError:
            line['sourceNetworks'] = ['any']

        # Destination Networks
        line['destNetworks'] = []
        try:
            for item in rule['destinationNetworks']['objects']:
                # Put each object in a list, will join to str when printing to CSV
                line['destNetworks'].append(item['name'])
        except KeyError:
            line['destNetworks'] = ['any']

        # Source Ports
        line['sourcePorts'] = []
        try:
            for item in rule['sourcePorts']['objects']:
                # Put each object in a list, will join to str when printing to CSV
                line['sourcePorts'].append(item['name'])
        except KeyError:
            line['sourcePorts'] = ['any']

        # Destination Ports
        line['destPorts'] = []
        try:
            for item in rule['destinationPorts']['objects']:
                # Put each object in a list, will join to str when printing to CSV
                line['destPorts'] = [item['name']]
        except KeyError:
            line['destPorts'] = ['any']

        # Now get items that may not exist, but can only have one value
        # ipsPolicy
        try:
            line['ipsPolicy'] = rule['ipsPolicy']['name']
        except KeyError:
            line['ipsPolicy'] = 'none'

        # variableSet
        try:
            line['variableSet'] = rule['variableSet']['name']
        except KeyError:
            line['variableSet'] = 'none'

        # filePolicy
        try:
            line['filePolicy'] = rule['filePolicy']['name']
        except KeyError:
            line['filePolicy'] = 'none'

        # syslogConfig
        try:
            line['syslogConfig'] = rule['syslogConfig']['name']
        except KeyError:
            line['syslogConfig'] = 'none'

        # Print status to stdout
        print("Writing rule #{0} to CSV...".format(line['ruleNum']))

        # Write rule to line in policyFile
        policyFile.write("{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}\n"
                         .format(line['ruleNum'], line['name'], line['enabled'], line['action'],
                                 ';'.join(line['sourceZones']), ';'.join(line['destZones']),
                                 ';'.join(line['sourceNetworks']), ';'.join(line['destNetworks']),
                                 ';'.join(line['sourcePorts']), ';'.join(line['destPorts']), line['ipsPolicy'],
                                 line['variableSet'], line['filePolicy'], line['logBegin'], line['logEnd'],
                                 line['sendEventsToFMC'], line['syslogConfig']))
policyFile.close()
print("File is at: ./{0}.csv".format(ac_policy))
