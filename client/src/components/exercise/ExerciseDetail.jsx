import { useParams } from 'react-router-dom';
import { useEffect, useState } from 'react';
import styled from 'styled-components';
import toast from 'react-hot-toast';

function ExerciseDetail() {
  const [exercise, setExercise] = useState({ work_exercise: [] });

  const { exerciseId } = useParams();

  useEffect(() => {
    (async () => {
      const resp = await fetch(`/api/v1/exercises/${exerciseId}`);
      const data = await resp.json();

      if (resp.ok) {
        setExercise(data);
      } else {
        toast.error(data.error);
      }
    })();
  }, [exerciseId]);

  const { id, name, body_part, work_exercise = [] } = exercise;

  return (
    <CardDetail id={id}>
      <h1>{name}</h1>
      <div className="wrapper">
        <div>
          <h3>Body Part:</h3>
          <p>{body_part}</p>
          <h2>Associated Workouts</h2>
          {work_exercise.map(work => (
            <li key={work.id}>
              {work.name} - {work.sets} sets of {work.reps} reps
            </li>
          ))
        }
        </div>
      </div>
    </CardDetail>
  );
}

export default ExerciseDetail;

const CardDetail = styled.div`
  display: flex;
  flex-direction: column;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  max-width: 600px;
  margin: 0 auto;

  h1 {
    font-size: 24px;
    color: #333;
  }

  .wrapper {
    display: flex;
    flex-direction: column;
  }

  h3 {
    margin: 10px 0 5px;
  }

  p {
    margin: 5px 0;
  }

  ul {
    list-style-type: none;
    padding-left: 0;
  }

  li {
    margin: 5px 0;
    font-size: 16px;
  }
`;
