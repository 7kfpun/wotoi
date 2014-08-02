# -*- coding: utf-8 -*-


def get_or_create(model, *args, **kwargs):

    """ fix sqlite that not support well for models get_or_create method."""

    try:
        obj = model.objects.get(**kwargs)
    except model.DoesNotExist:
        obj = model(**kwargs)
        obj.save()
        return obj
