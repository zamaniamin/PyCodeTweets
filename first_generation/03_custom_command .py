"""
You can create a custom management command in Django to automate the data filling process.
A management command is a Python script that can be executed using the `manage.py`
command-line utility. 
You can define your data creation logic in the custom command's handle method.

Here's an example:
Create a new file `<myapp>/management/commands/<fill_data>.py` with the following content:
"""


from django.core.management.base import BaseCommand
from myapp.models import MyModel


class Command(BaseCommand):
    help = 'Fill data in the database'

    def handle(self, *args, **options):
        # Your data creation logic
        instance = MyModel(field1=value1, field2=value2)
        instance.save()
        
        
"""
Run the custom command using the following command:
$ python manage.py <fill_data>
"""


# Series: PyCodeTweets 03
# Issue: custom management command in Django to automate the data filling process.
# GitHub: https://github.com/zamaniamin
# Twitter: https://twitter.com/zamaniamiin
