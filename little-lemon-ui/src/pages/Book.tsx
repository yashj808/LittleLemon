import React, { useState } from 'react';
import styles from './Auth.module.css'; // Reusing Auth styles for consistent look

const Book: React.FC = () => {
  const [name, setName] = useState('');
  const [date, setDate] = useState('');
  const [time, setTime] = useState('');
  const [guests, setGuests] = useState(2);
  const [submitted, setSubmitted] = useState(false);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setSubmitted(true);
  };

  if (submitted) {
    return (
      <div className={styles.authContainer} style={{ textAlign: 'center' }}>
        <h2>Reservation Confirmed!</h2>
        <p>Thank you, {name}. We look forward to seeing you on {date} at {time} for {guests} guests.</p>
        <button className={styles.submitBtn} onClick={() => setSubmitted(false)}>Make Another Reservation</button>
      </div>
    );
  }

  return (
    <div className={styles.authContainer}>
      <h2>Reserve a Table</h2>
      <form onSubmit={handleSubmit}>
        <div className={styles.formGroup}>
          <label>Name</label>
          <input type="text" value={name} onChange={(e) => setName(e.target.value)} required />
        </div>
        <div className={styles.formGroup}>
          <label>Date</label>
          <input type="date" value={date} onChange={(e) => setDate(e.target.value)} required />
        </div>
        <div className={styles.formGroup}>
          <label>Time</label>
          <input type="time" value={time} onChange={(e) => setTime(e.target.value)} required />
        </div>
        <div className={styles.formGroup}>
          <label>Number of Guests</label>
          <input type="number" min="1" max="10" value={guests} onChange={(e) => setGuests(parseInt(e.target.value))} required />
        </div>
        <button type="submit" className={styles.submitBtn}>Book Now</button>
      </form>
    </div>
  );
};

export default Book;
