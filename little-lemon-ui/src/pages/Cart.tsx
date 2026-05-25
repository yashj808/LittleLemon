import React from 'react';
import { useCart } from '../context/CartContext';
import styles from './Menu.module.css'; // Reusing Menu grid for items

const Cart: React.FC = () => {
  const { cart, removeFromCart, clearCart, totalPrice } = useCart();

  const handleCheckout = () => {
    alert('Thank you for your order! This is a prototype checkout.');
    clearCart();
  };

  if (cart.length === 0) {
    return (
      <div style={{ textAlign: 'center', padding: '4rem' }}>
        <h2>Your cart is empty</h2>
        <p>Go to the menu to add some delicious items!</p>
      </div>
    );
  }

  return (
    <div style={{ maxWidth: '800px', margin: '0 auto' }}>
      <h1 style={{ textAlign: 'center', color: '#495e57' }}>Your Cart</h1>
      <div style={{ backgroundColor: 'white', padding: '2rem', borderRadius: '12px', boxShadow: '0 4px 6px rgba(0,0,0,0.1)' }}>
        {cart.map((item) => (
          <div key={item.id} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '1rem 0', borderBottom: '1px solid #edefee' }}>
            <div>
              <h3 style={{ margin: 0 }}>{item.title} x {item.quantity}</h3>
              <p style={{ margin: '0.25rem 0 0', color: '#666' }}>${item.price} each</p>
            </div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '1rem' }}>
              <span style={{ fontWeight: 'bold' }}>${(parseFloat(item.price) * item.quantity).toFixed(2)}</span>
              <button 
                onClick={() => removeFromCart(item.id)}
                style={{ background: 'none', border: '1px solid #d9534f', color: '#d9534f', padding: '0.25rem 0.5rem', borderRadius: '4px', cursor: 'pointer' }}
              >
                Remove
              </button>
            </div>
          </div>
        ))}
        <div style={{ marginTop: '2rem', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <h2>Total: ${totalPrice.toFixed(2)}</h2>
          <div style={{ display: 'flex', gap: '1rem' }}>
            <button 
              onClick={clearCart}
              style={{ padding: '0.75rem 1.5rem', borderRadius: '6px', border: '1px solid #ccc', background: 'white', cursor: 'pointer' }}
            >
              Clear Cart
            </button>
            <button 
              onClick={handleCheckout}
              style={{ padding: '0.75rem 1.5rem', borderRadius: '6px', border: 'none', background: '#495e57', color: '#f4ce14', fontWeight: 'bold', cursor: 'pointer' }}
            >
              Checkout
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Cart;
