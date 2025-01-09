import { configureStore } from '@reduxjs/toolkit'
import walletsReducer from './slices/walletsSlice'

export const store = configureStore({
  reducer: {
    wallets: walletsReducer,
  },
})

export type RootState = ReturnType<typeof store.getState>
export type AppDispatch = typeof store.dispatch