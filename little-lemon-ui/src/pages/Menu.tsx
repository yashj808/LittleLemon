import React, { useEffect, useState } from 'react';
import api from '../services/api';
import { useCart } from '../context/CartContext';
import styles from './Menu.module.css';

interface MenuItem {
  id: number;
  title: string;
  price: string;
  stock: number;
  category: {
    title: string;
  };
}

const Menu: React.FC = () => {
  const [items, setItems] = useState<MenuItem[]>([]);
  const [loading, setLoading] = useState(true);
  const { addToCart } = useCart();

  useEffect(() => {
    const fetchMenu = async () => {
      try {
        const response = await api.get('/api/menu-items/');
        setItems(response.data.results || response.data);
      } catch (err) {
        console.error('Error fetching menu:', err);
      } finally {
        setLoading(false);
      }
    };
    fetchMenu();
  }, []);

  if (loading) return <div className={styles.loader}>Loading our delicious menu...</div>;

  return (
    <div>
      <h1 style={{ color: '#495e57', textAlign: 'center' }}>Our Menu</h1>
      <div className={styles.menuGrid}>
        {items.map((item) => (
          <div key={item.id} className={styles.card}>
            <div className={styles.cardContent}>
              <span className={styles.category}>{item.category?.title || 'General'}</span>
              <h3>{item.title}</h3>
              <p className={styles.price}>${item.price}</p>
              <p className={styles.stock}>
                In stock: <span className={styles.stockSpan}>{item.stock}</span>
              </p>
              <button 
                className={styles.orderBtn}
                onClick={() => addToCart(item)}
              >
                Order Now
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Menu;
