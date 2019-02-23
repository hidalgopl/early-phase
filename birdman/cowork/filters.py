from django.contrib.gis.db.models.functions import Distance


def apply_ordering(qs, pnt):
    if pnt:
        qs = qs.annotate(distance=Distance('point', pnt))
        return qs.order_by('distance')
    else:
        return qs.order_by('-rating')
