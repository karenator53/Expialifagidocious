import { PoolCreated as PoolCreatedEvent } from "../generated/UniswapV3Factory/UniswapV3Factory"
import { Pool, Token } from "../generated/schema"
import { UniswapV3Pool as PoolTemplate } from "../generated/templates"
import { loadOrCreateToken, ZERO_BD, ZERO_BI } from "./utils"

export function handlePoolCreated(event: PoolCreatedEvent): void {
  // Load or create tokens
  let token0 = loadOrCreateToken(event.params.token0)
  let token1 = loadOrCreateToken(event.params.token1)

  // Create new pool
  let pool = new Pool(event.params.pool.toHexString())
  pool.token0 = token0.id
  pool.token1 = token1.id
  pool.address = event.params.pool
  pool.fee = parseInt(event.params.fee.toString()) as i32
  pool.createdAtBlockNumber = event.block.number
  pool.createdAtTimestamp = event.block.timestamp
  pool.liquidity = ZERO_BI
  pool.sqrtPrice = ZERO_BI
  pool.token0Price = ZERO_BD
  pool.token1Price = ZERO_BD
  pool.tick = ZERO_BI
  pool.volumeToken0 = ZERO_BD
  pool.volumeToken1 = ZERO_BD
  pool.volumeUSD = ZERO_BD
  pool.untrackedVolumeUSD = ZERO_BD
  pool.txCount = ZERO_BI

  // Create pool template
  PoolTemplate.create(event.params.pool)

  // Save entities
  token0.save()
  token1.save()
  pool.save()
}