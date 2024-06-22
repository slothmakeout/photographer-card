module.exports = {
  content: [
    "./templates/**/*.html", // путь к вашим HTML и Jinja2 файлам
    "./static/**/*.js", // путь к вашим JavaScript файлам
  ],
  theme: {
    extend: {
      colors: {
        "glowcoma-green-400": "#27C196",
      },
    },
  },
  plugins: [],
};
