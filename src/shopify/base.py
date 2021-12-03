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

import hmac
import base64
import hashlib

import appier

from . import cart
from . import inventory_item
from . import shop
from . import order
from . import product
from . import webhook
from . import location
from . import smart_collection

CLIENT_ID = None
""" The default value to be used for the client id
in case no client id is provided to the API client """

CLIENT_SECRET = None
""" The secret value to be used for situations where
no client secret has been provided to the client """

REDIRECT_URL = "http://localhost:8080/oauth"
""" The redirect URL used as default (fallback) value
in case none is provided to the API (client) """

SCOPE = (
    "read_products",
    "write_products"
)
""" The list of permissions to be used to create the
scope string for the OAuth value """

class API(
    appier.API,
    cart.CartAPI,
    inventory_item.InventoryItemAPI,
    shop.ShopAPI,
    order.OrderAPI,
    product.ProductAPI,
    webhook.WebhookAPI,
    location.LocationAPI,
    smart_collection.SmartCollectionAPI
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

    def graphql(self, query_data):
        url = self.base_url + "admin/api/graphql.json"
        contents = self.post(url = url, data = query_data, headers = {
            "Content-Type" : "application/graphql"
        })
        return contents

    def verify_request(
        self,
        request,
        field = "hmac",
        header = "X-Shopify-Hmac-SHA256"
    ):
        is_param = True if request.get_param(field, None) else False
        signature = request.get_param(field, None)
        signature = request.get_header(header, signature)
        appier.verify(
            signature,
            message = "No signature found in request",
            exception = appier.OperationalError
        )

        if is_param:
            params_l = [(key, param) for key, param in appier.legacy.iteritems(request.get_params()) if not key == field]
            params_l.sort()
            params_s = appier.legacy.urlencode(params_l)
            data = appier.legacy.bytes(params_s, encoding = "utf-8", force = True)
        else:
            data = request.get_data()

        self.verify_signature(signature, data, base_64 = not is_param)

    def verify_signature(self, signature, data, key = None, base_64 = True):
        key = key if key else self.secret
        appier.verify(
            key,
            message = "No key for signing found",
            exception = appier.OperationalError
        )

        signature_b = appier.legacy.bytes(signature)
        key_b = appier.legacy.bytes(key)

        if base_64:
            _signature = hmac.new(key_b, data, hashlib.sha256).digest()
            _signature_b64 = base64.b64encode(_signature)
            valid = hmac.compare_digest(_signature_b64, signature_b)
        else:
            _signature = hmac.new(key_b, data, hashlib.sha256).hexdigest()
            _signature_b = appier.legacy.bytes(_signature)
            valid = hmac.compare_digest(_signature_b, signature_b)

        appier.verify(
            valid,
            message = "Request signature is not valid",
            exception = appier.SecurityError
        )

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

class OAuthAPI(appier.OAuth2API, API):

    def __init__(self, *args, **kwargs):
        appier.OAuth2API.__init__(self, *args, **kwargs)
        API.__init__(self, *args, **kwargs)
        self.client_id = appier.conf("SHOPIFY_ID", CLIENT_ID)
        self.secret = appier.conf("SHOPIFY_SECRET", CLIENT_SECRET)
        self.redirect_url = appier.conf("SHOPIFY_REDIRECT_URL", REDIRECT_URL)
        self.store_url = appier.conf("SHOPIFY_STORE", None)
        self.client_id = kwargs.get("client_id", self.client_id)
        self.secret = kwargs.get("secret", self.secret)
        self.redirect_url = kwargs.get("redirect_url", self.redirect_url)
        self.store_url = kwargs.get("store_url", self.store_url)
        self.scope = kwargs.get("scope", SCOPE)
        self.access_token = kwargs.get("access_token", None)
        self.access_mode = kwargs.get("access_mode", None)
        self._build_url()

    def oauth_authorize(self, state = None):
        url = self.base_url + "admin/oauth/authorize"
        values = dict(
            client_id = self.client_id,
            redirect_uri = self.redirect_url,
            response_type = "code",
            scope = ",".join(self.scope)
        )
        if self.access_mode: values["grant_options[]"] = self.access_mode
        if state: values["state"] = state
        data = appier.legacy.urlencode(values)
        url = url + "?" + data
        return url

    def oauth_access(self, code):
        url = self.base_url + "admin/oauth/access_token"
        contents = self.post(
            url,
            token = False,
            client_id = self.client_id,
            client_secret = self.client_secret,
            code = code
        )
        self.access_token = contents["access_token"]
        self.trigger("access_token", self.access_token)
        return self.access_token

    @property
    def client_secret(self):
        return self.secret

    def _build_url(self):
        if not self.store_url:
            raise appier.OperationalError(message = "No store URL provided")
        self.base_url = "https://%s/" % self.store_url

    def _fetch_many(
        self, 
        url,
        item_name = None,
        method_count = None,
        limit = 50,
        bulk_limit = 250,
        all = False,
        **kwargs
    ):
        # creates the sequence that is going to hold the complete set of
        # items to be retrieved from teh remote data source
        items = []

        # creates a variable to store the identifier of the last item that was
        # retrieved, assumes this will allow proper pagination of the items
        last_id = None

        # sets the initial value of the items remaining to be fetched as the
        # limit value, this value will change as the loop continues
        item_remaining = limit

        # if "all" flag is set to true then sets the the items remaining value
        # to the value obtained method count method call
        if all:
            limit = bulk_limit
            item_remaining = method_count()

        # keeps fetching items until there isn't any more items to fetch
        while item_remaining > 0:
            contents = self.get(
                url,
                limit = limit,
                since_id = last_id,
                **kwargs
            )
            items.extend(contents[item_name or "items"])
            try:
                last_id = items[-1]["id"]
            except:
                return []
            item_remaining -= limit

        # returns the final set of items that have been retrieved from the
        # remote data source according to the specification
        return items
