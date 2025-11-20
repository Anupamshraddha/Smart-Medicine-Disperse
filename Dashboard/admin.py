from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Medicine, AccessLog, Notification, MedicineUsage, UserProfile, SystemStatus

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "vpin", "quantity", "expiry_date", "category")
    search_fields = ("name", "barcode")
    list_filter = ("category", "expiry_date")

@admin.register(AccessLog)
class AccessLogAdmin(admin.ModelAdmin):
    list_display = ("user", "medicine", "action", "timestamp", "success")
    list_filter = ("action", "success")

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ("title", "type", "user", "is_read", "created_at")
    list_filter = ("type", "is_read")

@admin.register(MedicineUsage)
class MedicineUsageAdmin(admin.ModelAdmin):
    list_display = ("medicine", "user", "quantity_used", "usage_date")

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "roll_no", "phone_number", "is_admin", "interaction_status")

@admin.register(SystemStatus)
class SystemStatusAdmin(admin.ModelAdmin):
    list_display = ("is_locked", "esp32_connected", "last_esp32_ping", "current_user", "last_activity", "camera_on")

