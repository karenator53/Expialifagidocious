# Changelog

All notable changes to the Sonic Chain DEX Data Indexing Project will be documented in this file.

## [0.0.10] - 2024-01-24

### Added
- Initial deployment of the subgraph for Sonic chain DEX indexing
- Implementation of multiple DEX factory handlers
- Basic pair template setup
- Event handlers for Swap, Sync, and Transfer events

### Changed
- Updated factory addresses to use correct Sonic chain addresses
- Modified template imports to use SonicPair instead of UniswapV2Pair
- Updated factory mapping to use contract addresses as IDs

### Fixed
- Corrected factory addresses (previously using Ethereum's Uniswap V3 addresses)
- Fixed template import paths
- Added missing event handlers

## [0.0.11] - 2024-01-25

### Added
- Enhanced error handling in Transfer event handler
- Added logging for debugging purposes
- Implemented safe contract calls using try_catch pattern

### Changed
- Updated handleTransfer function to be more robust
- Modified error handling approach in pair handlers
- Added detailed logging for debugging

### Fixed
- Added proper null checks in event handlers
- Implemented safe contract calls for totalSupply
- Added missing log import

### Technical Details
- Transfer event handler now uses `try_totalSupply()` instead of direct calls
- Added warning logs for debugging pair creation issues
- Implemented proper error handling for contract calls

## [Pending Changes]

### To Be Implemented
1. Price Oracle Enhancement
   - Add token price calculations
   - Implement USD value tracking
   - Setup proper derivedETH calculations

2. Schema Updates
   - Add token0Price and token1Price fields
   - Add factory relationships
   - Update entity relationships

3. Factory Statistics
   - Implement proper volume aggregation
   - Add liquidity tracking
   - Update transaction counting

### Known Issues
1. USD calculations returning zero values
   - Root cause: Missing price oracle implementation
   - Status: In progress
   - Solution: Implementing price calculations using wS as base token

2. Missing factory relationships
   - Root cause: Incomplete schema definition
   - Status: To be fixed
   - Solution: Adding proper entity relationships

3. Transfer event indexing errors at block #277573
   - Root cause: Improper error handling
   - Status: Fixed in latest update
   - Solution: Enhanced error handling and logging

## Development Notes

### Price Oracle Implementation
- Decision to use wS as base token for price calculations
- Need to implement proper price relationships between pairs
- Plan to add USD value calculations based on wS price

### Event Handler Updates
- Enhanced Transfer event handler with better error handling
- Added detailed logging for debugging purposes
- Implemented safe contract calls to prevent reverts

### Schema Evolution
- Initial schema focused on basic pair and factory tracking
- Need to add price-related fields
- Planning to enhance entity relationships

### Testing Strategy
- Implemented playground queries for validation
- Added specific test cases for each handler
- Created validation queries for price calculations

## Future Plans

### Short Term
- Complete price oracle implementation
- Fix USD calculations
- Enhance factory statistics

### Medium Term
- Add historical data analysis
- Implement token metadata enrichment
- Optimize indexing performance

### Long Term
- Add advanced analytics
- Implement cross-DEX comparisons
- Add more sophisticated price calculations