import React, { useEffect, useState } from 'react';
import api from '../services/api';

const Manager: React.FC = () => {
  const [message, setMessage] = useState('Checking access...');
  const [isAuthorized, setIsAuthorized] = useState(false);

  useEffect(() => {
    const checkManagerAccess = async () => {
      try {
        const response = await api.get('/api/manager-view/');
        setMessage(response.data.message);
        setIsAuthorized(true);
      } catch (err: any) {
        setMessage(err.response?.data?.message || 'Access Denied');
        setIsAuthorized(false);
      }
    };
    checkManagerAccess();
  }, []);

  return (
    <div style={{ textAlign: 'center', padding: '2rem' }}>
      <h1 style={{ color: '#495e57' }}>Manager Dashboard</h1>
      <div style={{ 
        marginTop: '2rem', 
        padding: '2rem', 
        backgroundColor: isAuthorized ? '#d4edda' : '#f8d7da',
        color: isAuthorized ? '#155724' : '#721c24',
        borderRadius: '8px',
        border: `1px solid ${isAuthorized ? '#c3e6cb' : '#f5c6cb'}`
      }}>
        <h2>{message}</h2>
        {!isAuthorized && (
          <p>You must be part of the "Manager" group to view this dashboard.</p>
        )}
      </div>
    </div>
  );
};

export default Manager;
