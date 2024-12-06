import { useOutletContext, useParams } from 'react-router-dom';
import { useEffect, useState } from 'react';
import styled from 'styled-components';
import toast from 'react-hot-toast';
import WorkExercise from '../workexercise/WorkExercise';

function ExerciseDetail() {
  const [exercise, setExercise] = useState({ work_exercises: [] });
  const { currentUser } = useOutletContext();
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

  const { id, name, body_part, work_exercises } = exercise;

  const uniqueWorkExercises = work_exercises.filter((value, index, self) => {
    return index === self.findIndex((e) => (
      e.sets === value.sets && e.reps === value.reps && e.weight === value.weight
    ));
  });

  console.log("Unique Work Exercises: ", uniqueWorkExercises);

  return (
    <CardDetail id={id}>
      <h1>{name}</h1>
      <div className="wrapper">
        <div>
          <h3>Body Part:</h3>
          <p>{body_part}</p>
          <h2>Should Do:</h2>
          <hr />
          {currentUser && uniqueWorkExercises.map(we => (
            <WorkExercise key={we.id} workExercise={we} />
          ))}
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
`;
