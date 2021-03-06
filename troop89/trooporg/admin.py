#  Copyright (c) 2018 Brian Schubert
#
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at http://mozilla.org/MPL/2.0/.

from django.contrib import admin

from .models import Member, Patrol, PositionInstance, PositionType, Term


class PositionInstanceInline(admin.TabularInline):
    model = PositionInstance
    extra = 0


class PatrolMembershipInline(admin.TabularInline):
    model = Patrol.members.through
    extra = 0


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    # Note: if editing user fields from the member admin is desired, simply
    # swap out the base class with the standard UserAdmin or derivative and
    # add the relevant fields/fieldsets.
    inlines = (PositionInstanceInline, PatrolMembershipInline)

    fields = ('first_name', 'last_name')

    list_display = ('first_name', 'last_name', 'is_adult_view', 'is_active_member_view')

    list_display_links = ('first_name', 'last_name')

    def is_adult_view(self, obj: Member) -> bool:
        return obj.is_adult

    is_adult_view.boolean = True

    is_adult_view.short_description = 'Adult'

    def is_active_member_view(self, obj: Member) -> bool:
        return obj.is_active_member

    is_active_member_view.boolean = True

    is_active_member_view.short_description = 'Active Member'


@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    inlines = (PositionInstanceInline, PatrolMembershipInline)

    list_display = ('nickname', 'start', 'end')

    date_hierarchy = 'start'

    empty_value_display = '(none)'


@admin.register(PositionType)
class PositionTypeAdmin(admin.ModelAdmin):
    inlines = (PositionInstanceInline,)

    list_display = ('title', 'is_adult', 'is_leader', 'precedence')

    ordering = ('is_adult', '-is_leader', '-precedence')


@admin.register(Patrol)
class PatrolAdmin(admin.ModelAdmin):
    inlines = (PatrolMembershipInline,)

    list_display = ('name', 'date_created', 'is_active')

    prepopulated_fields = {'slug': ('name',)}

    fieldsets = (
        (None, {
            'fields': ('name', 'date_created')
        }),
        ('Advanced', {
            'classes': ('collapse',),
            'fields': ('slug',)
        })
    )
