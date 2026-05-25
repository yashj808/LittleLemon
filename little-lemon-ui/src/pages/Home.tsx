import React from 'react';
import { Link } from 'react-router-dom';
import styles from './Home.module.css';

const Home: React.FC = () => {
  return (
    <div className={styles.container}>
      <section className={styles.hero}>
        <h1>Little Lemon</h1>
        <h2>Chicago</h2>
        <p>
          We are a family owned Mediterranean restaurant, focused on traditional recipes served with a modern twist.
        </p>
        <Link to="/book" className={styles.ctaBtn}>Reserve a Table</Link>
      </section>

      <section className={styles.features}>
        <div className={styles.featureCard}>
          <h3>Fresh Ingredients</h3>
          <p>We use only the finest ingredients sourced from local farms.</p>
        </div>
        <div className={styles.featureCard}>
          <h3>Authentic Flavors</h3>
          <p>Our recipes have been passed down through generations.</p>
        </div>
        <div className={styles.featureCard}>
          <h3>Modern Ambiance</h3>
          <p>Enjoy your meal in our beautifully designed dining area.</p>
        </div>
      </section>
    </div>
  );
};

export default Home;
