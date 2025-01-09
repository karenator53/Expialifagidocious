import { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import type { AppDispatch, RootState } from '../store'
import { fetchWallets, deleteWalletAsync } from '../store/slices/walletsSlice'
import AddWalletForm from '../components/AddWalletForm'
import { createSprite } from '../components/Sprites'

export default function Dashboard() {
  const dispatch = useDispatch<AppDispatch>()
  const { items: wallets, loading, error } = useSelector(
    (state: RootState) => state.wallets
  )

  useEffect(() => {
    dispatch(fetchWallets())
  }, [dispatch])

  const handleDeleteWallet = (id: string, event: React.MouseEvent<HTMLButtonElement>) => {
    const button = event.currentTarget;
    const rect = button.getBoundingClientRect();
    
    // Create burst effect at button position
    createSprite('burst', rect.x + rect.width / 2, rect.y + rect.height / 2);
    
    dispatch(deleteWalletAsync(id));
  };


  if (loading) return <div>Loading...</div>
  if (error) return <div>Error: {error}</div>

  return (
    <div className="dashboard">
      <h1>Dashboard</h1>
      <AddWalletForm />
      {wallets.length === 0 ? (
        <p className="text-secondary">No wallets added yet.</p>
      ) : (
        <div className="wallet-grid">
          {wallets.map((wallet) => (
            <div key={wallet.id} className="card">
              <h3>{wallet.chain.toUpperCase()} Wallet</h3>
              <p>Address: {wallet.address.slice(0, 6)}...{wallet.address.slice(-4)}</p>
              <p>Balance: {wallet.balance} {wallet.chain.toUpperCase()}</p>
              <button
                onClick={(e) => handleDeleteWallet(wallet.id, e)}
                className="button button--delete"
              >
                Remove Wallet
              </button>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}