import styled from "styled-components"
// import {Link} from "react-router-dom"4

function WorkExercise({ workExercise }) {
    const {sets, reps, weight, id} = workExercise
    
    return (
        <>
        <Card id={id}>
                <div>
                    <h4>Sets: {sets}</h4>
                    <h4>Reps: {reps}</h4>
                    <h4>Weight: {weight} lbs</h4>
                </div>
        </Card>
                    <hr/>
                    </>
    )
}

export default WorkExercise

const Card = styled.li `
    display:flex;

`