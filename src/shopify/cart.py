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

class CartAPI(object):

    def get_cart(self):
        url = self.website_url + "cart.js"
        contents, file = self.get(url, handle = True)
        self._handle_cookie(file)
        return contents

    def clear_cart(self):
        url = self.website_url + "cart/clear.js"
        contents, file = self.post(url, handle = True)
        self._handle_cookie(file)
        return contents

    def add_cart(self, id, quantity = 1):
        url = self.website_url + "cart/add.js"
        contents, file = self.post(
            url,
            data_j = dict(
                id = id,
                quantity = quantity
            ),
            handle = True
        )
        self._handle_cookie(file)
        return contents

    def _handle_cookie(self, file):
        headers = file.info()
        cookie = headers.get("Set-Cookie", None)
        if not cookie: return
        cookie_m = appier.parse_cookie(cookie)
        session_id = cookie_m.get("_session_id", None)
        cart = cookie_m.get("cart", None)
        if session_id: self.session_id = session_id
        if cart: self.cart = cart
