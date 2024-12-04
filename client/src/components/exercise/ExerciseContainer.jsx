// import styled from 'styled-components'
import ExerciseCard from './ExerciseCard'
import { useOutletContext } from 'react-router-dom'

function ExerciseContainer() {
    const { exercises } = useOutletContext
    return(
        <div>
            <h2>CoreFlow</h2>
            <CardContanier>
                {exercises && exercises.map(exercise => <ExerciseCard key={exercise.id} exercise={exercise}/>)}
            </CardContanier>
        </div>
    )
}

export default ExerciseContainer