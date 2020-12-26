import uuid

from django.db import models


class PositionModel(models.Model):
    class Meta:
        abstract = True

    pos_x = models.IntegerField()
    pos_y = models.IntegerField()

    @property
    def pos(self):
        return [self.pos_x, self.pos_y]

    @pos.setter
    def pos(self, value):
        self.pos_x, self.pos_y = value


class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


def toon_sprite_dir(instance, filename):
    return  f'toon_sprite/{instance.toon_id}/{filename}'


class Toon(models.Model):
    toon_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    toon_name = models.CharField(max_length=144)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    toon_sprite = models.ImageField(upload_to=toon_sprite_dir, height_field=40, width_field=40)


class Campaign(models.Model):
    camp_name = models.CharField(max_length=144)
    dm = models.ForeignKey('User', on_delete=models.CASCADE)
    encounter = models.ForeignKey('Encounter', on_delete=models.CASCADE, null=True, blank=True)


class Grid(models.Model):
    camp = models.ForeignKey('Campaign', on_delete=models.CASCADE)
    name = models.CharField(max_length=144)


class GridObject(PositionModel):
    grid = models.ForeignKey('Grid', on_delete=models.CASCADE)
    typ = models.ForeignKey('NPC', on_delete=models.CASCADE)
    go_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


def npc_sprite_dir(instance, filename):
    return f'npc_sprite/{instance.id}/{filename}'


class NPC(models.Model):
    name = models.CharField(max_length=144)
    npc_sprite = models.ImageField(upload_to=npc_sprite_dir, height_field=40, width_field=40)


class Encounter(models.Model):
    grid = models.ForeignKey('Grid', on_delete=models.CASCADE)


class EncounterEvent(models.Model):
    encounter = models.ForeignKey('Encounter', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    object_uuid = models.UUIDField()
    action = models.JSONField()


class MarchOrder(PositionModel):
    campaign = models.ForeignKey('Campaign', on_delete=models.CASCADE)
    toon = models.ForeignKey('Toon', on_delete=models.CASCADE)
