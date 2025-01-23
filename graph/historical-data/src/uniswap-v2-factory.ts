import { BigInt } from "@graphprotocol/graph-ts"
import { PairCreated as PairCreatedEvent } from "../generated/UniswapV2Factory/UniswapV2Factory"
import { Pair, Token } from "../generated/schema"
import { UniswapV2Pair as PairTemplate } from "../generated/templates"
import { loadOrCreateToken, ZERO_BD, ZERO_BI } from "./utils"

export function handlePairCreated(event: PairCreatedEvent): void {
  // Load or create tokens
  let token0 = loadOrCreateToken(event.params.token0)
  let token1 = loadOrCreateToken(event.params.token1)

  // Create new pair
  let pair = new Pair(event.params.pair.toHexString())
  pair.token0 = token0.id
  pair.token1 = token1.id
  pair.address = event.params.pair
  pair.createdAtBlockNumber = event.block.number
  pair.createdAtTimestamp = event.block.timestamp
  pair.reserve0 = ZERO_BD
  pair.reserve1 = ZERO_BD
  pair.totalSupply = ZERO_BD
  pair.reserveUSD = ZERO_BD
  pair.volumeToken0 = ZERO_BD
  pair.volumeToken1 = ZERO_BD
  pair.volumeUSD = ZERO_BD
  pair.untrackedVolumeUSD = ZERO_BD
  pair.txCount = ZERO_BI

  // Create pair template
  PairTemplate.create(event.params.pair)

  // Save entities
  token0.save()
  token1.save()
  pair.save()
}
