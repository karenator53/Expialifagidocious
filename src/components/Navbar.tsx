import { Link } from 'react-router-dom'

export default function Navbar() {
  return (
    <nav className="navbar">
      <div className="container">
        <Link to="/" className="navbar__brand">
          Expialifagidocious Wallet Tracker
        </Link>
        <div className="navbar__links">
          <Link to="/">Dashboard</Link>
          <Link to="/groups">Wallet Groups</Link>
        </div>
      </div>
    </nav>
  )
}