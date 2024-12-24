module.exports = {
  content: [
    './myApp/templates/**/*.html',
  ],
  darkMode: 'class',
  plugins: [
    require('daisyui'),
  ],
  theme: {
    container: {
      center: true,
      padding: {
        DEFAULT: '1rem',
        sm: '2rem',
        lg: '4rem',
        xl: '5rem',
        '2xl': '6rem',
      },
    },
    extend: {
      screens: {
        '2xl': '1320px',
      },
      colors: {
        'dark': '#0f172a',
      },
    },
  },
}
