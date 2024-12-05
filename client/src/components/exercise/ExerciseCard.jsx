import React from 'react';
import { Link } from 'react-router-dom';
import styled from 'styled-components';

function ExerciseCard({ exercise }) {
    const { name, body_part, id } = exercise;

    return (
        <Card>
            <Link to={`/exercises/${id}`}>
                <CardContent>
                    <Title>{name}</Title>
                    <BodyPart>{body_part}</BodyPart>
                </CardContent>
            </Link>
        </Card>
    );
}

export default ExerciseCard;

const Card = styled.div`
    background-color: #fff;
    border-radius: 12px; /* Slightly more rounded corners */
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    padding: 20px;
    width: 260px;
    margin: 16px;
    text-align: center;
    transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
    
    &:hover {
        transform: translateY(-8px); /* Slightly more noticeable hover effect */
        box-shadow: 0 6px 18px rgba(0, 0, 0, 0.15); /* Enhanced shadow on hover */
    }
`;

const CardContent = styled.div`
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
`;

const Title = styled.h2`
    font-size: 1.25rem;
    color: #333;
    margin: 8px 0;
    font-weight: 600; /* Bold font for the exercise name */
`;

const BodyPart = styled.p`
    font-size: 1rem;
    color: #777;
    margin: 4px 0;
    font-weight: 500; /* Slightly bold to emphasize the body part */
`;