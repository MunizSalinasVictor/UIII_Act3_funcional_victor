from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# ==========================================
# MODELO: SUSCRIPCIÓN
# ==========================================
class Suscripcion(models.Model):
    nombre_plan = models.CharField(max_length=50, unique=True)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    calidad_video = models.CharField(max_length=20)
    num_dispositivos = models.IntegerField()
    beneficio_extra = models.TextField()
    descarga_offline = models.BooleanField(default=False)
    
    # Relación muchos a muchos
    contenidos_exclusivos = models.ManyToManyField(
        'Contenido', 
        related_name='suscripciones_exclusivas',
        blank=True
    )
    usuarios_premium = models.ManyToManyField(
        'Usuario', 
        related_name='suscripciones_adicionales',
        blank=True
    )

    class Meta:
        db_table = 'suscripcion'
    
    def __str__(self):
        return f"{self.nombre_plan} - ${self.precio}"

# ==========================================
# MODELO: CONTENIDO
# ==========================================
class Contenido(models.Model):
    TIPO_CHOICES = [
        ('pelicula', 'Película'),
        ('serie', 'Serie'),
        ('documental', 'Documental'),
    ]
    
    titulo = models.CharField(max_length=100, unique=True)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    fecha_lanzamiento = models.DateField()
    categoria = models.IntegerField()
    capitulos = models.CharField(max_length=5)
    
    suscripcion = models.ForeignKey(
        Suscripcion, 
        on_delete=models.CASCADE,
        related_name='contenidos_principales'
    )

    class Meta:
        db_table = 'contenido'
    
    def __str__(self):
        return self.titulo

# ==========================================
# MODELO: USUARIO
# ==========================================
class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=128)
    fecha_registro = models.DateField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    
    suscripcion = models.ForeignKey(
        Suscripcion, 
        on_delete=models.CASCADE,
        related_name='usuarios_principales'
    )

    class Meta:
        db_table = 'usuario'
    
    def __str__(self):
        return self.nombre_usuario