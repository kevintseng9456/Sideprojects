import React, {useState} from "react";

import {MenuIcon, XIcon, QuestionMarkCircleIcon, CogIcon} from '@heroicons/react/outline'
import sidebarTitleImg from '../assets/greg-rakozy-oMpAz-DN-9I-unsplash.jpg'
import Login from './Login'

function Navbar() {
    const [nav, setNav] = useState(false)
    const handleClick = () => setNav(!nav)

    // const handleClose = () => setNav(!nav)


  return (
    <div className="w-screen h-[8vh] bg-primary fixed shadow-md shadow-secondary px-5 flex justify-between items-center ">
        <div onClick={handleClick}>
            {!nav ? <MenuIcon className="cursor-pointer w-8 text-text_m"/> : <XIcon className="cursor-pointer w-8 text-text_m" />}        
        </div>
        
        <div className={`top-[9vh] left-0 flex w-[40vh] h-[88vh] bg-primary text-text_m fixed ease-in-out duration-300 flex-col
            ${!nav ? "-translate-x-full " : "translate-x-0 shadow-lg shadow-secondary"}`}>

            <div className="divide-y-4 divide-secondary w-[36vh] h-[80vh] m-2 ">   
                <h3 className="text-clip overflow-hidden flex w-full text-3xl text-text_m justify-left text-left px-2 py-2 gap-2 items-end">
                    <img className='rounded-lg brightness-75 w-[80px] h-[80px] ' src={sidebarTitleImg} alt="/" />
                    Dope project
                </h3>
                <ul className="flex w-full text-3xl text-text_m text-left px-10 py-4 list-disc">
                    <li >Daily</li> 
                </ul>

            </div>
            <div className="w-[38vh] h-[-2vh] m-2 flex justify-center">
                <Login/>
            </div>            
            


            
        </div>

        <div>
            <p className="text-text_m text-3xl">Speculate 思辨</p>
        </div>
        <div className="flex space-x-2">
            <QuestionMarkCircleIcon className="cursor-pointer w-8 text-text_m"/>
            <CogIcon className="cursor-pointer w-8 text-text_m"/>

        </div>
    </div>
  )
}

export default Navbar
