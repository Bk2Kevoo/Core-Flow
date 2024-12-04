import { useParams } from 'react-router-dom'
import { useEffect, useState } from 'react'
import styled from 'styled-components'
import toast from 'react-hot-toast'

function WorkoutDetail() {
    const [workout, setWorkout] = useState({ work_exercise: [] })

    const { workoutId } = useParams()

    useEffect(() => {
        (async () => {
            const resp = await fetch(`/api/v1/workouts/${workoutId}`)
            const data = await resp.json()
            if (resp.ok) {
                setWorkout(data)
            } else {
                toast.error(data.error)
            }
        })()
    }, [workoutId])


    const { id, name, date } = workout

    return (
        <CardDetail id={id}>
        <h1>{title}</h1>
            <div className='wrapper'>
            <div>
                <p>{name}</p>
                <p>{date}</p>
                <ul>
                {workout.map(workout => ( <li key={workout.id}>{`${workout.name}`}</li>))}
                </ul>
            </div>
            <img src={image} alt={title}/>
            </div>
        </CardDetail>
    )
}

export default WorkoutDetail

const CardDetail = styled