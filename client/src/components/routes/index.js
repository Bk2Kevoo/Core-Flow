import { createBrowserRouter } from 'react-router-dom'
import App from '../App'
// import Home from '../components/pages/Home'
import Error from '../errors/ErrorPage'
import ExerciseDetail from "../exercise/ExerciseDetail"
// import Register from '../components/auth/Register'


export const router = createBrowserRouter([
    {
        path: "/",
        element: <App />,
        errorElement: <Error />,
        children: [
            // {
            //     path: "/exercises",
            //     index: true,
            //     element: <ExerciseDetail />
            // },
            {
                path: "/exercises/:exerciseId",
                index: true,
                element: <ExerciseDetail />
            },
        ]
    }
])