import { createBrowserRouter } from 'react-router-dom'
import App from '../App'
import Home from '../components/pages/Home'
import Error from '../components/errors/Error'
import Register from '../components/auth/Register'


export const router = createBrowserRouter([
    {
        path: "/",
        element: <App />,
        errorElement: <Error />,
        children: [
            {
                path: "/",
                index: true,
                element: <Home />
            },
            {
                path: "users/new",
                element: <ProductionForm />
            },
            {
                path: "productions/:productionId/edit",
                element: <ProductionEdit />
            },
            {
                path: "/productions/:productionId",
                element: <ProductionDetail />
            },
            {
                path: "/register",
                element: <Register />
            }
        ]
    }
])