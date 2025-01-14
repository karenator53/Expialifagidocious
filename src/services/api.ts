const API_BASE_URL = 'http://localhost:8000/api';

export interface Wallet {
  id: string;
  name: string;
  address: string;
  group: string;
  created_at: string;
  updated_at: string;
  balance?: number;
  currentPrice?: number;
  transactions?: {
    hash: string;
    timestamp: number;
    type: 'buy' | 'sell';
    tokenSymbol: string;
    amount: number;
    price: number;
  }[];
  lastUpdated?: number;
}

export async function fetchWallets(): Promise<Wallet[]> {
  const response = await fetch(`${API_BASE_URL}/wallets`);
  if (!response.ok) {
    throw new Error('Failed to fetch wallets');
  }
  return response.json();
}

export async function addWallet(wallet: Omit<Wallet, 'id' | 'created_at' | 'updated_at'>): Promise<Wallet> {
  const response = await fetch(`${API_BASE_URL}/wallets`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(wallet),
  });
  if (!response.ok) {
    throw new Error('Failed to add wallet');
  }
  return response.json();
}

export async function deleteWallet(id: string): Promise<void> {
  const response = await fetch(`${API_BASE_URL}/wallets/${id}`, {
    method: 'DELETE',
  });
  if (!response.ok) {
    throw new Error('Failed to delete wallet');
  }
}