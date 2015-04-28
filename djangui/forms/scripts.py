from django import forms


class DjanguiForm(forms.Form):

    def add_djangui_fields(self):
        # This adds fields such as job name, description that we like to validate on but don't want to include in
        # form rendering
        self.fields['job_name'] = forms.CharField()
        self.fields['job_description'] = forms.CharField(required=False)

    def save(self, **kwargs):
        from ..backend import utils
        if 'user' in self.data:
            self.cleaned_data['user'] = self.data['user']
        job, command = utils.create_djangui_job(self.cleaned_data)
        return job, command