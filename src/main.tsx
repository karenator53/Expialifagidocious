import React from 'react'
import ReactDOM from 'react-dom/client'
import { Provider } from 'react-redux'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import App from './App'
import { store } from './store'
import './styles/main.scss'

// Import your components
import Layout from './components/Layout'
import Dashboard from './pages/Dashboard'
import WalletGroups from './pages/WalletGroups'
import NotFound from './pages/NotFound'

const router = createBrowserRouter([
  {
    path: "/",
    element: <Layout />,
    children: [
      {
        index: true,
        element: <Dashboard />
      },
      {
        path: "groups",
        element: <WalletGroups />
      },
      {
        path: "*",
        element: <NotFound />
      }
    ]
  }
], {
  future: {
    v7_startTransition: true,
    v7_relativeSplatPath: true
  }
});

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <Provider store={store}>
      <RouterProvider router={router} />
    </Provider>
  </React.StrictMode>,
)