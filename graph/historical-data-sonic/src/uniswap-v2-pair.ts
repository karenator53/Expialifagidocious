import { BigInt, BigDecimal, log, ethereum } from '@graphprotocol/graph-ts'
import { Swap as SwapEvent, Sync as SyncEvent, Transfer as TransferEvent } from '../generated/templates/SonicPair/UniswapV2Pair'
import { Pair, Swap, Token, Bundle } from '../generated/schema'
import { UniswapV2Pair } from '../generated/templates/SonicPair/UniswapV2Pair'
import { convertTokenToDecimal, ZERO_BD, ONE_BD, ZERO_BI, ONE_BI, bigDecimalAbs } from './utils'

export function handleSwap(event: SwapEvent): void {
  let pair = Pair.load(event.address.toHexString())
  if (pair === null) return

  let token0 = Token.load(pair.token0)
  let token1 = Token.load(pair.token1)
  if (token0 === null || token1 === null) return

  let bundle = Bundle.load('1')
  if (bundle === null) {
    bundle = new Bundle('1')
    bundle.ethPrice = ZERO_BD
    bundle.save()
  }

  let amount0In = convertTokenToDecimal(event.params.amount0In, BigInt.fromI32(token0.decimals))
  let amount1In = convertTokenToDecimal(event.params.amount1In, BigInt.fromI32(token1.decimals))
  let amount0Out = convertTokenToDecimal(event.params.amount0Out, BigInt.fromI32(token0.decimals))
  let amount1Out = convertTokenToDecimal(event.params.amount1Out, BigInt.fromI32(token1.decimals))

  // Update pair volume
  pair.volumeToken0 = pair.volumeToken0.plus(bigDecimalAbs(amount0In).plus(bigDecimalAbs(amount0Out)))
  pair.volumeToken1 = pair.volumeToken1.plus(bigDecimalAbs(amount1In).plus(bigDecimalAbs(amount1Out)))
  pair.volumeUSD = pair.volumeUSD.plus(bigDecimalAbs(amount0In).plus(bigDecimalAbs(amount0Out)).times(token0.derivedETH.times(bundle.ethPrice)))
  pair.untrackedVolumeUSD = pair.untrackedVolumeUSD.plus(bigDecimalAbs(amount0In).plus(bigDecimalAbs(amount0Out)).times(token0.derivedETH.times(bundle.ethPrice)))
  pair.txCount = pair.txCount.plus(ONE_BI)

  // Update token volume
  token0.volume = token0.volume.plus(bigDecimalAbs(amount0In).plus(bigDecimalAbs(amount0Out)))
  token0.volumeUSD = token0.volumeUSD.plus(bigDecimalAbs(amount0In).plus(bigDecimalAbs(amount0Out)).times(token0.derivedETH.times(bundle.ethPrice)))
  token0.untrackedVolumeUSD = token0.untrackedVolumeUSD.plus(bigDecimalAbs(amount0In).plus(bigDecimalAbs(amount0Out)).times(token0.derivedETH.times(bundle.ethPrice)))
  token0.txCount = token0.txCount.plus(ONE_BI)

  token1.volume = token1.volume.plus(bigDecimalAbs(amount1In).plus(bigDecimalAbs(amount1Out)))
  token1.volumeUSD = token1.volumeUSD.plus(bigDecimalAbs(amount1In).plus(bigDecimalAbs(amount1Out)).times(token1.derivedETH.times(bundle.ethPrice)))
  token1.untrackedVolumeUSD = token1.untrackedVolumeUSD.plus(bigDecimalAbs(amount1In).plus(bigDecimalAbs(amount1Out)).times(token1.derivedETH.times(bundle.ethPrice)))
  token1.txCount = token1.txCount.plus(ONE_BI)

  // Update pair reserves
  let pairContract = UniswapV2Pair.bind(event.address)
  let reserves = pairContract.getReserves()
  pair.reserve0 = convertTokenToDecimal(reserves.value0, BigInt.fromI32(token0.decimals))
  pair.reserve1 = convertTokenToDecimal(reserves.value1, BigInt.fromI32(token1.decimals))
  pair.reserveUSD = pair.reserve0
    .times(token0.derivedETH.times(bundle.ethPrice))
    .plus(pair.reserve1.times(token1.derivedETH.times(bundle.ethPrice)))

  // Create swap event
  let swap = new Swap(event.transaction.hash.toHexString().concat('-').concat(event.logIndex.toString()))
  swap.transaction = event.transaction.hash
  swap.timestamp = event.block.timestamp
  swap.pair = pair.id
  swap.token0 = token0.id
  swap.token1 = token1.id
  swap.amount0In = amount0In
  swap.amount1In = amount1In
  swap.amount0Out = amount0Out
  swap.amount1Out = amount1Out
  swap.amountUSD = bigDecimalAbs(amount0In).plus(bigDecimalAbs(amount0Out)).times(token0.derivedETH.times(bundle.ethPrice))
  swap.logIndex = event.logIndex

  // Save entities
  pair.save()
  token0.save()
  token1.save()
  swap.save()
}

export function handleSync(event: SyncEvent): void {
  let pair = Pair.load(event.address.toHexString())
  if (pair === null) return

  let token0 = Token.load(pair.token0)
  let token1 = Token.load(pair.token1)
  if (token0 === null || token1 === null) return

  let bundle = Bundle.load('1')
  if (bundle === null) {
    bundle = new Bundle('1')
    bundle.ethPrice = ZERO_BD
    bundle.save()
  }

  // Update pair reserves
  pair.reserve0 = convertTokenToDecimal(event.params.reserve0, BigInt.fromI32(token0.decimals))
  pair.reserve1 = convertTokenToDecimal(event.params.reserve1, BigInt.fromI32(token1.decimals))
  pair.reserveUSD = pair.reserve0
    .times(token0.derivedETH.times(bundle.ethPrice))
    .plus(pair.reserve1.times(token1.derivedETH.times(bundle.ethPrice)))

  // Save entities
  pair.save()
}

export function handleTransfer(event: TransferEvent): void {
  let pair = Pair.load(event.address.toHexString())
  if (pair === null) {
    log.warning('Pair not found in handleTransfer: {}', [event.address.toHexString()])
    return
  }

  let pairContract = UniswapV2Pair.bind(event.address)
  let totalSupplyResult = pairContract.try_totalSupply()
  
  if (!totalSupplyResult.reverted) {
    pair.totalSupply = convertTokenToDecimal(totalSupplyResult.value, BigInt.fromI32(18)) // LP tokens have 18 decimals
    pair.save()
  } else {
    log.warning('Failed to get totalSupply for pair: {}', [event.address.toHexString()])
  }
} 