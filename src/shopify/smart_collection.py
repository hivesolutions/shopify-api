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

class SmartCollectionAPI(object):

    def list_smart_collections(self, *args, **kwargs):
        url = self.base_url + "admin/smart_collections.json"
        contents = self.get(url, **kwargs)
        return contents["smart_collections"]

    def many_smart_collections(self, *args, **kwargs):
        url = self.base_url + "admin/smart_collections.json"
        contents = self.get_many(
            url,
            key = "smart_collections",
            **kwargs
        )
        return contents["smart_collections"]

    def create_smart_collection(self, smart_collection):
        url = self.base_url + "admin/smart_collections.json"
        contents = self.post(url, data_j = dict(smart_collection = smart_collection))
        return contents["smart_collection"]

    def get_smart_collection(self, id):
        url = self.base_url + "admin/smart_collections/%d.json" % id
        contents = self.get(url)
        return contents["smart_collection"]

    def update_smart_collection(self, id, smart_collection):
        url = self.base_url + "admin/smart_collections/%d.json" % id
        contents = self.put(url, data_j = dict(smart_collection = smart_collection))
        return contents["smart_collection"]

    def delete_smart_collection(self, id):
        url = self.base_url + "admin/smart_collections/%d.json" % id
        self.delete(url)
