# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

*

### Changed

*

### Fixed

* Issue related to missing replacement of code - [#22](https://github.com/hivesolutions/shopify-api/issues/22)

## [0.7.0] - 2023-01-13

### Added

* Add support for versioned admin endpoints, using `SHOPIFY_API_VERSION`

## [0.6.5] - 2022-12-26

### Changed

* Renamed repository into `shopify-api`

### Fixed

* Renamed metafield `value_type` as `type` due to Shopify deprecation - [#19](https://github.com/hivesolutions/shopify-api/issues/19)

## [0.6.4] - 2021-12-03

### Fixed

* Fixed naming in the `count_orders` call

## [0.6.3] - 2021-12-03

### Fixed

* Returns of the items values

## [0.6.2] - 2021-12-03

### Changed

* Added support for the `bulk_limit` parameter

### Fixed

* Dynamic support for items naming in the `_fetch_many()` method

## [0.6.1] - 2021-12-03

### Changed

* Improved the current `_fetch_many` solution

## [0.6.0] - 2021-12-02

### Changed

* Created the `list_orders_a` for advanced listing of orders

## [0.5.0] - 2021-11-12

### Added

* Endpoint for creating and listing order metafields

## [0.4.0] - 2021-09-03

### Added

* Inventory Item API

## [0.3.1] - 2021-09-01

### Added

* New automation structure

## [0.3.0] - 2021-09-01

### Added

* Endpoint for listing locations
* Endpoint for fulfilling an order
