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

    def get_orders_count(self, *args, **kwargs):
        url = self.base_url + "admin/orders/count.json"
        contents = self.get(url, **kwargs)
        return contents["count"]

    def list_orders(self, all = True, limit = 50, **kwargs):
        url = self.base_url + "admin/orders.json"
        orders = []
        last_id = None
        orders_count = limit

        # if "all" flag is set to true then set the "limit" to the maximum
        # allowed value (250) and set "order_count" with the total number
        # of existing orders
        if all:
            limit = 250
            orders_count = self.get_orders_count()

        # keep fetching orders until there isn't any more orders to fetch
        while orders_count > 0:
            contents = self.get(
                url,
                limit = limit,
                since_id = last_id,
                **kwargs
            )
            orders.extend(contents["orders"])
            try:
                last_id = orders[-1]["id"]
            except:
                return []
            orders_count -= limit

        return orders

    def get_order(self, id):
        url = self.base_url + "admin/orders/%d.json" % id
        contents = self.get(url)
        return contents["order"]

    def transactions_order(self, id):
        url = self.base_url + "admin/orders/%d/transactions.json" % id
        contents = self.get(url)
        return contents["transactions"]

    def update_order(self, id, **kwargs):
        order = dict(kwargs)
        order["id"] = str(id)
        url = self.base_url + "admin/orders/%d.json" % id
        self.put(
            url,
            data_j = dict(order = order)
        )

    def pay_order(self, id):
        url = self.base_url + "admin/orders/%d/transactions.json" % id
        self.post(
            url,
            data_j = dict(
                transaction = dict(
                    kind = "capture"
                )
            )
        )

    def cancel_order(self, id, restock = True, email = False):
        url = self.base_url + "admin/orders/%d/cancel.json" % id
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
        url = self.base_url + "admin/orders/%d/fulfillments.json" % id
        self.post(
            url,
            data_j = dict(fulfillment = fulfillment)
        )

    def metafields_order(self, id, *args, **kwargs):
        url = self.base_url + "admin/orders/%d/metafields.json" % id
        contents = self.get(url, **kwargs)
        return contents["metafields"]

    def create_metafield_order(self, id, key, value, value_type = "string", namespace = "global"):
        url = self.base_url + "admin/orders/%d/metafields.json" % id
        contents = self.post(
            url,
            data_j = dict(
                metafield = dict(
                    namespace = namespace,
                    key = key,
                    value = value,
                    value_type = value_type
                )
            )
        )
        return contents["metafield"]
