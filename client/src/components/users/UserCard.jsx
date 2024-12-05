import { useEffect, useState } from 'react';
import styled from 'styled-components';
import toast from 'react-hot-toast';
import { useNavigate } from 'react-router-dom';

function DeleteUserPage() {
  const [user, setUser] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    (async () => {
      const resp = await fetch('/api/v1/delete-account');
      const data = await resp.json();

      if (resp.ok) {
        setUser(data);
      } else {
        toast.error(data.error || 'Error fetching user details');
      }
    })();
  }, []);

  const handleDeleteUser = async () => {
    const resp = await fetch('/api/v1/delete-account', { method: 'DELETE' });

    if (resp.ok) {
      toast.success('User deleted successfully');
      navigate('/'); // Redirect to a goodbye or home page after deletion
    } else {
      const data = await resp.json();
      toast.error(data.error || 'Error deleting user');
    }
  };

  if (!user) {
    return <LoadingMessage>Loading user details...</LoadingMessage>;
  }

  return (
    <DeleteUserContainer>
      <h1>Delete Your Account</h1>
      <UserDetails>
        <p><strong>Name:</strong> {user.name}</p>
        <p><strong>Email:</strong> {user.email}</p>
      </UserDetails>
      <DeleteButton onClick={handleDeleteUser}>Delete Account</DeleteButton>
      <CancelButton onClick={() => navigate('/')}>Cancel</CancelButton>
    </DeleteUserContainer>
  );
}

export default DeleteUserPage;

const DeleteUserContainer = styled.div`
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  text-align: center;

  h1 {
    color: #333;
    font-size: 28px;
    margin-bottom: 20px;
  }
`;

const UserDetails = styled.div`
  margin-bottom: 20px;
  text-align: left;

  p {
    font-size: 16px;
    margin: 5px 0;
  }
`;

const DeleteButton = styled.button`
  background-color: #e74c3c;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  font-size: 16px;
  cursor: pointer;
  margin-right: 10px;

  &:hover {
    background-color: #c0392b;
  }
`;

const CancelButton = styled.button`
  background-color: #95a5a6;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  font-size: 16px;
  cursor: pointer;

  &:hover {
    background-color: #7f8c8d;
  }
`;

const LoadingMessage = styled.div`
  text-align: center;
  font-size: 18px;
  color: #333;
`;
