import { useEffect, useState } from "react";
import toast from 'react-hot-toast';
import { useOutletContext, useParams } from "react-router-dom";
import styled from 'styled-components'
import Exercise from "../exercise/ExerciseCard"

function Category() {
  const [category, setCategory] = useState({ exercises: [] });  // Ensure `exercises` is always an array
  const { currentUser } = useOutletContext()
  const { categoryId } = useParams();

  useEffect(() => {
    (async () => {
        const resp = await fetch(`/api/v1/categories/${categoryId}`);
        const data = await resp.json()
        if (resp.ok) {
          setCategory(data)
        } else {
            toast.error(data.error)
        }
    })();
  }, [categoryId]);

  const { id, name, exercises } = category;  // Ensure exercises is destructured

  return(
    <CardDetail id={id}>
      <h1>{name}</h1>
        <div className='wrapper'>
          <div>
            <h3>Of Type:</h3>
            <p>{name}</p>
            <h2>Exercises</h2>
            <ul>
            {currentUser && Array.isArray(exercises) && exercises.length > 0 ? (
                exercises.map(exer => <Exercise key={exer.id} exercise={exer} />)
            ) : (
                <p>Must Login to View the specific cateegory 😊</p>
            )}
            </ul>
          </div>
        </div>
    </CardDetail>
  )
}

export default Category;

const CardDetail = styled.div`
  display: flex;
  flex-direction: column;
  padding: 20px;
  border-radius: 15px;
  max-width: 800px;
  margin: 20px auto;
  background-color: #f7f7f7; /* Soft background color */
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1); /* Soft shadow effect */
  transition: transform 0.3s ease-in-out; /* Hover effect for card */
  &:hover {
    transform: scale(1.03); /* Slightly enlarge on hover */
  }

  h1 {
    font-size: 28px;
    color: #2c3e50;
    font-weight: 600;
    text-align: center;
  }

  .wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 20px;
  }

  h2 {
    font-size: 22px;
    margin-top: 10px;
    color: #34495e;
    font-weight: 500;
  }

  ul {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 15px;
    margin-top: 15px;
    padding: 0;
    list-style-type: none;
  }

  li {
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #fff;
    border-radius: 10px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    padding: 15px;
    transition: transform 0.3s ease-in-out; /* Hover effect for exercises */
  }

  li:hover {
    transform: translateY(-5px); /* Lift up on hover */
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
  }

  p {
    color: #e74c3c;
    font-size: 18px;
    text-align: center;
    margin-top: 20px;
  }
`;