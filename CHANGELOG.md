## [0.0.19] - 2024-01-25

### Removed
- Manual timeseries data handling code from mapping files
- Custom implementation of TokenDayData and PairDayData updates
- Direct manipulation of timeseries aggregations

### Changed
- Switched to using The Graph's native timeseries support
- Updated schema to use built-in timeseries directives
- Simplified event handling to rely on automatic aggregations

### Technical Notes
- The Graph now automatically handles timeseries aggregations through the `@timeseries` directive
- Removed manual calculations for:
  - Daily volume updates
  - Price tracking
  - Transaction counting
  - USD calculations
- These metrics are now handled by the graph-node directly

### Impact on Queries
- Historical data can now be queried using The Graph's standard timeseries query format
- Example queries will need to be updated to use the new schema format
- Previous custom aggregation methods have been replaced with standard Graph Protocol aggregations

### Next Steps
- Update query documentation to reflect new timeseries structure
- Test aggregation queries against the new schema
- Verify automatic timeseries data collection 