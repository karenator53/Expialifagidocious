import axios from 'axios';

const BASE_URL = 'https://api.sonicscan.org/api';
const API_KEY = 'V7B8Q64VHUQF2SJY5FI8PTATANCFCIAVHQ';

interface TokenPosition {
  id: string;
  symbol: string;
  amount: number;
  averagePrice: number;
  currentPrice: number;
  profitLoss: number;
  profitLossPercentage: number;
}

interface Transaction {
  hash: string;
  timestamp: number;
  type: 'buy' | 'sell';
  tokenSymbol: string;
  amount: number;
  price: number;
}

export const sonicApi = {
  async getWalletBalance(address: string): Promise<number> {
    try {
      const response = await axios.get(`${BASE_URL}`, {
        params: {
          module: 'account',
          action: 'balance',
          address,
          tag: 'latest',
          apikey: API_KEY
        }
      });
      return Number(response.data.result) / 1e18;
    } catch (error) {
      console.error('Error fetching wallet balance:', error);
      throw error;
    }
  },

  async getTransactions(address: string): Promise<Transaction[]> {
    try {
      const response = await axios.get(`${BASE_URL}`, {
        params: {
          module: 'account',
          action: 'txlist',
          address,
          startblock: 0,
          endblock: 99999999,
          page: 1,
          offset: 100,
          sort: 'desc',
          apikey: API_KEY
        }
      });

      return response.data.result.map((tx: any) => ({
        hash: tx.hash,
        timestamp: Number(tx.timeStamp) * 1000,
        type: tx.from.toLowerCase() === address.toLowerCase() ? 'sell' : 'buy',
        tokenSymbol: 'SONIC',
        amount: Number(tx.value) / 1e18,
        price: 1 // You might want to fetch historical prices
      }));
    } catch (error) {
      console.error('Error fetching transactions:', error);
      throw error;
    }
  },

  async getTokenPrice(): Promise<number> {
    try {
      const response = await axios.get(`${BASE_URL}`, {
        params: {
          module: 'stats',
          action: 'ethprice',
          apikey: API_KEY
        }
      });
      return Number(response.data.result.ethusd);
    } catch (error) {
      console.error('Error fetching token price:', error);
      throw error;
    }
  }
}; 