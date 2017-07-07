import logging
import sys
import time

from rainbow_logging_handler import RainbowLoggingHandler

from lib.firepowerREST.fireREST import FireREST


class FirePOWER(object):
    def __init__(self, device=None, username=None, password=None, verify_cert=False, domain='Global', loglevel=20):
        self.logger = logging.getLogger('FIREPOWER')
        self.logger.setLevel(loglevel)
        formatter = logging.Formatter('%(asctime)s [%(name)s] [%(levelname)s] %(message)s')
        handler = RainbowLoggingHandler(sys.stderr, color_funcName=('black', 'yellow', True))
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

        self.api = FireREST(device=device, username=username, password=password, verify_cert=verify_cert,
                            loglevel=loglevel)
        self.domain = domain

    def get_network_objects(self):
        """
        Get list of firepower network objects via REST interface
        :return: network objects [list]
        """
        network_objects = list()
        responses = self.api.get_objects('network', expanded=True, domain=self.domain)
        for response in responses:
            payload = response.json()
            if response.status_code == 200:
                if 'items' in payload:
                    network_objects.extend(payload['items'])
                else:
                    self.logger.error('Payload does not include items. Do network objects exist?')
                    self.logger.debug('Payload: %s' % payload)
            else:
                self.logger.error('Error in payload. Status Code: %s' % response.status_code)
                self.logger.debug('Payload: %s' % payload)
        return network_objects

    def get_host_objects(self):
        """
        Get list of firepower host objects via REST interface
        :return: host objects [list]
        """
        host_objects = list()
        responses = self.api.get_objects('host', expanded=True, domain=self.domain)
        for response in responses:
            payload = response.json()
            if response.status_code == 200:
                if 'items' in payload:
                    host_objects.extend(payload['items'])
                else:
                    self.logger.error('Payload does not include items. Do host objects exist?')
                    self.logger.debug('Payload: %s' % payload)
            else:
                self.logger.error('Error in payload. Status Code: %s' % response.status_code)
                self.logger.debug('Payload: %s' % payload)
        return host_objects

    def get_range_objects(self):
        """
        Get list of firepower range objects via REST interface
        :return: range objects [list]
        """
        range_objects = list()
        responses = self.api.get_objects('range', expanded=True, domain=self.domain)
        for response in responses:
            payload = response.json()
            if response.status_code == 200:
                if 'items' in payload:
                    range_objects.extend(payload['items'])
                else:
                    self.logger.error('Payload does not include items. Do range objects exist?')
                    self.logger.debug('Payload: %s' % payload)
            else:
                self.logger.error('Error in payload. Status Code: %s' % response.status_code)
                self.logger.debug('Payload: %s' % payload)
        return range_objects

    def get_networkgroup_objects(self):
        """
        Get list of firepower networkgroup objects via REST interface
        :return: networkgroup objects [list]
        """
        networkgroup_objects = list()
        responses = self.api.get_objects('networkgroup', expanded=True, domain=self.domain)
        for response in responses:
            payload = response.json()
            if response.status_code == 200:
                if 'items' in payload:
                    networkgroup_objects.extend(payload['items'])
                else:
                    self.logger.error('Payload does not include items. Do networkgroup objects exist?')
                    self.logger.debug('Payload: %s' % payload)
            else:
                self.logger.error('Error in payload. Status Code: %s' % response.status_code)
                self.logger.debug('Payload: %s' % payload)
        return networkgroup_objects

    def get_protocolport_objects(self):
        """
        Get list of firepower protocolport objects via REST interface
        :return: protocolport objects [list]
        """
        protocol_objects = list()
        responses = self.api.get_objects('protocolportobject', expanded=True, domain=self.domain)
        for response in responses:
            payload = response.json()
            if response.status_code == 200:
                if 'items' in payload:
                    protocol_objects.extend(payload['items'])
                else:
                    self.logger.error('Payload does not include items. Do protocol objects exist?')
                    self.logger.debug('Payload: %s' % payload)
            else:
                self.logger.error('Error in payload. Status Code: %s' % response.status_code)
                self.logger.debug('Payload: %s' % payload)
        return protocol_objects

    def get_icmp_objects(self):
        """
        Get list of firepower icmpv4 objects via REST interface
        :return: icmpv4 objects [list]
        """
        icmp_objects = list()
        responses = self.api.get_objects('icmpv4object', expanded=False, domain=self.domain)
        for response in responses:
            payload = response.json()
            if response.status_code == 200:
                if 'items' in payload:
                    icmp_objects.extend(payload['items'])
                else:
                    self.logger.error('Payload does not include items. Do icmpv4object objects exist?')
                    self.logger.debug('Payload: %s' % payload)
            else:
                self.logger.error('Error in payload. Status Code: %s' % response.status_code)
                self.logger.debug('Payload: %s' % payload)
        return icmp_objects

    def get_portobjectgroup_objects(self):
        """
        Get list of firepower portobjectgroup objects via REST interface
        :return: portobjectgroup objects [list]
        """
        portobjectgroup_objects = list()
        responses = self.api.get_objects('portobjectgroup', expanded=True, domain=self.domain)
        for response in responses:
            payload = response.json()
            if response.status_code == 200:
                if 'items' in payload:
                    portobjectgroup_objects.extend(payload['items'])
                else:
                    self.logger.error('Payload does not include items. Do portobjectgroup objects exist?')
                    self.logger.debug('Payload: %s' % payload)
            else:
                self.logger.error('Error in payload. Status Code: %s' % response.status_code)
                self.logger.debug('Payload: %s' % payload)
        return portobjectgroup_objects

    def get_acp_rules(self, policy_name):
        """
        Get access-control-policy rules via FP REST API Interface
        :param:policy_name: name of access-control-policy
        :return: list of access-control-policy rules used in specified policy
        """
        policy_id = self.api.get_acp_id_by_name(policy_name, domain=self.domain)
        policy_rules = list()
        responses = self.api.get_acp_rules(policy_id, expanded=True, domain=self.domain)
        for response in responses:
            payload = response.json()
            if response.status_code == 200:
                if 'items' in payload:
                    policy_rules.extend(payload['items'])
                else:
                    self.logger.error('Payload does not include items. Do rules exist in access-conrol-policy?')
                    self.logger.debug('Payload: %s' % payload)
            else:
                self.logger.error('Error in payload. Status Code: %s' % response.status_code)
                self.logger.debug('Payload: %s' % payload)
        return policy_rules

    def import_network_objects(self, network_objects, type):
        """
        import network objects via firepower rest api
        :param network_objects: list of network objects to import
        :return: None
        """
        network_objects = self.normalize_network_objects(network_objects, type)
        for index, network_object in enumerate(network_objects):
            if network_object['type'].lower() == 'network':
                if index % 50 == 0:
                    time.sleep(5)
                    self.logger.info('Sleep for 5sec. API cannot handle too many subsequent requests.')
                self.api.create_object('network', network_object, domain=self.domain)
            else:
                self.logger.debug('Import of Network Object %s skipped, Type is invalid: %s' % (
                    network_object['name'], network_object['type']))

    def import_host_objects(self, host_objects, type):
        """
        import host objects via firepower rest api
        :param host_objects: list of host objects to import
        :return: None
        """
        host_objects = self.normalize_host_objects(host_objects, type)
        for index, host_object in enumerate(host_objects):
            if host_object['type'].lower() == 'host':
                if index % 50 == 0:
                    time.sleep(5)
                    self.logger.info('Sleep for 5sec. API cannot handle too many subsequent requests.')
                self.api.create_object('host', host_object, domain=self.domain)
            else:
                self.logger.debug('Import of Host Object %s skipped, Type is invalid: %s' % (
                    host_object['name'], host_object['type']))

    def import_range_objects(self, range_objects, type):
        """
        import range objects via firepower rest api
        :param range_objects: list of range objects to import
        :return: None
        """
        range_objects = self.normalize_range_objects(range_objects, type)
        for index, range_object in enumerate(range_objects):
            if range_object['type'].lower() == 'range':
                if index % 50 == 0:
                    time.sleep(5)
                    self.logger.info('Sleep for 5sec. API cannot handle too many subsequent requests.')
                self.api.create_object('range', range_object, domain=self.domain)
            else:
                self.logger.debug('Import of Range Object %s skipped, Type is invalid: %s' % (
                    range_object['name'], range_object['type']))

    def import_networkgroup_objects(self, networkgroup_objects, type):
        """
        import networkgroup objects via firepower rest api
        :param networkgroup_objects: list of networkgroup objects to import
        :param type: type of firewall objects come from
        :return: None
        """
        networkgroup_objects = self.normalize_networkgroup_objects(networkgroup_objects, type)
        for index, networkgroup_object in enumerate(networkgroup_objects):
            if networkgroup_object['type'].lower() == 'networkgroup':
                if index % 50 == 0:
                    time.sleep(5)
                    self.logger.info('Sleep for 5sec. API cannot handle too many subsequent requests.')
                self.api.create_object('networkgroup', networkgroup_object, domain=self.domain)
            else:
                self.logger.debug('Import of NetworkGroup Object %s skipped, Type is invalid: %s' % (
                    networkgroup_object['name'], networkgroup_object['type']))

    def import_protocolport_objects(self, protocolport_objects):
        """
        import protocolport objects via firepower rest api
        :param protocolport_objects: list of protocolport objects to import
        :return: None
        """
        for index, protocolport_object in enumerate(protocolport_objects):
            if protocolport_object['type'].lower() == 'protocolportobject':
                if index % 50 == 0:
                    time.sleep(5)
                    self.logger.info('Sleep for 5sec. API cannot handle too many subsequent requests.')
                self.api.create_object('protocolportobject', protocolport_object, domain=self.domain)
            else:
                self.logger.info('Import of ProtocolPort Object %s skipped, Type is invalid: %s' % (
                    protocolport_object['name'], protocolport_object['type']))

    def import_icmp_objects(self, icmp_objects):
        """
        import icmpv4 objects via firepower rest api
        :param icmp_objects: list of icmpv4 objects to import
        :return: None
        """
        for index, icmp_object in enumerate(icmp_objects):
            if icmp_object['type'].lower() == 'icmpv4object':
                if index % 50 == 0:
                    time.sleep(5)
                    self.logger.critical('Sleep for 5sec. API cannot handle too many subsequent requests.')
                self.api.create_object('icmpv4object', icmp_object, domain=self.domain)
            else:
                self.logger.debug('Import of ICMPv4 Object %s skipped, Type is invalid: %s' % (
                    icmp_object['name'], icmp_object['type']))

    def import_protocolportgroup_objects(self, protocolportgroup_objects, type):
        """
        import protocolportgroup objects via firepower rest api
        :param protocolportgroup_objects: list of protocolportgroup objects to import
        :param type: type of firewall objects come from
        :return: None
        """
        protocolportgroup_objects = self.normalize_portgroup_objects(protocolportgroup_objects, type)
        for index, protocolportgroup_object in enumerate(protocolportgroup_objects):
            if protocolportgroup_object['type'].lower() == 'portobjectgroup':
                if index % 50 == 0:
                    time.sleep(5)
                    self.logger.info('Sleep for 5sec. API cannot handle too many subsequent requests.')
                self.api.create_object('portobjectgroup', protocolportgroup_object, domain=self.domain)
            else:
                self.logger.debug('Import of ProtocolPortGroup Object %s skipped, Type is invalid: %s' % (
                    protocolportgroup_object['name'], protocolportgroup_object['type']))

    def normalize_network_objects(self, networkobjects, type):
        if type.lower() == 'asa':
            return_networkobjects = list()
            for networkobject in networkobjects:
                obj = dict()
                obj['name'] = networkobject['name']
                obj['type'] = 'Network'
                obj['value'] = networkobject['host']['value']
                return_networkobjects.append(obj)
            return return_networkobjects
        return networkobjects

    def normalize_host_objects(self, hosts, type):
        """
        Normalize host objects. Dictionary is being adapted to fit required format for import
        :param hosts: host objects from source
        :param type: type of firewall objects come from
        :return: firepower rest api compatible host objects
        """
        if type == 'asa':
            for i, v in enumerate(hosts):
                obj = dict()
                obj['name'] = v['name']
                obj['type'] = 'Host'
                obj['value'] = v['host']['value']
                hosts[i] = obj
            return hosts
        if type == 'checkpoint':
            for i, v in enumerate(hosts):
                if v['type'].lower() == 'host':
                    obj = dict()
                    obj['name'] = v['name']
                    obj['type'] = v['type']
                    obj['value'] = v['value']
                    obj['description'] = v['description']
                    hosts[i] = obj
        return hosts

    def normalize_range_objects(self, ranges, type):
        """
        Normalize range objects. Dictionary is being adapted to fit required format for import
        :param hosts: range objects from source
        :param type: type of firewall objects come from
        :return: firepower rest api compatible range objects
        """
        if type == 'asa':
            for i, v in enumerate(ranges):
                obj = dict()
                obj['name'] = v['name']
                obj['type'] = 'Range'
                obj['value'] = v['host']['value']
                ranges[i] = obj
            return ranges
        return ranges

    def normalize_networkgroup_objects(self, networkgroups, type):
        """
        Normalize networkgroup objects. Dictionary is being adapted to fit required format for import
        :param networkgroup: networkgroup objects from source
        :param type: type of firewall objects come from
        :return: firepower rest api compatible networkgroup objects
        """
        return_networkgroups = list()

        supported_object_types = [
            'network',
            'host',
            'range',
            'networkgroup',
        ]

        fp_network_objects = self.get_network_objects()
        fp_host_objects = self.get_host_objects()
        fp_range_objects = self.get_range_objects()
        fp_networkgroup_objects = self.get_networkgroup_objects()

        if type.lower() == 'asa':
            fp_objects = list()
            fp_objects.append(fp_network_objects)
            fp_objects.append(fp_host_objects)
            fp_objects.append(fp_range_objects)
            fp_objects.append(fp_networkgroup_objects)
            for index, networkgroup in enumerate(networkgroups):
                if networkgroup['members'].__len__() > 0:
                    processable = True
                    for i, v in enumerate(networkgroup['members']):
                        found = False
                        for obj in fp_objects:
                            if obj['name'] == v['name']:
                                found = True
                                obj_new = dict()
                                obj_new['id'] = obj['id']
                                networkgroup['members'][i] = obj_new
                        if not found:
                            processable = False
                            self.logger.warning(
                                'Network Group %s: Member %s not found. Network Group '
                                'will be removed from list.' % (networkgroup['name'], v['name']))
                    if processable:
                        return_networkgroups.append(networkgroup)
                else:
                    self.logger.warning('Network-Group %s has no elements, skipping' % networkgroup['name'])
                    self.logger.debug('Network-Group Dump: %s' % networkgroup)

        if type.lower() == 'checkpoint':
            for index, networkgroup in enumerate(networkgroups):
                if networkgroup['type'].lower() == 'networkgroup':
                    if 'objects' in networkgroup:
                        processable = True
                        for i, v in enumerate(networkgroup['objects']):
                            found = False
                            if 'type' in v:
                                if v['type'].lower() in supported_object_types:
                                    if v['type'].lower() == 'network':
                                        for fp_obj in fp_network_objects:
                                            if fp_obj['name'] == v['name']:
                                                network_new = dict()
                                                network_new['id'] = fp_obj['id']
                                                networkgroup['objects'][i] = network_new
                                                found = True

                                    if v['type'].lower() == 'host':
                                        for fp_obj in fp_host_objects:
                                            if fp_obj['name'] == v['name']:
                                                host_new = dict()
                                                host_new['id'] = fp_obj['id']
                                                networkgroup['objects'][i] = host_new
                                                found = True

                                    if v['type'].lower() == 'range':
                                        for fp_obj in fp_range_objects:
                                            if fp_obj['name'] == v['name']:
                                                range_new = dict()
                                                range_new['id'] = fp_obj['id']
                                                networkgroup['objects'][i] = range_new
                                                found = True

                                    if v['type'].lower() == 'networkgroup':
                                        for fp_obj in fp_networkgroup_objects:
                                            if fp_obj['name'] == v['name']:
                                                networkgroup_new = dict()
                                                networkgroup_new['id'] = fp_obj['id']
                                                networkgroup['objects'][i] = networkgroup_new
                                                found = True
                                    if not found:
                                        processable = False
                                        self.logger.warning(
                                            'Network Group %s: Member %s with Object type %s not found. Network Group '
                                            'will be removed from list.' % (networkgroup['name'], v['name'], v['type']))
                                else:
                                    self.logger.warning('Network-Group %s: Member %s Object type %s not supported' % (
                                        networkgroup['name'], v['name'], v['type']))
                            else:
                                self.logger.warning(
                                    'Network-Group %s: Member %s Type unknown, skipping' % (networkgroup['name'],
                                                                                            v['name']))
                        if processable:
                            return_networkgroups.append(networkgroup)
                    else:
                        self.logger.warning('Network-Group %s has no elements, skipping' % networkgroup['name'])
                        self.logger.debug('Network-Group Dump: %s' % networkgroup)
        return return_networkgroups

    def normalize_portgroup_objects(self, portgroups, type):
        """
        Normalize portgroup objects. Dictionary is being adapted to fit required format for import
        :param portgroups: portgroup objects from source
        :param type: type of firewall objects come from
        :return: firepower rest api compatible portgroup objects
        """

        return_portgroups = list()

        supported_object_types = [
            'protocolportobject',
            'portobjectgroup',
            # 'icmpv4object' | bug in fmc api, expanded=True will lead to error for icmpv4objects
        ]

        fp_protocolport_objects = self.get_protocolport_objects()
        fp_icmp_objects = self.get_icmp_objects()
        fp_portobjectgroup_objects = self.get_portobjectgroup_objects()

        if type.lower() == 'checkpoint':
            for index, portobject_group in enumerate(portgroups):
                if portobject_group['type'].lower() == 'portobjectgroup':
                    if 'objects' in portobject_group:
                        processable = True
                        for i, v in enumerate(portobject_group['objects']):
                            found = False
                            if 'type' in v:
                                if v['type'].lower() in supported_object_types:
                                    if v['type'].lower() == 'protocolportobject':
                                        for fp_obj in fp_protocolport_objects:
                                            if fp_obj['name'].lower() == v['name'].lower():
                                                protocolport_new = dict()
                                                protocolport_new['id'] = fp_obj['id']
                                                protocolport_new['name'] = fp_obj['name']
                                                protocolport_new['type'] = fp_obj['type']
                                                portobject_group['objects'][i] = protocolport_new
                                                found = True

                                    if v['type'].lower() == 'icmpv4object':
                                        for fp_obj in fp_icmp_objects:
                                            if fp_obj['name'].lower() == v['name'].lower():
                                                icmp_new = dict()
                                                icmp_new['id'] = fp_obj['id']
                                                icmp_new['name'] = fp_obj['name']
                                                icmp_new['type'] = fp_obj['type']
                                                portobject_group['objects'][i] = icmp_new
                                                found = True

                                    if v['type'].lower() == 'portobjectgroup':
                                        for fp_obj in fp_portobjectgroup_objects:
                                            if fp_obj['name'].lower() == v['name'].lower():
                                                portobjectgroup_new = dict()
                                                portobjectgroup_new['id'] = fp_obj['id']
                                                portobjectgroup_new['type'] = fp_obj['type']
                                                portobjectgroup_new['name'] = fp_obj['name']
                                                portobject_group['objects'][i] = portobjectgroup_new
                                                found = True
                                    if not found:
                                        processable = False
                                        self.logger.warning(
                                            'PortObject-Group %s: Member %s with Object type %s not found. PortObject-Group '
                                            'will be removed from list.' % (
                                                portobject_group['name'], v['name'], v['type']))
                                else:
                                    processable = False
                                    self.logger.warning(
                                        'PortObject-Group %s: Member %s Object type %s not supported' % (
                                            portobject_group['name'], v['name'], v['type']))
                            else:
                                processable = False
                                self.logger.warning(
                                    'PortObject-Group %s: Member %s Type unknown, skipping' % (portobject_group['name'],
                                                                                               v['name']))
                        if processable:
                            return_portgroups.append(portobject_group)
                    else:
                        self.logger.warning('PortObject-Group %s has no elements, skipping' % portobject_group['name'])
                        self.logger.debug('PortObject-Group Dump: %s' % portobject_group)
        return return_portgroups
