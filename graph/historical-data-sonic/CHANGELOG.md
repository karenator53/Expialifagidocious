# Changelog

## [0.0.18] - 2024-01-25

### Changed
- Updated subgraph spec version to 1.1.0 for official timeseries and aggregation support
- Aligned with The Graph's official specification for:
  - Timeseries entities
  - Aggregation directives
  - Entity field types

### Technical Details
- Upgraded from specVersion 1.0.0 to 1.1.0
- Maintained Int8 ID fields for timeseries entities
- Kept Timestamp type for timestamp fields
- Ensured compatibility with official aggregation support

### Next Steps
1. Deploy with new spec version
2. Verify timeseries data collection
3. Test aggregation queries
4. Monitor indexing performance

## [0.0.17] - 2024-01-25

### Changed
- Updated subgraph spec version to 1.0.0 for full feature support
- Fixed timeseries entity requirements:
  - Changed ID fields back to Int8 type
  - Maintained Timestamp type for timestamp fields
  - Updated aggregation entity definitions

### Technical Details
- Upgraded from specVersion 0.0.7 to 1.0.0
- Ensured proper ID field types for timeseries entities
- Maintained compatibility with The Graph's latest features

### Next Steps
1. Deploy updated subgraph
2. Test timeseries data collection
3. Verify aggregation functionality

## [0.0.16] - 2024-01-25

### Changed
- Updated subgraph spec version to 0.0.7 to support aggregations
- Fixed schema validation errors:
  - Changed timeseries entity ID fields to ID type
  - Changed timestamp fields to Timestamp type
  - Updated entity definitions to match spec requirements

### Technical Details
- Upgraded from specVersion 0.0.4 to 0.0.7
- Fixed type definitions in schema.graphql
- Ensured compatibility with The Graph's timeseries features

### Next Steps
1. Deploy updated subgraph
2. Verify timeseries data collection
3. Test aggregation queries

## [0.0.15] - 2024-01-25

### Changed
- Updated schema to align with The Graph's timeseries best practices
  - Changed timestamp fields to Int8 for better compatibility
  - Removed manual timeseries entity creation
  - Simplified mapping code to rely on graph-node's automatic handling
- Removed helper functions for timeseries entities
  - Removed getOrCreateTokenDayData
  - Removed getOrCreatePairDayData

### Technical Details
- Changed timestamp type from Timestamp to Int8
- Removed manual entity creation and updates
- Simplified mapping code by removing timeseries manipulation
- Letting graph-node handle all timeseries aggregations

### Next Steps
1. Deploy updated schema
2. Test automatic timeseries data generation
3. Verify aggregation queries

## [0.0.14] - 2024-01-25

### Changed
- Simplified timeseries entity handling
  - Removed direct entity manipulation
  - Using ID-based approach for timeseries entities
  - Letting graph-node handle timeseries aggregations
- Removed manual timeseries updates from handlers

### Technical Details
- Changed timeseries entity functions to return IDs
- Removed manual entity creation and updates
- Relying on graph-node's automatic timeseries handling
- Simplified mapping code for better maintainability

### Next Steps
1. Test automatic timeseries aggregation
2. Verify data consistency
3. Monitor indexing performance

## [0.0.13] - 2024-01-25

### Fixed
- Fixed timestamp type issues in mapping handlers
  - Updated TokenDayData timestamp to use i64
  - Updated PairDayData timestamp to use i64
- Fixed build errors related to type mismatches

### Technical Details
- Added BigInt.toI64() conversion for timestamps
- Ensured proper type handling in timeseries entities
- Verified successful build with type fixes

## [0.0.12] - 2024-01-25

### Added
- Implemented timeseries support in mapping handlers
  - Added TokenDayData and PairDayData tracking in handleSwap
  - Added price and liquidity tracking in handleSync
  - Added helper functions for creating day data entities
- Added price calculation logic for pairs
- Added volume and liquidity tracking in timeseries

### Changed
- Updated handleSwap to track daily metrics
- Updated handleSync to maintain price history
- Enhanced entity saving to include timeseries data

### Technical Details
- Implemented dayID calculation based on timestamp
- Added price calculations for token pairs
- Added volume aggregation in daily entities
- Enhanced liquidity tracking with USD values

### Next Steps
1. Verify schema generation for new entities
2. Test timeseries queries
3. Add more sophisticated price calculations
4. Implement additional time intervals if needed

## [0.0.11] - 2024-01-25

### Added
- Timeseries entities for historical price tracking
  - TokenDayData for daily token price and volume data
  - PairDayData for daily pair statistics
  - TokenHourData aggregation for hourly token metrics
  - PairHourData aggregation for hourly pair metrics
- Aggregation support for price tracking
  - High/Low price calculations
  - Volume aggregation
  - Transaction count aggregation

### Changed
- Enhanced schema with timeseries support
- Added hourly and daily data tracking
- Improved price tracking granularity

### Technical Details
- Added @entity(timeseries: true) support
- Implemented @aggregation for hourly data
- Added proper timestamp handling
- Enhanced metric tracking with aggregation functions

### Next Steps
1. Update mapping handlers for timeseries data
2. Implement price calculation logic
3. Add volume tracking in handlers
4. Test aggregation queries 