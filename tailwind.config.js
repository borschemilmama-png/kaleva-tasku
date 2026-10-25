/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        klv: {
          bg: '#f0ece4',           // Exact kaleva.fi signature warm newsprint background
          card: '#ffffff',         // Crisp clean white card
          fg: '#000000',           // Pure black text
          heading: '#111827',      // Deep charcoal
          subtle: '#5c5852',       // Editorial gray
          border: '#dedad2',       // Clean newsprint divider border
          borderLight: '#ebe7df',
          red: '#cf2e2e',          // Kaleva breaking red
          orange: '#c25700',       // Kaleva signature accent ochre
          blue: '#002855',         // Historic Kaleva navy
          green: '#1a7a40',        // Solution green
          greenLight: '#edf7ed',
          redLight: '#fdf2f2',
          yellowLight: '#fef9e7'
        }
      },
      fontFamily: {
        serif: ['"Instrument Serif"', 'Georgia', 'serif'],
        sans: ['"Plus Jakarta Sans"', '"Archivo"', '-apple-system', 'sans-serif'],
        mono: ['"JetBrains Mono"', 'monospace'],
      },
    },
  },
  plugins: [],
}
