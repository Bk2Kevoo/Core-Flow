// import styled from 'styled-components'
import ExerciseCard from './ExerciseCard'
import { useOutletContext } from 'react-router-dom'

function ExerciseContainer() {
    const { exercises } = useOutletContext
    return(
        <div>
            <h2>CoreFlow</h2>
            <CardContaier>
                {exercises && exercises.map(exercise => <ExerciseCard key={exercise.id} exercise={exercise}/>)}
            </CardContaier>
        </div>
    )
}

export default ExerciseContainer