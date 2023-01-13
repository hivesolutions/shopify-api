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

class OrderAPI(object):

    def list_orders(self, *args, **kwargs):
        url = self.admin_url + "orders.json"
        contents = self.get(url, **kwargs)
        return contents["orders"]

    def list_orders_a(self, limit = 50, all = True, **kwargs):
        url = self.admin_url + "orders.json"
        orders = self._fetch_many(
            url,
            item_name = "orders",
            method_count = self.count_orders,
            limit = limit,
            all = all,
            **kwargs
        )
        return orders

    def get_order(self, id):
        url = self.admin_url + "orders/%d.json" % id
        contents = self.get(url)
        return contents["order"]

    def count_orders(self, *args, **kwargs):
        url = self.admin_url + "orders/count.json"
        contents = self.get(url, **kwargs)
        return contents["count"]

    def transactions_order(self, id):
        url = self.admin_url + "orders/%d/transactions.json" % id
        contents = self.get(url)
        return contents["transactions"]

    def update_order(self, id, **kwargs):
        order = dict(kwargs)
        order["id"] = str(id)
        url = self.admin_url + "orders/%d.json" % id
        self.put(
            url,
            data_j = dict(order = order)
        )

    def pay_order(self, id):
        url = self.admin_url + "orders/%d/transactions.json" % id
        self.post(
            url,
            data_j = dict(
                transaction = dict(
                    kind = "capture"
                )
            )
        )

    def cancel_order(self, id, restock = True, email = False):
        url = self.admin_url + "orders/%d/cancel.json" % id
        self.post(
            url,
            data_j = dict(
                restock = restock,
                email = email
            )
        )

    def fulfill_order(self, id, location_id, **kwargs):
        fulfillment = dict(kwargs)
        fulfillment["location_id"] = location_id
        url = self.admin_url + "orders/%d/fulfillments.json" % id
        self.post(
            url,
            data_j = dict(fulfillment = fulfillment)
        )

    def metafields_order(self, id, *args, **kwargs):
        url = self.admin_url + "orders/%d/metafields.json" % id
        contents = self.get(url, **kwargs)
        return contents["metafields"]

    def create_metafield_order(self, id, key, value, type = None, value_type = None, namespace = "global"):
        type = type or value_type or "string"
        url = self.admin_url + "orders/%d/metafields.json" % id
        contents = self.post(
            url,
            data_j = dict(
                metafield = dict(
                    namespace = namespace,
                    key = key,
                    value = value,
                    type = type
                )
            )
        )
        return contents["metafield"]
