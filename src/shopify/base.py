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

import appier

from . import cart
from . import order
from . import product
from . import webhook

class API(
    appier.API,
    cart.CartAPI,
    order.OrderAPI,
    product.ProductAPI,
    webhook.WebhookAPI
):

    def __init__(self, *args, **kwargs):
        appier.API.__init__(self, *args, **kwargs)
        self.api_key = appier.conf("SHOPIFY_API_KEY", None)
        self.password = appier.conf("SHOPIFY_PASSWORD", None)
        self.secret = appier.conf("SHOPIFY_SECRET", None)
        self.store_url = appier.conf("SHOPIFY_STORE", None)
        self.website_url = appier.conf("SHOPIFY_WEBSITE", None)
        self.api_key = kwargs.get("api_key", self.api_key)
        self.password = kwargs.get("password", self.password)
        self.secret = kwargs.get("secret", self.secret)
        self.store_url = kwargs.get("store_url", self.store_url)
        self.website_url = kwargs.get("website_url", self.website_url)
        self._build_url()

    def build(
        self,
        method,
        url,
        data = None,
        data_j = None,
        data_m = None,
        headers = None,
        params = None,
        mime = None,
        kwargs = None
    ):
        cookie_l = []
        if hasattr(self, "session_id"):
            cookie_l.append("_session_id=%s" % self.session_id)
        if hasattr(self, "cart"): cookie_l.append("cart=%s" % self.cart)
        cookie = ";".join(cookie_l)
        if not cookie: return
        headers["Cookie"] = cookie

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
            raise appier.OperationalError(message = "No API key provided")
        if not self.password:
            raise appier.OperationalError(message = "No password provided")
        if not self.store_url:
            raise appier.OperationalError(message = "No store URL provided")
        self.base_url = "https://%s:%s@%s/" % (
            self.api_key, self.password, self.store_url
        )
        self.website_url = "http://%s/" % (self.website_url or self.store_url)
