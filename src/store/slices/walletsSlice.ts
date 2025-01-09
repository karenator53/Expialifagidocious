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
    return await api.addWallet(wallet);
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
      });
  },
})

export const { setSelectedGroup } = walletsSlice.actions
export default walletsSlice.reducer