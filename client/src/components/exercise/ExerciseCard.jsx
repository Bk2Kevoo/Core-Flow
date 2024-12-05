import React from 'react';
import { Link } from 'react-router-dom';
import styled from 'styled-components';


function ExerciseCard({ exercise }) {
    const { name, body_part, id,} = exercise;
    
    return (
        <Card>
            <Link to={`/exercises/${id}`}>
                <div>
                    <Title>{name}</Title>
                    <BodyPart>{body_part}</BodyPart>
                </div>
            </Link>
        </Card>
    );
}

export default ExerciseCard;

// Styled-components for Card and other elements
const Card = styled.div`
    background-color: #fff;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    padding: 16px;
    width: 250px;
    margin: 16px;
    text-align: center;
    transition: transform 0.2s ease-in-out;
    
    &:hover {
        transform: translateY(-5px);
    }
`;


const Title = styled.h2`
    font-size: 1.2rem;
    color: #333;
    margin: 8px 0;
`;

const BodyPart = styled.p`
    font-size: 1rem;
    color: #666;
    margin: 4px 0;
`;
