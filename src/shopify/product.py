#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Shopify API
# Copyright (c) 2008-2016 Hive Solutions Lda.
#
# This file is part of Hive Shopify API.
#
# Hive Shopify API is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Hive Shopify API is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Hive Shopify API. If not, see <http://www.gnu.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2016 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "GNU General Public License (GPL), Version 3"
""" The license for the module """

class ProductApi(object):

    def list_products(self, *args, **kwargs):
        url = self.base_url + "admin/products.json"
        contents = self.get(
            url,
            **kwargs
        )
        return contents["products"]

    def many_products(self, *args, **kwargs):
        url = self.base_url + "admin/products.json"
        contents = self.get_many(
            url,
            key = "products",
            **kwargs
        )
        return contents["products"]

    def images_product(self, id, *args, **kwargs):
        url = self.base_url + "admin/products/%d/images.json" % id
        contents = self.get(
            url,
            **kwargs
        )
        return contents["images"]
