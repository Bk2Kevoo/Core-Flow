import { Outlet, useNavigate } from 'react-router-dom'
// import { createGlobalStyle } from 'styled-components'
import { useEffect, useState } from 'react'
// import Header from './components/navigation/Header'
import toast, { Toaster } from "react-hot-toast"

function App() {
    const [workouts, setWorkOuts] = useState([])
    const [categories, setCategories] = useState([])
    const [exercises, setExercises] = useState([])

    const [user, setUser] = useState(null)
    const [editUser, setEditUser] = useState(false)

    const navigate = useNavigate()

 // Getting all the WORKOUTS
    useEffect(() => {
        (async () => {
        const resp = await fetch("/api/v1/workouts")
        const data = await resp.json()
        if (resp.ok) {
            setWorkOuts(data)
        } else {
            toast.error(data.error)
        }
        })()
    }, [])

    // Getting all the CATEGORIES
    useEffect(() => {
        (async () => {
        const resp = await fetch("/api/v1/categories")
        const data = await resp.json()
        if (resp.ok) {
            setCategories(data)
        } else {
            toast.error(data.error)
        }
        })()
    }, [])
    
    // Getting all the EXERCISES
    useEffect(() => {
        (async () => {
        const resp = await fetch("/api/v1/exercises")
        const data = await resp.json()
        if (resp.ok) {
            setExercises(data)
        } else {
            toast.error(data.error)
        }
        })()
    }, [])


        // Add user, edit user, delete user, update user



        return (
            <>
            {/* <GlobalStyle /> */}
            <Toaster />
            <Outlet context={{}} />
            </>
        )
}




export default App;