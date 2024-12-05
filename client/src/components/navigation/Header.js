import { useState } from 'react'
import {Link} from 'react-router-dom'
import styled from 'styled-components'
import { GiHamburgerMenu } from 'react-icons/gi'
import toast from 'react-hot-toast'


function Header({currentUser, updateUser}) {
    const [menu, setMenu] = useState(false)
   
     const handleLogout = async () => {
       const resp = await fetch("/api/v1/logout", {method: "DELETE"})
       if (resp.ok) {
         updateUser(null)
       } else {
         const data = await resp.json()
         toast.error(data.error)
       }
     }
     
       return (
           <Nav> 
            <NavH1>CoreFlow</NavH1>
            <Menu>
              {!menu?
              <div onClick={() => setMenu(!menu)}>
                <GiHamburgerMenu size={30}/> 
              </div>:
              <ul>
                 <li onClick={() => setMenu(!menu)}>x</li>
                 <li><Link to='/home'> Home</Link></li>
                 <li ><Link to='/categories'>Categories</Link></li>
                 { currentUser ? (
                   <>
                     <li ><button onClick={handleLogout}>Logout</button></li>
                   </>
                 ) : (
                   <li><Link to='/register'>Register Now!</Link></li>
                 )}
              </ul>
              }
            </Menu>
           </Nav>
       )
   }
   
   export default Header

   // This is For the Styling of our Header

   const NavH1 = styled.h1`
   font-family: 'Splash', cursive;
   `
   const Nav = styled.div`
     display: flex;
     justify-content:space-between;
     
   `;
   
   const Menu = styled.div`
     display: flex;
     align-items: center;
     a{
       text-decoration: none;
       color:black;
       font-family:Arial;
     }
     a:hover{
       color:pink
     }
     ul{
       list-style:none;
     }
     
   `;