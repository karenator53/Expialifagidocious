import { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchWalletData } from '../store/slices/walletsSlice';
import { WalletCard } from '../components/WalletCard';
import type { RootState } from '../store';

export default function WalletGroups() {
  const dispatch = useDispatch();
  const { items: wallets, loading, selectedGroup } = useSelector((state: RootState) => state.wallets);

  useEffect(() => {
    // Fetch data for each wallet
    wallets.forEach(wallet => {
      if (!wallet.lastUpdated || Date.now() - wallet.lastUpdated > 300000) { // 5 minutes
        dispatch(fetchWalletData(wallet.address));
      }
    });
  }, [dispatch, wallets]);

  const filteredWallets = selectedGroup 
    ? wallets.filter(w => w.group === selectedGroup)
    : wallets;

  if (loading) return <div className="loading">Loading...</div>;

  return (
    <div className="wallet-groups">
      <div className="wallet-grid">
        {filteredWallets.map(wallet => (
          <WalletCard key={wallet.id} wallet={wallet} />
        ))}
      </div>
    </div>
  );
}