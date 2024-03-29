ICMP_TYPE = {
    0: 'Echo Reply',
    1: 'Unassigned',
    2: 'Unassigned',
    3: 'Destination Unreachable',
    4: 'Source Quench (Deprecated)',
    5: 'Redirect',
    6: 'Alternate Host Address (Deprecated)',
    7: 'Unassigned',
    8: 'Echo',
    9: 'Router Advertisement',
    10: 'Router Solicitation',
    11: 'Time Exceeded',
    12: 'Parameter Problem',
    13: 'Timestamp',
    14: 'Timestamp Reply',
    15: 'Information Request (Deprecated)',
    16: 'Information Reply (Deprecated)',
    17: 'Address Mask Request (Deprecated)',
    18: 'Address Mask Reply (Deprecated)',
    19: 'Reserved (for Security)',
    20: 'Reserved (for Robustness Experiment)',
    21: 'Reserved (for Robustness Experiment)',
    22: 'Reserved (for Robustness Experiment)',
    23: 'Reserved (for Robustness Experiment)',
    24: 'Reserved (for Robustness Experiment)',
    25: 'Reserved (for Robustness Experiment)',
    26: 'Reserved (for Robustness Experiment)',
    27: 'Reserved (for Robustness Experiment)',
    28: 'Reserved (for Robustness Experiment)',
    29: 'Reserved (for Robustness Experiment)',
    30: 'Traceroute (Deprecated)',
    31: 'Datagram Conversion Error (Deprecated)',
    32: 'Mobile Host Redirect (Deprecated)',
    33: 'IPv6 Where-Are-You (Deprecated)',
    34: 'IPv6 I-Am-Here (Deprecated)',
    35: 'Mobile Registration Request (Deprecated)',
    36: 'Mobile Registration Reply (Deprecated)',
    37: 'Domain Name Request (Deprecated)',
    38: 'Domain Name Reply (Deprecated)',
    39: 'SKIP (Deprecated)',
    40: 'Photuris',
    41: 'ICMP messages utilized by experimental mobility protocols such as Seamoby',
    42: 'Extended Echo Request',
    43: 'Extended Echo Reply',
    253: 'RFC3692-style Experiment 1',
    254: 'RFC3692-style Experiment 2',
    255: 'Reserved',
}

IP_PROTOCOL = {
    '0': 'HOPOPT',
    '1': 'ICMP',
    '2': 'IGMP',
    '3': 'GGP',
    '4': 'IPv4',
    '5': 'ST',
    '6': 'TCP',
    '7': 'CBT',
    '8': 'EGP',
    '9': 'IGP',
    '10': 'BBN-RCC-MON',
    '11': 'NVP-II',
    '12': 'PUP',
    '13': 'ARGUS (deprecated)',
    '14': 'EMCON',
    '15': 'XNET',
    '16': 'CHAOS',
    '17': 'UDP',
    '18': 'MUX',
    '19': 'DCN-MEAS',
    '20': 'HMP',
    '21': 'PRM',
    '22': 'XNS-IDP',
    '23': 'TRUNK-1',
    '24': 'TRUNK-2',
    '25': 'LEAF-1',
    '26': 'LEAF-2',
    '27': 'RDP',
    '28': 'IRTP',
    '29': 'ISO-TP4',
    '30': 'NETBLT',
    '31': 'MFE-NSP',
    '32': 'MERIT-INP',
    '33': 'DCCP',
    '34': '3PC',
    '35': 'IDPR',
    '36': 'XTP',
    '37': 'DDP',
    '38': 'IDPR-CMTP',
    '39': 'TP++',
    '40': 'IL',
    '41': 'IPv6',
    '42': 'SDRP',
    '43': 'IPv6-Route',
    '44': 'IPv6-Frag',
    '45': 'IDRP',
    '46': 'RSVP',
    '47': 'GRE',
    '48': 'DSR',
    '49': 'BNA',
    '50': 'ESP',
    '51': 'AH',
    '52': 'I-NLSP',
    '53': 'SWIPE (deprecated)',
    '54': 'NARP',
    '55': 'MOBILE',
    '56': 'TLSP',
    '57': 'SKIP',
    '58': 'IPv6-ICMP',
    '59': 'IPv6-NoNxt',
    '60': 'IPv6-Opts',
    '61': '',
    '62': 'CFTP',
    '63': '',
    '64': 'SAT-EXPAK',
    '65': 'KRYPTOLAN',
    '66': 'RVD',
    '67': 'IPPC',
    '68': '',
    '69': 'SAT-MON',
    '70': 'VISA',
    '71': 'IPCV',
    '72': 'CPNX',
    '73': 'CPHB',
    '74': 'WSN',
    '75': 'PVP',
    '76': 'BR-SAT-MON',
    '77': 'SUN-ND',
    '78': 'WB-MON',
    '79': 'WB-EXPAK',
    '80': 'ISO-IP',
    '81': 'VMTP',
    '82': 'SECURE-VMTP',
    '83': 'VINES',
    '84': 'IPTM',
    '85': 'NSFNET-IGP',
    '86': 'DGP',
    '87': 'TCF',
    '88': 'EIGRP',
    '89': 'OSPFIGP',
    '90': 'Sprite-RPC',
    '91': 'LARP',
    '92': 'MTP',
    '93': 'AX.25',
    '94': 'IPIP',
    '95': 'MICP (deprecated)',
    '96': 'SCC-SP',
    '97': 'ETHERIP',
    '98': 'ENCAP',
    '99': '',
    '100': 'GMTP',
    '101': 'IFMP',
    '102': 'PNNI',
    '103': 'PIM',
    '104': 'ARIS',
    '105': 'SCPS',
    '106': 'QNX',
    '107': 'A/N',
    '108': 'IPComp',
    '109': 'SNP',
    '110': 'Compaq-Peer',
    '111': 'IPX-in-IP',
    '112': 'VRRP',
    '113': 'PGM',
    '114': '',
    '115': 'L2TP',
    '116': 'DDX',
    '117': 'IATP',
    '118': 'STP',
    '119': 'SRP',
    '120': 'UTI',
    '121': 'SMP',
    '122': 'SM (deprecated)',
    '123': 'PTP',
    '124': 'ISIS over IPv4',
    '125': 'FIRE',
    '126': 'CRTP',
    '127': 'CRUDP',
    '128': 'SSCOPMCE',
    '129': 'IPLT',
    '130': 'SPS',
    '131': 'PIPE',
    '132': 'SCTP',
    '133': 'FC',
    '134': 'RSVP-E2E-IGNORE',
    '135': 'Mobility Header',
    '136': 'UDPLite',
    '137': 'MPLS-in-IP',
    '138': 'manet',
    '139': 'HIP',
    '140': 'Shim6',
    '141': 'WESP',
    '142': 'ROHC',
    '143': 'Ethernet',
    '144-252': '',
    '253': '',
    '254': '',
    '255': 'Reserved',
}

STATE = {
    True: 'Enabled',
    False: 'Disabled',
}

FILTERS = {
    'current_security_level': 'currentSecurityLevel',
    'destination_interface': 'destinationInterface',
    'deployed_status': 'deployedStatus',
    'device_id': 'deviceId',
    'device_uuids': 'deviceUUIDs',
    'end_time': 'endTime',
    'fetch_zero_hitcount': 'fetchZeroHitCount',
    'fts': 'fts',
    'gid': 'gid',
    'group_by': 'groupBy',
    'ids': 'ids',
    'include_count': 'includeCount',
    'ip_address': 'ipAddress',
    'ips_policy': 'ipspolicy',
    'metric': 'metric',
    'module_ids': 'moduleIDs',
    'name': 'name',
    'name_or_value': 'nameOrValue',
    'obj_type': 'type',
    'overrides': 'overrides',
    'protocol': 'protocol',
    'port': 'port',
    'realm': 'realm',
    'rule_ids': 'ids',
    'operation': 'operation',
    'original_destination': 'originalDestination',
    'original_destination_port': 'originalDestinationPort',
    'original_source': 'originalSource',
    'original_source_port': 'originalSourcePort',
    'show_only_parents': 'showonlyparents',
    'sid': 'sid',
    'sort_by': 'sortBy',
    'source_interface': 'sourceInterface',
    'status': 'status',
    'start_time': 'startTime',
    'translated_destination': 'translatedDestination',
    'translated_destination_port': 'translatedDestinationPort',
    'translated_source': 'translatedSource',
    'translated_source_port': 'translatedSourcePort',
    'unused_only': 'unusedOnly',
    'vpn_topology_id': 'vpnTopologyId',
    'vuln_id': 'id',
}

PARAMS = {
    'above_category': 'aboveCategory',
    'category': 'category',
    'insert_after': 'insertAfter',
    'insert_before': 'insertBefore',
    'name': 'name',
    'override_target_id': 'overrideTargetId',
    'section': 'section',
    'skip_control_readiness': 'skipControlReadiness',
    'target_index': 'targetIndex',
}
