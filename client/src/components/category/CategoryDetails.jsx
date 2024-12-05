import { useEffect, useState } from "react";
import toast from 'react-hot-toast';
import { useOutletContext, useParams } from "react-router-dom";
import styled from 'styled-components'
import Exercise from "../exercise/ExerciseCard"

function Category() {
  const [category, setCategory] = useState({ exercise: [] });
  const { currentUser } = useOutletContext()
  const { categoryId } = useParams();

  useEffect(() => {
    (async () => {
        const resp = await fetch(`api/v1/categories/${categoryId}`);
        const data = await resp.json()
        if (resp.ok) {
          setCategory(data)
        } else {
            toast.error(data.error)
        }
        })();
  }, [categoryId])

  const {id, name,} = category

  return(
    <CardDetail id={id}>
      <h1>{name}</h1>
        <div className='wrapper'>
          <div>
            <h3>Name:</h3>
            <p>{name}</p>
            <h2>Exercises</h2>
            <ul>
              {currentUser && category.exercise.map(exer => <Exercise key={exer.id} category={exer}/>)}
            </ul>
          </div>
        </div>

    </CardDetail>
  )
}

export default Category

const CardDetail = styled.div`
  display: flex;
  flex-direction: column;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  max-width: 600px;
  margin: 0 auto;

  h1 {
    font-size: 24px;
    color: #333;
}
    `

