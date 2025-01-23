import { PairCreated as PairCreatedEvent } from "../generated/SushiSwapFactory/UniswapV2Factory"
import { Token, Pair } from "../generated/schema"

export function handlePairCreated(event: PairCreatedEvent): void {
  // Create token0 if it doesn't exist
  let token0 = Token.load(event.params.token0.toHexString())
  if (token0 === null) {
    token0 = new Token(event.params.token0.toHexString())
    token0.save()
  }

  // Create token1 if it doesn't exist
  let token1 = Token.load(event.params.token1.toHexString())
  if (token1 === null) {
    token1 = new Token(event.params.token1.toHexString())
    token1.save()
  }

  // Create new pair
  let pair = new Pair(event.params.pair.toHexString())
  pair.token0 = token0.id
  pair.token1 = token1.id
  pair.address = event.params.pair
  pair.createdAtBlockNumber = event.block.number
  pair.createdAtTimestamp = event.block.timestamp
  pair.save()
}