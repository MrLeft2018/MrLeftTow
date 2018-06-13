from django.contrib import admin
from sign.models import Event,GameBoy

# Register your models here.
# 下面两行是初始admin页面可以显示出Event以及GameBoy
#admin.site.register(Event)
#admin.site.register(GameBoy)

# 界面字段返回多参数设置如下
class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'limit', 'status', 'address', 'start_time']
    search_fields = ['name'] #搜索栏
    list_filter = ['status'] #过滤器

class GameBoyAdmin(admin.ModelAdmin):
    list_display = ['realname', 'phone', 'email', 'sign', 'create_time', 'event']
    search_fields = ['realname','phone']  # 搜索栏
    list_filter = ['sign']  # 过滤器

admin.site.register(Event,EventAdmin)
admin.site.register(GameBoy,GameBoyAdmin)