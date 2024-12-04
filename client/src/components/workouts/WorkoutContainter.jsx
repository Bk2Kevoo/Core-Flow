import styled from 'styled-components'
import WorkoutCard from './WorkoutCard';
import { useOutletContext } from 'react-router-dom';

function WorkoutContainer() {
    const { workouts } = useOutletContext();

    return (
        <div>
            <h1>
                <span>F</span>CoreFlow<span>C</span>enter
            </h1>
            <ul>
                {workouts && workouts.map(workout => (
                    <WorkoutCard key={workout.id} workout={workout} />
                ))}
            </ul>
        </div>
    );
}

export default WorkoutContainer;

const Container = styled