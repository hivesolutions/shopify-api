#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Shopify API
# Copyright (C) 2008-2015 Hive Solutions Lda.
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

__copyright__ = "Copyright (c) 2008-2015 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "GNU General Public License (GPL), Version 3"
""" The license for the module """

import appier

from . import order
from . import product
from . import webhook

class Api(
    appier.Api,
    order.OrderApi,
    product.ProductApi,
    webhook.WebhookApi
):

    def __init__(self, *args, **kwargs):
        appier.Api.__init__(self, *args, **kwargs)
        self.api_key = appier.conf("SHOPIFY_API_KEY", None)
        self.password = appier.conf("SHOPIFY_PASSWORD", None)
        self.secret = appier.conf("SHOPIFY_SECRET", None)
        self.store_url = appier.conf("SHOPIFY_STORE", None)
        self.api_key = kwargs.get("api_key", self.api_key)
        self.password = kwargs.get("password", self.password)
        self.secret = kwargs.get("secret", self.secret)
        self.store_url = kwargs.get("store_url", self.store_url)
        self._build_url()

    def get_many(self, url, key = None, **kwargs):
            page = 1
            result = []
            while True:
                items = self.get(url, page = page, **kwargs)
                if key: items = items[key]
                if not items: break
                result.extend(items)
                page += 1
            if key: result = {key : result}
            return result

    def _build_url(self):
        if not self.api_key:
            raise appier.OperationalError(message = "No api key provided")
        if not self.password:
            raise appier.OperationalError(message = "No password provided")
        if not self.store_url:
            raise appier.OperationalError(message = "No store url provided")
        self.base_url = "https://%s:%s@%s/" % (
            self.api_key, self.password, self.store_url
        )
