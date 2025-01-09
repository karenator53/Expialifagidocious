import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchWalletData } from '../store/slices/walletsSlice';

export default function WalletGroups() {
  const dispatch = useDispatch();
  const { wallets, loading } = useSelector((state: RootState) => state.wallets);

  useEffect(() => {
    // Fetch data for each wallet
    wallets.forEach(wallet => {
      dispatch(fetchWalletData(wallet.address));
    });
  }, [dispatch, wallets]);

  if (loading) return <div>Loading...</div>;

  return (
    <div className="wallet-groups">
      {wallets.map(wallet => (
        <div key={wallet.address} className="wallet-card">
          <h3>Wallet {wallet.address}</h3>
          <div className="wallet-stats">
            <p>Balance: {wallet.balance?.toFixed(4)} SONIC</p>
            <p>Value: ${(wallet.balance * wallet.currentPrice)?.toFixed(2)}</p>
            <h4>Recent Transactions</h4>
            <div className="transactions">
              {wallet.transactions?.slice(0, 5).map(tx => (
                <div key={tx.hash} className="transaction">
                  <span>{tx.type === 'buy' ? '↓' : '↑'}</span>
                  <span>{tx.amount.toFixed(4)} SONIC</span>
                  <span>{new Date(tx.timestamp).toLocaleDateString()}</span>
                </div>
              ))}
            </div>
          </div>
        </div>
      ))}
    </div>
  );
}