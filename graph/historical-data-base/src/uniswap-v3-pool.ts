import { BigInt, BigDecimal } from '@graphprotocol/graph-ts'
import { Swap as SwapEvent } from '../generated/templates/UniswapV3Pool/UniswapV3Pool'
import { Pool, Swap, Token, Bundle } from '../generated/schema'
import { UniswapV3Pool } from '../generated/templates/UniswapV3Pool/UniswapV3Pool'
import { convertTokenToDecimal, ZERO_BD, ONE_BD, ZERO_BI, ONE_BI, bigDecimalAbs, bigDecimalPow } from './utils'

export function handleSwap(event: SwapEvent): void {
  let pool = Pool.load(event.address.toHexString())
  if (pool === null) return

  let token0 = Token.load(pool.token0)
  let token1 = Token.load(pool.token1)
  if (token0 === null || token1 === null) return

  let bundle = Bundle.load('1')
  if (bundle === null) {
    bundle = new Bundle('1')
    bundle.ethPrice = ZERO_BD
    bundle.save()
  }

  let amount0 = convertTokenToDecimal(event.params.amount0, BigInt.fromI32(token0.decimals))
  let amount1 = convertTokenToDecimal(event.params.amount1, BigInt.fromI32(token1.decimals))

  // Update pool volume
  pool.volumeToken0 = pool.volumeToken0.plus(bigDecimalAbs(amount0))
  pool.volumeToken1 = pool.volumeToken1.plus(bigDecimalAbs(amount1))
  pool.volumeUSD = pool.volumeUSD.plus(bigDecimalAbs(amount0).times(token0.derivedETH.times(bundle.ethPrice)))
  pool.untrackedVolumeUSD = pool.untrackedVolumeUSD.plus(bigDecimalAbs(amount0).times(token0.derivedETH.times(bundle.ethPrice)))
  pool.txCount = pool.txCount.plus(ONE_BI)

  // Update token volume
  token0.volume = token0.volume.plus(bigDecimalAbs(amount0))
  token0.volumeUSD = token0.volumeUSD.plus(bigDecimalAbs(amount0).times(token0.derivedETH.times(bundle.ethPrice)))
  token0.untrackedVolumeUSD = token0.untrackedVolumeUSD.plus(bigDecimalAbs(amount0).times(token0.derivedETH.times(bundle.ethPrice)))
  token0.txCount = token0.txCount.plus(ONE_BI)

  token1.volume = token1.volume.plus(bigDecimalAbs(amount1))
  token1.volumeUSD = token1.volumeUSD.plus(bigDecimalAbs(amount1).times(token1.derivedETH.times(bundle.ethPrice)))
  token1.untrackedVolumeUSD = token1.untrackedVolumeUSD.plus(bigDecimalAbs(amount1).times(token1.derivedETH.times(bundle.ethPrice)))
  token1.txCount = token1.txCount.plus(ONE_BI)

  // Update pool state
  pool.sqrtPrice = event.params.sqrtPriceX96
  let sqrtPriceX96BD = BigDecimal.fromString(event.params.sqrtPriceX96.toString())
  pool.token0Price = bigDecimalPow(sqrtPriceX96BD, 2).div(bigDecimalPow(BigDecimal.fromString('2'), 192))
  pool.token1Price = ONE_BD.div(pool.token0Price)
  pool.tick = BigInt.fromI32(event.params.tick)
  pool.liquidity = event.params.liquidity

  // Create swap event
  let swap = new Swap(event.transaction.hash.toHexString().concat('-').concat(event.logIndex.toString()))
  swap.transaction = event.transaction.hash
  swap.timestamp = event.block.timestamp
  swap.pool = pool.id
  swap.token0 = token0.id
  swap.token1 = token1.id
  swap.amount0In = amount0.lt(ZERO_BD) ? ZERO_BD : amount0
  swap.amount1In = amount1.lt(ZERO_BD) ? ZERO_BD : amount1
  swap.amount0Out = amount0.gt(ZERO_BD) ? ZERO_BD : bigDecimalAbs(amount0)
  swap.amount1Out = amount1.gt(ZERO_BD) ? ZERO_BD : bigDecimalAbs(amount1)
  swap.amountUSD = bigDecimalAbs(amount0).times(token0.derivedETH.times(bundle.ethPrice))
  swap.logIndex = event.logIndex

  // Save entities
  pool.save()
  token0.save()
  token1.save()
  swap.save()
} 