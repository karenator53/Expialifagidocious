import { BigInt } from "@graphprotocol/graph-ts"
import { PairCreated as PairCreatedEvent } from "../generated/UniswapV2Factory/UniswapV2Factory"
import { Pair, Token, Factory } from "../generated/schema"
import { SonicPair as PairTemplate } from "../generated/templates"
import { loadOrCreateToken, ZERO_BD, ZERO_BI } from "./utils"

export function handlePairCreated(event: PairCreatedEvent): void {
  // Load or create factory using the factory contract address as the ID
  let factory = Factory.load(event.address.toHexString())
  if (factory === null) {
    factory = new Factory(event.address.toHexString())
    factory.pairCount = ZERO_BI
    factory.totalVolumeUSD = ZERO_BD
    factory.totalLiquidityUSD = ZERO_BD
    factory.txCount = ZERO_BI
    factory.totalValueLockedUSD = ZERO_BD
  }
  factory.pairCount = factory.pairCount.plus(BigInt.fromI32(1))
  factory.save()

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
