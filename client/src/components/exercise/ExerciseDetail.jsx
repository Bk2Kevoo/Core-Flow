import  {useParams, useNavigate } from 'react-router-dom'
import {useEffect, useState} from 'react'
import styled from 'styled-components'
// import { useOutletContext } from 'react-router-dom'
import toast, { Toaster } from 'react-hot-toast'


function ExerciseDetail() {
    // const { handleEdit, deleteUser } = useOutletContext
    const { exercise, setExercise } = useState({category:[]})

    const { exerciseId } = useParams()
    // const { userId } = useParams()
    const navigate = useNavigate()

    
    useEffect(()=>{
        (async () => {
          const resp = await fetch(`/api/v1/exercises/${exerciseId}`)
          const data = await resp.json()
          if (resp.ok) {
            setExercise(data)
          } else {
            toast.error(data.error)
          }
        })()
      }, [exerciseId])

    const {id, name, body_part, image, category} = exercise

    return(
      <CardDetail id={id}>
        <h1>{name}</h1>
          <div className='wrapper'>
            <div>
              <h3>Body Part:</h3>
              <p>{body_part}</p>
              <h2>Category</h2>
              <ul>
                {category.map(cat => <li key={cat.id}>{`${cat.name}`}</li>)}
              </ul>
            </div>
            <img src={image} alt ={name}/>
          </div>

      </CardDetail>
    )
}

export default ExerciseDetail

const CardDetail = styled `
    display:flex;

`