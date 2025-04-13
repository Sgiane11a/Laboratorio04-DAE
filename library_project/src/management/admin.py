from django.contrib import admin
from .models import LibraryBranch, BookCopy, BookLoan, Reservation

@admin.register(LibraryBranch)
class LibraryBranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'email')

@admin.register(BookCopy)
class BookCopyAdmin(admin.ModelAdmin):
    list_display = ('book', 'branch', 'condition', 'is_available', 'inventory_number')

@admin.register(BookLoan)
class BookLoanAdmin(admin.ModelAdmin):
    list_display = ('copy', 'borrower', 'checkout_date', 'due_date', 'status')

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'branch', 'request_date', 'status')