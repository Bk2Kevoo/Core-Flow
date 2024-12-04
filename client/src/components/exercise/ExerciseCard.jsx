import styled from "styled-components"
// import {Link} from "react-router-dom"4

function ExerciseCard() {
    const {name, body_part, id} = exercise
    
    return (
        <Card id={id}>
            <Link to={`/exercises/${id}`}>
                <div>
                    <h2>{name}</h2>
                    <p>{body_part}</p>
                </div>
            </Link>
        </Card>
    )
}

export default ExerciseCard

const Card = styled.li `
    display:flex;

`