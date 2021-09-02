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

class InventoryItemAPI(object):

    def list_inventory_items(self, *args, **kwargs):
        url = self.base_url + "admin/inventory_items.json"
        contents = self.get(url, **kwargs)
        return contents["inventory_items"]

    def get_inventory_item(self, id):
        url = self.base_url + "admin/inventory_items/%d.json" % id
        contents = self.get(url)
        return contents["inventory_item"]

    def update_inventory_item(self, id, inventory_item):
        url = self.base_url + "admin/inventory_items/%d.json" % id
        contents = self.put(url, data_j = dict(inventory_item = inventory_item))
        return contents["inventory_item"]
