# File: F1-main/library/models.py
from django.db import models


class Driver(models.Model):
    name = models.CharField(
        max_length=45,
        verbose_name='Name',
        help_text='Enter the full name of the driver',
        error_messages={'blank': 'Driver name must be provided'}
    )
    nationality = models.CharField(
        max_length=45,
        verbose_name='Nationality',
        help_text='Enter the driver’s nationality'
    )
    number_of_wins = models.PositiveIntegerField(
        default=0,
        verbose_name='Number of Wins'
    )
    photo = models.ImageField(
        upload_to='media/drivers/',
        null=True,
        blank=True,
        verbose_name='Driver Photo'
    )

    class Meta:
        ordering = ['-number_of_wins', 'name']
        verbose_name = 'Driver'
        verbose_name_plural = 'Drivers'

    def __str__(self):
        return f'{self.name} ({self.nationality}) – {self.number_of_wins} wins'


class Team(models.Model):
    ENGINE_SUPPLIER_CHOICES = [
        ('Ferrari', 'Ferrari'),
        ('Mercedes', 'Mercedes'),
        ('Honda', 'Honda'),
        ('Renault', 'Renault'),
    ]

    team_name = models.CharField(
        max_length=45,
        verbose_name='Team Name'
    )
    engine_supplier = models.CharField(
        max_length=20,
        choices=ENGINE_SUPPLIER_CHOICES,
        verbose_name='Engine Supplier'
    )
    country = models.CharField(
        max_length=45,
        verbose_name='Country of Origin'
    )
    driver1 = models.ForeignKey(
        Driver,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='First Driver',
        related_name='primary_teams'
    )
    driver2 = models.ForeignKey(
        Driver,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Second Driver',
        related_name='secondary_teams'
    )
    # New field for team logo
    logo = models.ImageField(
        upload_to='teams/',
        null=True,
        blank=True,
        verbose_name='Team Logo'
    )


    class Meta:
        ordering = ['team_name']
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

    def __str__(self):
        return f'{self.team_name} ({self.country})'


class Car(models.Model):
    model = models.CharField(
        max_length=45,
        verbose_name='Car Model'
    )
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        verbose_name='Owning Team'
    )
    # New field for car photo
    photo = models.ImageField(
        upload_to='cars/',
        null=True,
        blank=True,
        verbose_name='Car Photo'
    )


    class Meta:
        ordering = ['model']
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'

    def __str__(self):
        return f'{self.model} – team: {self.team.team_name}'
