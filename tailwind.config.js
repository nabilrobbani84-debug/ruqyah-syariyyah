/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
  ],
  theme: {
    extend: {
      colors: {
        'sage-green': '#8FA290',
        'forest-green': '#1A4D2E',
        'deep-green': '#0F2F1C',
        'cream': '#F9F9F7',
        'gold-accent': '#C5A059',
        'gold-light': '#E5C985',
      },
      fontFamily: {
        sans: ['"Plus Jakarta Sans"', 'sans-serif'],
        serif: ['"Playfair Display"', 'serif'],
        arabic: ['"Amiri"', 'serif'],
      },
      animation: {
        'bounce-slow': 'bounce 3s infinite',
      }
    },
  },
  plugins: [],
}
