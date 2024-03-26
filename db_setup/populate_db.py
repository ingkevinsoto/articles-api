import sqlite3

# Sample articles data
articles_data = [
    ("10 Consejos para mejorar tu productividad", 
     "La productividad es una habilidad clave en el mundo laboral actual. Aquí te ofrecemos 10 consejos prácticos para mejorarla: 1. Organiza tu tiempo...",
     "https://www.shutterstock.com/shutterstock/photos/2054923319/display_1500/stock-photo-vocalist-in-front-of-crowd-on-scene-in-stadium-bright-stage-lighting-crowded-dance-floor-phone-2054923319.jpg",
     "John Doe"),
    
    ("Cómo mantener un estilo de vida saludable", 
     "Mantener un estilo de vida saludable es fundamental para nuestro bienestar general. Descubre algunos hábitos que pueden ayudarte a alcanzar este objetivo:...",
    "https://www.shutterstock.com/shutterstock/photos/2335455709/display_1500/stock-photo-cheering-woman-on-man-shoulders-at-music-festival-2335455709.jpg",
     "Jane Smith"),
    
    ("Los beneficios del ejercicio físico", 
     "El ejercicio físico regular no solo fortalece el cuerpo, sino que también tiene numerosos beneficios para la salud mental. Descubre por qué es importante...",
     "https://www.shutterstock.com/shutterstock/photos/611045375/display_1500/stock-photo-crowd-at-concert-summer-music-festival-611045375.jpg",
     "Michael Johnson")
]

conn = sqlite3.connect('blog.db')
cursor = conn.cursor()

cursor.executemany("INSERT INTO articles (title, content, image_url, autor) VALUES (?, ?, ?, ?)", articles_data)

conn.commit()
conn.close()
