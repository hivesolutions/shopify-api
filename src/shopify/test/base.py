#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Appier Framework
# Copyright (c) 2008-2025 Hive Solutions Lda.
#
# This file is part of Hive Appier Framework.
#
# Hive Appier Framework is free software: you can redistribute it and/or modify
# it under the terms of the Apache License as published by the Apache
# Foundation, either version 2.0 of the License, or (at your option) any
# later version.
#
# Hive Appier Framework is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# Apache License for more details.
#
# You should have received a copy of the Apache License along with
# Hive Appier Framework. If not, see <http://www.apache.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__copyright__ = "Copyright (c) 2008-2025 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

import unittest

import appier

import shopify


class APITest(unittest.TestCase):

    def test_verify_signature(self):
        api = shopify.API(
            api_key="dummy_api_key",
            password="dummy_password",
            secret="dummy_secret",
            store_url="dummy_store_url",
        )

        result = api.verify_signature(
            "+AX/dhRR/3hKfDlZ4NqDhqPz0RXN/56CYxXNeHETdhc=", b"hello world"
        )
        self.assertEqual(result, None)

        self.assertRaises(
            appier.SecurityError,
            lambda: api.verify_signature(
                "0AX/dhRR/3hKfDlZ4NqDhqPz0RXN/56CYxXNeHETdhc=", b"hello world"
            ),
        )

        result = api.verify_signature(
            "f805ff761451ff784a7c3959e0da8386a3f3d115cdff9e826315cd7871137617",
            b"hello world",
            base_64=False,
        )
        self.assertEqual(result, None)

        self.assertRaises(
            appier.SecurityError,
            lambda: api.verify_signature(
                "d805ff761451ff784a7c3959e0da8386a3f3d115cdff9e826315cd7871137617",
                b"hello world",
                base_64=False,
            ),
        )

    def test_base_url(self):
        api = shopify.API(
            api_key="dummy_api_key",
            password="dummy_password",
            secret="dummy_secret",
            store_url="dummy_store_url",
        )
        self.assertEqual(
            api.base_url, "https://dummy_api_key:dummy_password@dummy_store_url/"
        )

        api = shopify.API(
            api_version="2023-01",
            api_key="dummy_api_key",
            password="dummy_password",
            secret="dummy_secret",
            store_url="dummy_store_url",
        )
        self.assertEqual(
            api.base_url, "https://dummy_api_key:dummy_password@dummy_store_url/"
        )

    def test_admin_url(self):
        api = shopify.API(
            api_key="dummy_api_key",
            password="dummy_password",
            secret="dummy_secret",
            store_url="dummy_store_url",
        )
        self.assertEqual(
            api.admin_url, "https://dummy_api_key:dummy_password@dummy_store_url/admin/"
        )

        api = shopify.API(
            api_version="2023-01",
            api_key="dummy_api_key",
            password="dummy_password",
            secret="dummy_secret",
            store_url="dummy_store_url",
        )
        self.assertEqual(
            api.admin_url,
            "https://dummy_api_key:dummy_password@dummy_store_url/admin/api/2023-01/",
        )


class OAuthAPITest(unittest.TestCase):

    def test_verify_signature(self):
        api = shopify.OAuthAPI(
            api_key="dummy_api_key",
            password="dummy_password",
            secret="dummy_secret",
            store_url="dummy_store_url",
        )

        result = api.verify_signature(
            "+AX/dhRR/3hKfDlZ4NqDhqPz0RXN/56CYxXNeHETdhc=", b"hello world"
        )
        self.assertEqual(result, None)

        self.assertRaises(
            appier.SecurityError,
            lambda: api.verify_signature(
                "0AX/dhRR/3hKfDlZ4NqDhqPz0RXN/56CYxXNeHETdhc=", b"hello world"
            ),
        )

        result = api.verify_signature(
            "f805ff761451ff784a7c3959e0da8386a3f3d115cdff9e826315cd7871137617",
            b"hello world",
            base_64=False,
        )
        self.assertEqual(result, None)

        self.assertRaises(
            appier.SecurityError,
            lambda: api.verify_signature(
                "d805ff761451ff784a7c3959e0da8386a3f3d115cdff9e826315cd7871137617",
                b"hello world",
                base_64=False,
            ),
        )

    def test_base_url(self):
        api = shopify.OAuthAPI(
            api_key="dummy_api_key",
            password="dummy_password",
            secret="dummy_secret",
            store_url="dummy_store_url",
        )
        self.assertEqual(api.base_url, "https://dummy_store_url/")

        api = shopify.OAuthAPI(
            api_version="2023-01",
            api_key="dummy_api_key",
            password="dummy_password",
            secret="dummy_secret",
            store_url="dummy_store_url",
        )
        self.assertEqual(api.base_url, "https://dummy_store_url/")

    def test_admin_url(self):
        api = shopify.OAuthAPI(
            api_key="dummy_api_key",
            password="dummy_password",
            secret="dummy_secret",
            store_url="dummy_store_url",
        )
        self.assertEqual(api.admin_url, "https://dummy_store_url/admin/")

        api = shopify.OAuthAPI(
            api_version="2023-01",
            api_key="dummy_api_key",
            password="dummy_password",
            secret="dummy_secret",
            store_url="dummy_store_url",
        )
        self.assertEqual(api.admin_url, "https://dummy_store_url/admin/api/2023-01/")
