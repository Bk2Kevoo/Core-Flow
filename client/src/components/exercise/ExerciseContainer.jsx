import styled from 'styled-components'
import ExerciseCard from './ExerciseCard'
import { useOutletContext } from 'react-router-dom'

function ExerciseContainer() {
    const { exercises } = useOutletContext()
    return(
        <Container>
            <Title>CoreFlow</Title>
            <CardContainer>
                {exercises && exercises.map(exercise => (
                    <ExerciseCard key={exercise.id} exercise={exercise} />
                ))}
            </CardContainer>
        </Container>
    )
}

export default ExerciseContainer

// Styled-components for improved layout and styling

const Container = styled.div`
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
    background-color: #f8f9fa; /* Light background for contrast */
`;

const Title = styled.h2`
    font-size: 2rem;
    color: #2c3e50;
    text-align: center;
    font-weight: 600;
    margin-bottom: 20px; /* Add spacing between the title and the cards */
`;

const CardContainer = styled.div`
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); /* Responsive grid */
    gap: 20px; /* Space between the cards */
    padding: 20px;
`;
