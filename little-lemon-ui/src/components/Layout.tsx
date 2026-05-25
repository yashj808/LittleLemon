import React from 'react';
import { Link, Outlet, useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { useCart } from '../context/CartContext';
import styles from './Layout.module.css';

const Layout: React.FC = () => {
  const { isAuthenticated, logout } = useAuth();
  const { totalItems } = useCart();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  return (
    <div>
      <nav className={styles.navbar}>
        <div className={styles.logo}>Little Lemon</div>
        <div className={styles.navLinks}>
          <Link to="/">Home</Link>
          <Link to="/menu">Menu</Link>
          <Link to="/book">Reservations</Link>
          <Link to="/cart" className={styles.cartLink}>
            Cart ({totalItems})
          </Link>
          {isAuthenticated ? (
            <>
              <Link to="/manager">Manager</Link>
              <button onClick={handleLogout} className={styles.logoutBtn}>Logout</button>
            </>
          ) : (
            <>
              <Link to="/login">Login</Link>
              <Link to="/register">Register</Link>
            </>
          )}
        </div>
      </nav>
      <main className={styles.mainContent}>
        <Outlet />
      </main>
    </div>
  );
};

export default Layout;
