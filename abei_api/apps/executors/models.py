from uuid import uuid1

from django.db import models


class ProcedureRun(models.Model):
    uuid = models.UUIDField(
        unique=True,
        default=uuid1,
    )
    procedure = models.ForeignKey(
        'editors.Procedure',
        related_name='runs',
        on_delete=models.CASCADE,
    )
    created_time = models.DateTimeField(
        auto_now_add=True,
    )
    finished_time = models.DateTimeField(
        null=True,
        default=None,
    )
