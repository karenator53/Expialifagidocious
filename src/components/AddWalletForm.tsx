import { useState } from 'react'
import { useDispatch } from 'react-redux'
import { addWalletAsync } from '../store/slices/walletsSlice'
import { createSprite } from './Sprites'
import type { AppDispatch } from '../store'

export default function AddWalletForm() {
  const dispatch = useDispatch<AppDispatch>()
  const [address, setAddress] = useState('')
  const [chain, setChain] = useState<'sonic' | 'base' | 'solana'>('sonic')

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    
    if (!address.trim()) return

    dispatch(addWalletAsync({
      name: `Wallet ${address.slice(0, 6)}`,
      address: address.trim(),
      group: chain.toUpperCase(),
      balance: 0
    }))

    // Create multiple sparkles around the form
    const formElement = document.querySelector('.form');
    if (formElement) {
      const rect = formElement.getBoundingClientRect();
      for (let i = 0; i < 5; i++) {
        createSprite('sparkle', rect.x + Math.random() * rect.width, rect.y + Math.random() * rect.height);
      }
    }

    setAddress('')
    setChain('sonic')
  }

  return (
    <form onSubmit={handleSubmit} className="form">
      <div className="form__group">
        <label htmlFor="address" className="form__label">
          Wallet Address
        </label>
        <input
          id="address"
          type="text"
          className="form__input"
          value={address}
          onChange={(e) => setAddress(e.target.value)}
          placeholder="Enter wallet address"
          required
        />
      </div>
      <div className="form__group">
        <label htmlFor="chain" className="form__label">
          Blockchain
        </label>
        <select
          id="chain"
          className="form__select"
          value={chain}
          onChange={(e) => setChain(e.target.value as 'sonic' | 'base' | 'solana')}
        >
          <option value="sonic">Sonic</option>
          <option value="base">Base</option>
          <option value="solana">Solana</option>
        </select>
      </div>
      <button type="submit" className="button">
        Add Wallet
      </button>
    </form>
  )
}