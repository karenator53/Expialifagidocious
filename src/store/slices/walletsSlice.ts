import { createSlice, PayloadAction, createAsyncThunk } from '@reduxjs/toolkit'
import * as api from '../../services/api'
import { sonicApi } from '../../services/sonicApi'

export type Wallet = api.Wallet;

interface WalletsState {
  items: Wallet[]
  loading: boolean
  error: string | null,
  selectedGroup: string | null
}

const initialState: WalletsState = {
  items: [],
  loading: false,
  error: null,
  selectedGroup: null,
}

export const fetchWallets = createAsyncThunk(
  'wallets/fetchWallets',
  async () => {
    return await api.fetchWallets();
  }
);

export const addWalletAsync = createAsyncThunk(
  'wallets/addWallet',
  async (wallet: Omit<Wallet, 'id' | 'created_at' | 'updated_at'>) => {
    // First add the wallet to the database
    const newWallet = await api.addWallet(wallet);
    
    // Then fetch its Sonic data
    const [balance, transactions, price] = await Promise.all([
      sonicApi.getWalletBalance(wallet.address),
      sonicApi.getTransactions(wallet.address),
      sonicApi.getTokenPrice()
    ]);

    // Combine the data
    return {
      ...newWallet,
      balance,
      transactions,
      currentPrice: price,
      lastUpdated: Date.now()
    };
  }
);

export const deleteWalletAsync = createAsyncThunk(
  'wallets/deleteWallet',
  async (id: string) => {
    await api.deleteWallet(id);
    return id;
  }
);

export const fetchWalletData = createAsyncThunk(
  'wallets/fetchWalletData',
  async (address: string) => {
    const [balance, transactions, price] = await Promise.all([
      sonicApi.getWalletBalance(address),
      sonicApi.getTransactions(address),
      sonicApi.getTokenPrice()
    ]);

    return {
      address,
      balance,
      transactions,
      currentPrice: price,
      lastUpdated: Date.now()
    };
  }
);

// Add a thunk to refresh wallet data
export const refreshWalletData = createAsyncThunk(
  'wallets/refreshData',
  async (wallet: Wallet) => {
    const [balance, transactions, price] = await Promise.all([
      sonicApi.getWalletBalance(wallet.address),
      sonicApi.getTransactions(wallet.address),
      sonicApi.getTokenPrice()
    ]);

    // Update the wallet in the database
    const updatedWallet = await api.updateWallet(wallet.id, {
      ...wallet,
      balance,
      currentPrice: price,
      transactions,
      lastUpdated: Date.now()
    });

    return updatedWallet;
  }
);

const walletsSlice = createSlice({
  name: 'wallets',
  initialState,
  reducers: {
    setSelectedGroup: (state, action: PayloadAction<string | null>) => {
      state.selectedGroup = action.payload
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchWallets.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(fetchWallets.fulfilled, (state, action) => {
        state.loading = false;
        state.items = action.payload;
      })
      .addCase(fetchWallets.rejected, (state, action) => {
        state.loading = false;
        state.error = action.error.message || 'Failed to fetch wallets';
      })
      .addCase(addWalletAsync.fulfilled, (state, action) => {
        state.items.push(action.payload);
      })
      .addCase(deleteWalletAsync.fulfilled, (state, action) => {
        state.items = state.items.filter(wallet => wallet.id !== action.payload);
      })
      .addCase(fetchWalletData.pending, (state) => {
        state.loading = true;
      })
      .addCase(fetchWalletData.fulfilled, (state, action) => {
        state.loading = false;
        const index = state.items.findIndex(w => w.address === action.payload.address);
        if (index >= 0) {
          state.items[index] = action.payload;
        } else {
          state.items.push(action.payload);
        }
      })
      .addCase(fetchWalletData.rejected, (state, action) => {
        state.loading = false;
        state.error = action.error.message;
      })
      .addCase(refreshWalletData.fulfilled, (state, action) => {
        const index = state.items.findIndex(w => w.id === action.payload.id);
        if (index >= 0) {
          state.items[index] = action.payload;
        }
      });
  },
})

export const { setSelectedGroup } = walletsSlice.actions
export default walletsSlice.reducer