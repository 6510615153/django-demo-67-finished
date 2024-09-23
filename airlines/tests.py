from django.test import TestCase

from django.core.management.color import no_style
from django.db import connection

from myapps.models import MyModel1, MyModel2

sequence_sql = connection.ops.sequence_reset_sql(no_style(), [MyModel1, MyModel2])
with connection.cursor() as cursor:
    for sql in sequence_sql:
        cursor.execute(sql)