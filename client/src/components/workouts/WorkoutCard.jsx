import { Link } from 'react-router-dom'
import styled from 'styled-components'

function WorkoutCard({ workout }) {
    const { id, name, date } = workout

    return (
        <Card id={id}>
            <Link to={`/workouts/${id}`}>
                <div>
                    <h2>{name}</h2>
                    <p>{date}</p>
                    <img src={image} alt={title} />
                </div>
            </Link>
        </Card>
    )
}

export default WorkoutCard

const Card = styled