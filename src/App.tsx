import { Routes, Route } from 'react-router-dom'
import Layout from './components/Layout'
import Dashboard from './pages/Dashboard'
import WalletGroups from './pages/WalletGroups'
import NotFound from './pages/NotFound'

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<Layout />}>
        <Route index element={<Dashboard />} />
        <Route path="groups" element={<WalletGroups />} />
        <Route path="*" element={<NotFound />} />
      </Route>
    </Routes>
  )
}