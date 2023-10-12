# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.4.2] - 2023-10-11

### Added

### Changed
- Switched from python-dateutil to pendulum for parsing datetime types.

## [0.4.1] - 2023-09-21

### Added

### Changed
- Allow passing of valid strings as values for datetime and UUID fields.

## [0.4.0] - 2023-07-27

### Added

### Changed
- Enabled backing store support

## [0.3.7] - 2023-07-04

### Added

### Changed
- Fixes the key assignment to the writer in write_bytes_value.

## [0.3.6] - 2023-06-27

### Added

### Changed
- Fixed a bug with loading json response in method to get root parse node.

## [0.3.5] - 2023-06-14

### Added

- Added support for composed types (de)serialization.

### Changed

- Fixed a bug with assigning field values.

## [0.3.4] - 2023-05-17

### Added

### Changed

- Fixed a bug with assigning field values.

## [0.3.3] - 2023-04-27

### Added

### Changed

- Fixed a bug with deserializing collection of enum values.

## [0.3.2] - 2023-04-27

### Added

### Changed

- Fixed a bug with deserializing models with additional data.

## [0.3.1] - 2023-03-20

### Added

### Changed

- Fixed a bug with deserializing bytes responses.

## [0.3.0] - 2023-03-09

### Added

### Changed

- Switched from snake casing api response keys to prevent mismatch scenarios.
- Fixed a bug with getting child node using deserializer identifier

## [0.2.2] - 2023-02-21

### Added

### Changed

- Fixed a bug with deserializing 'None' string values in enums.

