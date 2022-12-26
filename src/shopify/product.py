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

class ProductAPI(object):

    def list_products(self, *args, **kwargs):
        url = self.base_url + "admin/products.json"
        contents = self.get(url, **kwargs)
        return contents["products"]

    def many_products(self, *args, **kwargs):
        url = self.base_url + "admin/products.json"
        contents = self.get_many(
            url,
            key = "products",
            **kwargs
        )
        return contents["products"]

    def count_products(self, *args, **kwargs):
        url = self.base_url + "admin/products/count.json"
        contents = self.get(url, **kwargs)
        return contents["count"]

    def create_product(self, product):
        url = self.base_url + "admin/products.json"
        contents = self.post(
            url,
            data_j = dict(product = product)
        )
        return contents["product"]

    def get_product(self, id):
        url = self.base_url + "admin/products/%d.json" % id
        contents = self.get(url)
        return contents["product"]

    def delete_product(self, id):
        url = self.base_url + "admin/products/%d.json" % id
        self.delete(url)

    def images_product(self, id, *args, **kwargs):
        url = self.base_url + "admin/products/%d/images.json" % id
        contents = self.get(url, **kwargs)
        return contents["images"]

    def create_image_product(self, id, image):
        url = self.base_url + "admin/products/%d/images.json" % id
        contents = self.post(url, data_j = dict(image = image))
        return contents["image"]

    def delete_image_product(self, id, image_id):
        url = self.base_url + "admin/products/%d/images/%d.json" % (id, image_id)
        self.delete(url)

    def metafields_product(self, id, *args, **kwargs):
        url = self.base_url + "admin/products/%d/metafields.json" % id
        contents = self.get(url, **kwargs)
        return contents["metafields"]

    def create_metafield_product(self, id, key, value, type = None, value_type = None, namespace = "global"):
        type = type or value_type or "string"

        url = self.base_url + "admin/products/%d/metafields.json" % id
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
