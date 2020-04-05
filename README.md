# Shopify API

API client for the [Shopify](https://www.shopify.com) service.

## Configuration

| Name | Type | Default | Description |
| ----- | ----- | ----- | ----- |
| **SHOPIFY_API_KEY** | `str` | `None` | The username/key to be used in the authentication with the Shopify API. |
| **SHOPIFY_PASSWORD** | `str` | `None` | The password to be used in the authentication with the Shopify API. |
| **SHOPIFY_SECRET** | `str` | `None` | The shared secret to be used for message validation with the Shopify API. |
| **SHOPIFY_STORE** | `str` | `None` | The name/domain of the Shopify store to use the Shopify API. |
| **SHOPIFY_WEBSITE** | `str` | `None` | The public name/domain of the Shopify store to use the Shopify API, may be different from `SHOPIFY_STORE`. |
| **SHOPIFY_ID** | `str` | `None` | While using OAuth provides a way to define the client identifier. |
| **SHOPIFY_SECRET** | `str` | `None` | While using OAuth provides a way to define the client secret. |
| **SHOPIFY_REDIRECT_URL** | `str` | `None` | To be used in the OAuth process as the target redirect URL. |

## License

Shopify API is currently licensed under the [Apache License, Version 2.0](http://www.apache.org/licenses/).

## Build Automation

[![Build Status](https://travis-ci.org/hivesolutions/shopify_api.svg?branch=master)](https://travis-ci.org/hivesolutions/shopify_api)
[![Coverage Status](https://coveralls.io/repos/hivesolutions/shopify_api/badge.svg?branch=master)](https://coveralls.io/r/hivesolutions/shopify_api?branch=master)
[![PyPi Status](https://img.shields.io/pypi/v/shopify_api.svg)](https://pypi.python.org/pypi/shopify_api)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://www.apache.org/licenses/)
