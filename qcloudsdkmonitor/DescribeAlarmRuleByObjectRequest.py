# -*- coding: utf-8 -*-

from qcloudsdkcore.request import Request

class DescribeAlarmRuleByObjectRequest(Request):

    def __init__(self):
        super(DescribeAlarmRuleByObjectRequest, self).__init__(
            'monitor', 'qcloudcliV1', 'DescribeAlarmRuleByObject', 'monitor.api.qcloud.com')

    def get_dimensions(self):
        return self.get_params().get('dimensions')

    def set_dimensions(self, dimensions):
        self.add_param('dimensions', dimensions)

    def get_limit(self):
        return self.get_params().get('limit')

    def set_limit(self, limit):
        self.add_param('limit', limit)

    def get_metricName(self):
        return self.get_params().get('metricName')

    def set_metricName(self, metricName):
        self.add_param('metricName', metricName)

    def get_offset(self):
        return self.get_params().get('offset')

    def set_offset(self, offset):
        self.add_param('offset', offset)
