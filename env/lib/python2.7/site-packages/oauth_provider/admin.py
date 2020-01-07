from django.contrib import admin

from models import Consumer, Token
    
class ConsumerAdmin(admin.ModelAdmin):
    pass

class TokenAdmin(admin.ModelAdmin):
    pass
    

admin.site.register(Consumer, ConsumerAdmin)
admin.site.register(Token, TokenAdmin)
