import { Wallet } from '../services/api';
import { useDispatch } from 'react-redux';
import { refreshWalletData } from '../store/slices/walletsSlice';

interface WalletCardProps {
  wallet: Wallet;
}

export function WalletCard({ wallet }: WalletCardProps) {
  const dispatch = useDispatch();
  const timeAgo = wallet.lastUpdated ? new Date(wallet.lastUpdated).toLocaleString() : 'Never';

  return (
    <div className="wallet-card">
      <div className="wallet-card-header">
        <h3>{wallet.name}</h3>
        <span className="wallet-address">{wallet.address}</span>
        <span className="wallet-group">{wallet.group}</span>
      </div>
      
      <div className="wallet-stats">
        <div className="stat">
          <label>Balance:</label>
          <value>{wallet.balance?.toFixed(4) || '0'} SONIC</value>
        </div>
        
        <div className="stat">
          <label>Value:</label>
          <value>${((wallet.balance || 0) * (wallet.currentPrice || 0)).toFixed(2)}</value>
        </div>
        
        <div className="last-updated">
          Last updated: {timeAgo}
          <button onClick={() => dispatch(refreshWalletData(wallet))}>
            Refresh
          </button>
        </div>
      </div>

      <div className="recent-transactions">
        <h4>Recent Transactions</h4>
        <div className="transactions-list">
          {wallet.transactions?.slice(0, 5).map(tx => (
            <div key={tx.hash} className="transaction">
              <span className={`type ${tx.type}`}>
                {tx.type === 'buy' ? '↓' : '↑'}
              </span>
              <span className="amount">{tx.amount.toFixed(4)} SONIC</span>
              <span className="date">
                {new Date(tx.timestamp).toLocaleDateString()}
              </span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
} 