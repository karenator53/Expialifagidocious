import { useSelector } from 'react-redux';
import type { RootState } from '../store';

export default function Dashboard() {
  const { items: wallets } = useSelector((state: RootState) => state.wallets);

  // Group wallets by their group
  const walletsByGroup = wallets.reduce((acc, wallet) => {
    const group = wallet.group || 'Ungrouped'; // Provide default group if undefined
    if (!acc[group]) {
      acc[group] = [];
    }
    acc[group].push(wallet);
    return acc;
  }, {} as Record<string, typeof wallets>);

  return (
    <div className="dashboard">
      <h1>Dashboard</h1>
      
      {Object.entries(walletsByGroup).map(([group, groupWallets]) => (
        <div key={group} className="wallet-group">
          <h2>{group.toUpperCase()}</h2>
          <div className="wallet-stats">
            <div className="stat">
              <label>Total Wallets</label>
              <value>{groupWallets.length}</value>
            </div>
            <div className="stat">
              <label>Total Balance</label>
              <value>
                {groupWallets.reduce((sum, w) => sum + (w.balance || 0), 0).toFixed(4)} SONIC
              </value>
            </div>
            <div className="stat">
              <label>Total Value</label>
              <value>
                ${groupWallets
                  .reduce((sum, w) => sum + (w.balance || 0) * (w.currentPrice || 0), 0)
                  .toFixed(2)}
              </value>
            </div>
          </div>
        </div>
      ))}
    </div>
  );
}