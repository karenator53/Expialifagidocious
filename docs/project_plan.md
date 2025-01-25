# Sonic Chain DEX Data Indexing Project

## Project Overview
A subgraph implementation to index multiple Decentralized Exchanges (DEXs) on the Sonic chain, tracking pair creation events, swaps, and liquidity changes. The project aims to provide comprehensive data about DEX activities across multiple protocols using The Graph protocol.

## Goals & Requirements

### Primary Goals
- Index multiple DEX factories on Sonic chain
- Track pair creation events and updates
- Monitor swap activities and liquidity changes
- Provide USD-denominated metrics for volumes and TVL
- Enable cross-DEX analytics and comparisons

### Technical Requirements
- Support for multiple DEX protocols (Equalizer, Wagmi, Shadow, Beets, Metropolis, SwapX)
- V2-style pair template implementation
- Proper price oracle implementation using wS as base token
- Accurate volume and liquidity tracking
- Efficient event handling for Transfer, Sync, and Swap events

## Implementation Details

### DEX Factories Indexed
- Equalizer: `0xDDD9845Ba0D8f38d3045f804f67A1a8B9A528FcC`
- Wagmi: `0x56CFC796bC88C9c7e1b38C2b0aF9B7120B079aef`
- Shadow: `0xcD2d0637c94fe77C2896BbCBB174cefFb08DE6d7`
- Beets: `0x4fe80C33b27fB41946766C00e7A1F35A0D9E5ce3`
- Metropolis: `0x1570300e9cFEC66c9Fb0C8bc14366C86EB170Ad0`
- SwapX: `0x8121a3F8c4176E9765deEa0B95FA2BDfD3016794`

### Key Components
1. Factory Mapping
   - Tracks pair creation events
   - Maintains factory-level statistics
   - Uses contract addresses as unique identifiers

2. Pair Template
   - Handles swap events
   - Updates reserves and liquidity
   - Tracks volume metrics
   - Manages LP token supply

3. Price Oracle
   - Uses wS as base token
   - Calculates token prices
   - Provides USD value calculations

## Current Status

### Completed
- Basic subgraph structure implementation
- Factory address configuration
- Event handler setup
- Basic pair tracking
- Volume tracking in token amounts

### In Progress
- USD price calculations
- Factory volume aggregation
- Price oracle implementation
- Token price tracking

### Known Issues
1. Price Oracle
   - USD calculations returning zero values
   - Missing token price relationships
   - Incomplete derivedETH calculations

2. Data Tracking
   - Some events not being properly indexed
   - Missing factory relationships
   - Incomplete schema definitions

## Next Steps

### Immediate Tasks
1. Update schema to include:
   - Token price fields
   - Factory relationships
   - Proper entity relationships

2. Implement price calculations:
   - Add token0Price and token1Price to pairs
   - Setup proper derivedETH calculations
   - Configure USD value tracking

3. Fix event handlers:
   - Enhance Transfer event handling
   - Improve Sync event processing
   - Update Swap event calculations

### Future Enhancements
- Historical data analysis
- Token metadata enrichment
- Advanced analytics queries
- Performance optimizations

## Technical Notes

### Deployment
- Current Version: 0.0.10
- Endpoint: https://api.studio.thegraph.com/query/102096/historical-data-sonic/0.0.10
- Indexing Progress: 10% (Block #578421 of #5314829)

### Development Guidelines
- Use proper error handling in event handlers
- Implement safe contract calls
- Maintain proper entity relationships
- Follow The Graph's best practices