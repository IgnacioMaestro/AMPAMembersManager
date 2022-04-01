from django.contrib import admin

from ampa_members_manager.academic_course.models.academic_course import AcademicCourse
from ampa_members_manager.academic_course.models.established_course import EstablishedCourse
from ampa_members_manager.activity.models.repetitive_activity import RepetitiveActivity
from ampa_members_manager.activity.models.single_activity import SingleActivity
from ampa_members_manager.activity.models.unique_activity import UniqueActivity
from ampa_members_manager.family.models.authorization import Authorization
from ampa_members_manager.family.models.bank_account import BankAccount
from ampa_members_manager.family.models.child import Child
from ampa_members_manager.family.models.family import Family
from ampa_members_manager.family.models.membership import Membership
from ampa_members_manager.family.models.parent import Parent


class RepetitiveActivityAdmin(admin.ModelAdmin):
    fields = ['name', 'academic_course', 'assignment', 'funding', 'single_activities']


class UniqueActivityAdmin(admin.ModelAdmin):
    fields = ['name', 'academic_course', 'assignment', 'funding', 'single_activity']


admin.site.register(AcademicCourse)
admin.site.register(EstablishedCourse)
admin.site.register(Family)
admin.site.register(Child)
admin.site.register(Parent)
admin.site.register(BankAccount)
admin.site.register(Authorization)
admin.site.register(Membership)
admin.site.register(RepetitiveActivity, RepetitiveActivityAdmin)
admin.site.register(UniqueActivity, UniqueActivityAdmin)
admin.site.register(SingleActivity)
