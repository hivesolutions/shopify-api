#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Shopify API
# Copyright (c) 2008-2020 Hive Solutions Lda.
#
# This file is part of Hive Shopify API.
#
# Hive Shopify API is free software: you can redistribute it and/or modify
# it under the terms of the Apache License as published by the Apache
# Foundation, either version 2.0 of the License, or (at your option) any
# later version.
#
# Hive Shopify API is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# Apache License for more details.
#
# You should have received a copy of the Apache License along with
# Hive Shopify API. If not, see <http://www.apache.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2020 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

class WebhookAPI(object):

    def list_webhooks(self, *args, **kwargs):
        url = self.admin_url + "webhooks.json"
        contents = self.get(url, **kwargs)
        return contents["webhooks"]

    def create_webhook(self, webhook):
        url = self.admin_url + "webhooks.json"
        contents = self.post(url, data_j = dict(webhook = webhook))
        return contents["webhook"]

    def get_webhook(self, id):
        url = self.admin_url + "webhooks/%d.json" % id
        contents = self.get(url)
        return contents["webhook"]

    def update_webhook(self, id, webhook):
        url = self.admin_url + "webhooks/%d.json" % id
        contents = self.put(url, data_j = dict(webhook = webhook))
        return contents["webhook"]

    def delete_webhook(self, id):
        url = self.admin_url + "webhooks/%d.json" % id
        self.delete(url)
