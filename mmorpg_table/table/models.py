from django.db import models


class Users(models.Model):
    """Класс Users для создания экземпляров пользователей портала"""
    pass


class Ads(models.Model):
    """Класс Ads для создания экземпляров объявлений"""
    pass


class Reviews(models.Model):
    """Класс Reviews для создания откликов пользователей на объявления"""
    pass


class Categories(models.Model):
    """Класс Categories для создания категорий, к которым относятся объявления"""
    pass
