import { useEffect, useState } from 'react';
import styled from 'styled-components';
import toast from 'react-hot-toast';
import { Link } from 'react-router-dom';

function CategoriesList() {
  const [categories, setCategories] = useState([]);

  useEffect(() => {
    (async () => {
      const resp = await fetch('/api/v1/categories');
      const data = await resp.json();

      if (resp.ok) {
        setCategories(data);
      } else {
        toast.error(data.error);
      }
    })();
  }, []);

  return (
    <CategoriesContainer>
      <h1>Categories</h1>
      <ul>
        {categories.map((category) => (
          <CategoryCard key={category.id}>
            <Link to={`/categories/${category.id}`}>
              <h2>{category.name}</h2>
            </Link>
          </CategoryCard>
        ))}
      </ul>
    </CategoriesContainer>
  );
}

export default CategoriesList;

const CategoriesContainer = styled.div`
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;

  h1 {
    text-align: center;
    color: #333;
    font-size: 28px;
  }

  ul {
    list-style: none;
    padding: 0;
  }
`;

const CategoryCard = styled.li`
  margin: 10px 0;
  padding: 15px;
  border: 1px solid #ddd;
  border-radius: 8px;
  transition: background-color 0.3s, transform 0.3s;

  &:hover {
    background-color: #f5f5f5;
    transform: translateY(-3px);
  }

  a {
    text-decoration: none;
    color: #007bff;
  }

  h2 {
    margin: 0;
    font-size: 20px;
  }
`;
