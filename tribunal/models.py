from django.db import models


class Tribunal (models.Model):

    ESTADO_CHOICES = (
        ("", ""),
        ("aguascalientes", "Aguascalientes"),
        ("baja_california", "Baja California"),
        ("baja_california_sur", "Baja California Sur"),
        ("campeche", "Campeche"),
        ("chiapas", "Chiapas"),
        ("chihuahua", "Chihuahua"),
        ("coahuila", "Coahuila"),
        ("colima", "Colima"),
        ("cdmx", "Ciudad de México / CDMX"),
        ("durango", "Durango"),
        ("estado_de_mexico", "Estado de México"),
        ("guanajuato", "Guanajuato"),
        ("guerrero", "Guerrero"),
        ("hidalgo", "Hidalgo"),
        ("jalisco", "Jalisco"),
        ("michoacan", "Michoacán"),
        ("morelos", "Morelos"),
        ("nayarit", "Nayarit"),
        ("nuevo_leon", "Nuevo León"),
        ("oaxaca", "Oaxaca"),
        ("puebla", "Puebla"),
        ("querétaro", "Querétaro"),
        ("quintana_roo", "Quintana Roo"),
        ("san_luis_potosi", "San Luis Potosí"),
        ("sinaloa", "Sinaloa"),
        ("sonora", "Sonora"),
        ("tabasco", "Tabasco"),
        ("tamaulipas", "Tamaulipas"),
        ("tlaxcala", "Tlaxcala"),
        ("veracruz", "Veracruz"),
        ("yucatan", "Yucatán"),
        ("zacatecas", "Zacatecas"),
    )

    nombre = models.CharField(max_length=200)
    ubicacion = models.CharField(max_length=200)
    estado = models.CharField(max_length=50, choices=ESTADO_CHOICES)
