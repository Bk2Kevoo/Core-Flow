import { createBrowserRouter } from 'react-router-dom'
import App from '../App'
import Home from "../homepage/Home"
import Error from '../errors/ErrorPage'
import ExerciseDetail from "../exercise/ExerciseDetail"
import Registration from '../auth/Register'
import CategoryDetails from "../category/CategoryDetails"
import CategoriesList from '../category/CategoriesList'
import Profile from '../users/profile'



export const router = createBrowserRouter([
    {
        path: "/",
        element: <App />,
        errorElement: <Error />,
        children: [
            {
                path: "/",
                element: <Home />
            },
            {
                path: "/exercises/:exerciseId",
                element: <ExerciseDetail />
            },
            {
                path: "/categories",
                element: <CategoriesList />
            },
            {
                path: "/categories/:categoryId",
                element: <CategoryDetails />
            },
            {
                path: "/register",
                element: <Registration />
            },
            {
                path: "/profile",
                element: <Profile />
            },
        ]
    }
])