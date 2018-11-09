# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class RecordCreateRequest(Request):

    def __init__(self):
        super(RecordCreateRequest, self).__init__(
            'cns', 'qcloudcliV1', 'RecordCreate', 'cns.api.qcloud.com')

    def get_domain(self):
        return self.get_params().get('domain')

    def set_domain(self, domain):
        self.add_param('domain', domain)

    def get_subDomain(self):
        return self.get_params().get('subDomain')

    def set_subDomain(self, subDomain):
        self.add_param('subDomain', subDomain)

    def get_recordType(self):
        return self.get_params().get('recordType')

    def set_recordType(self, recordType):
        self.add_param('recordType', recordType)

    def get_recordLine(self):
        return self.get_params().get('recordLine')

    def set_recordLine(self, recordLine):
        self.add_param('recordLine', recordLine)

    def get_value(self):
        return self.get_params().get('value')

    def set_value(self, value):
        self.add_param('value', value)

    def get_ttl(self):
        return self.get_params().get('ttl')

    def set_ttl(self, ttl):
        self.add_param('ttl', ttl)

    def get_mx(self):
        return self.get_params().get('mx')

    def set_mx(self, mx):
        self.add_param('mx', mx)

