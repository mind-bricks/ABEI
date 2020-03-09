from rest_framework import (
    serializers,
)

from .models import (
    ProcedureRun,
)


class ProcedureRunSerializer(serializers.ModelSerializer):
    procedure = serializers.SlugRelatedField(
        slug_field='uuid',
        read_only=True,
    )

    class Meta:
        model = ProcedureRun
        fields = [
            'uuid',
            'procedure',
            'created_time',
        ]
        read_only_fields = [
            'uuid',
            'procedure',
            'created_time',
        ]
