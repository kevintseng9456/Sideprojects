/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}",],
  theme: {
    screens:{
      sm: "640px",
      md: "768px",
      lg: "1024px",
      xl: "1280px",
      "2xl": "1536px",
    },
    extend:{
      colors:{
        primary: '#263238',
        p_light: '#4f5b62',
        p_dark: '#000a12',

        secondary: '#718792',
        s_light: '#a0b7c2',
        s_dark: '#455a64',        

        text_m: '#FFFFFF',
      },

    }
  },
  plugins: [
    require('tailwindcss'),
    require('autoprefixer'),    
  ],
}
