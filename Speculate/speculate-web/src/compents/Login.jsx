import React from 'react'
import { GoogleLogin } from '@react-oauth/google';


function Login() {
  return (
    <div>
        <GoogleLogin
            onSuccess={credentialResponse => {
                console.log(credentialResponse);
            }}
            onError={() => {
                console.log('Login Failed');
            }}
            useOneTap
            />      
    </div>
  )
}

export default Login




