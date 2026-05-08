from django.shortcuts import render

# Tu clase y lista (lo ideal es que la clase esté en models.py, pero para este ejemplo:)
class Post:
    def __init__(self, titulo, contenido, autor="Usuario"):
        self.titulo = titulo
        self.contenido = contenido
        self.autor = autor
        self.likes = 0

def feed_view(request):
    # Simulando la base de datos
    feed_gastronomico = [
        Post("Ñoquis del Domingo", "Receta de la abuela con mucha salsa roja."),
        Post("Mi Fideo con Huevo", "Rápido, fácil y con mucho queso rallado."),
        Post("Pizza Casera", "Masa de 24hs de leudado.")
    ]
    
    # El diccionario 'context' envía los datos al HTML
    return render(request, 'uno.html', {'posts': feed_gastronomico})