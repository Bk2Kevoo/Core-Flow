import { Outlet, useNavigate } from 'react-router-dom'
import { createGlobalStyle } from 'styled-components'
import { useEffect, useState } from 'react'
import Header from './components/navigation/Header'
import toast, { Toaster } from "react-hot-toast"

function App() {
    const [currentUser, setCurrentUser] = useState(null)
    const [workouts, setWorkOuts] = useState([])
    const [editUser, setEditUser] = useState(false)
    const navigate = useNavigate()
}

export default App;