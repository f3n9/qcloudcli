# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeLocalDestinationIPPortTranslationNatRuleRequest(Request):

    def __init__(self):
        super(DescribeLocalDestinationIPPortTranslationNatRuleRequest, self).__init__(
            'vpc', 'qcloudcliV1', 'DescribeLocalDestinationIPPortTranslationNatRule', 'vpc.api.qcloud.com')

    def get_description(self):
        return self.get_params().get('description')

    def set_description(self, description):
        self.add_param('description', description)

    def get_directConnectGatewayId(self):
        return self.get_params().get('directConnectGatewayId')

    def set_directConnectGatewayId(self, directConnectGatewayId):
        self.add_param('directConnectGatewayId', directConnectGatewayId)

    def get_limit(self):
        return self.get_params().get('limit')

    def set_limit(self, limit):
        self.add_param('limit', limit)

    def get_offset(self):
        return self.get_params().get('offset')

    def set_offset(self, offset):
        self.add_param('offset', offset)

    def get_originalIP(self):
        return self.get_params().get('originalIP')

    def set_originalIP(self, originalIP):
        self.add_param('originalIP', originalIP)

    def get_originalPORT(self):
        return self.get_params().get('originalPORT')

    def set_originalPORT(self, originalPORT):
        self.add_param('originalPORT', originalPORT)

    def get_proto(self):
        return self.get_params().get('proto')

    def set_proto(self, proto):
        self.add_param('proto', proto)

    def get_translationIP(self):
        return self.get_params().get('translationIP')

    def set_translationIP(self, translationIP):
        self.add_param('translationIP', translationIP)

    def get_translationPORT(self):
        return self.get_params().get('translationPORT')

    def set_translationPORT(self, translationPORT):
        self.add_param('translationPORT', translationPORT)

    def get_vpcId(self):
        return self.get_params().get('vpcId')

    def set_vpcId(self, vpcId):
        self.add_param('vpcId', vpcId)
