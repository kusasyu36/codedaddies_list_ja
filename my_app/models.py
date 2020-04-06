#from django.db import models
#
#class Search(models.Model):
#    search = models.CharField(max_length=500)
#    created = models.DateTimeField(auto_now=True)
#    
#    class Meta:
#        verbose_name_plural = 'Searches'

#from django.db import models
#
#class Search(models.Model):
#    search = models.CharField(max_length=500)
#    created = models.DateTimeField(auto_now=True)
#    
#    class Meta:
#        verbose_name_plural = '検索'

from django.db import models

class Search(models.Model):
    search = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = '検索'
        
    def __str__(self):
        return '{}'.format(self.search)