import { useEffect, useState } from 'react'
import { Routes, Route, Navigate, useRoutes } from 'react-router-dom'

import { app, auth } from '../firebase.js'

import { useAuthState } from 'react-firebase-hooks/auth'

import Home from '../pages/Home.jsx'
import Login from '../pages/Login.jsx'
import Signup from '../pages/Signup.jsx'
 

function DecideCurrentPage() {
    const [user] = useAuthState(auth)

    if (!user) {
        return <Navigate to="/login" />
    }

    else {
        return <Home />
    }
}

export default function App() {
    let element = useRoutes([
        {
            path: '/',
            children: [
                {
                    index: true,
                    element: <DecideCurrentPage />,
                },
                {
                    path: 'login',
                    element: <Login />,
                }, 
                {
                    path: 'signup',
                    element: <Signup />,
                }
            ]
        }
    ])

    return element
}