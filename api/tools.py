from asyncio import exceptions
from django import forms

from django.contrib.postgres.fields import ArrayField


class ChoiceArrayField(ArrayField):
    """
    A field that allows us to store an array of choices.
    Uses Django's Postgres ArrayField
    and a MultipleChoiceField for its formfield.
    """

    def formfield(self, **kwargs):
        defaults = {
            "form_class": forms.MultipleChoiceField,
            "choices": self.base_field.choices,
        }
        defaults.update(kwargs)
        # Skip our parent's formfield implementation
        return super(ArrayField, self).formfield(**defaults)

    def to_python(self, value):
        res = super().to_python(value)
        if isinstance(res, list):
            value = [self.base_field.to_python(val) for val in res]
        return value

    def validate(self, value, model_instance):
        if not self.editable:
            # Skip validation for non-editable fields.
            return

        if self.choices is not None and value not in self.empty_values:
            if set(value).issubset({option_key for option_key, _ in self.choices}):
                return
            raise exceptions.ValidationError(
                self.error_messages["invalid_choice"],
                code="invalid_choice",
                params={"value": value},
            )

        if value is None and not self.null:
            raise exceptions.ValidationError(self.error_messages["null"], code="null")

        if not self.blank and value in self.empty_values:
            raise exceptions.ValidationError(self.error_messages["blank"], code="blank")


FUNCTION_CHOICES = (
    ("C#", "C#"),
    ("Django", "Django"),
    ("ExpressJS", "ExpressJS"),
    ("FastAPI", "FastAPI"),
    ("Firebase", "Firebase"),
    ("Javascript", "Javascript"),
    ("PostgreSQL", "PostgreSQL"),
    ("Python", "Python"),
    ("ReactJS", "ReactJS"),
    ("Tensorflow", "Tensorflow"),
    ("Typescript", "Typescript"),
    ("Unity3D", "Unity3D"),
)
