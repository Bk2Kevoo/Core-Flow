import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";

function Category() {
  const [categories, setCategories] = useState({exercises:[]});
  
  const { categoryId } = useParams

  useEffect(() => {
    (async () => {
        const resp = await fetch(`api/v1/categories/${categoryId}`)
        const data = await resp.json()
        if (resp.ok) {
            setCategories(data)
        } else {
            toast.error(data.error)
        }
        })()
  }, [categoryId])

  const {id, name, exercise} = categories

  return(
    <CardDetail id={id}>
      <h1>{name}</h1>
        <div className='wrapper'>
          <div>
            <h3>Name:</h3>
            <p>{name}</p>
            <h2>Exercises</h2>
            <ul>
              {exercise.map(exer => <li key={exer.id}>{`${exer.name}`}</li>)}
            </ul>
          </div>
        </div>

    </CardDetail>
  )
}

export default Category