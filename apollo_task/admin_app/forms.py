from django import forms

from .models import EmployeeModel,TaskAssigning


class Taskform(forms.ModelForm):
    class Meta:
        model=TaskAssigning
        fields= ['taskname','empID']

    def __int__(self,empID):
        self.empID= empID
        return empID
