import { Outlet} from 'react-router-dom'
// import { createGlobalStyle } from 'styled-components'
import { useEffect, useState } from 'react'
import Header from './navigation/Header'
import toast, { Toaster } from "react-hot-toast"

function App() {
    const [workouts, setWorkOuts] = useState([])
    const [currentUser, setCurrentUser] = useState(null)

    // const [user, setUser] = useState(null)
    // const [editUser, setEditUser] = useState(false)

    // const navigate = useNavigate()

 // Getting all the WORKOUTS
    useEffect(() => {
        currentUser && (async () => {
        const resp = await fetch("/api/v1/workouts")
        const data = await resp.json()
        if (resp.ok) {
            setWorkOuts(data)
        } else {
            toast.error(data.error)
        }
        })()
    }, [currentUser])

    useEffect(() => {
        (async () => {
        const resp = await fetch("/api/v1/current-user")
        const data = await resp.json()
        if (resp.ok) {
            setCurrentUser(data)
        } else {
            toast.error(data.error)
        }
        })()
    }, [])

        // Add user, edit user, delete user, update user
        const updateUser = (value) => setCurrentUser(value) 



        return (
            <>
            {/* <GlobalStyle /> */}
            <Header currentUser={currentUser} updateUser={updateUser} />
            <Toaster />
            <Outlet context={{workouts, currentUser, updateUser}} />
            </>
        )
}




export default App;