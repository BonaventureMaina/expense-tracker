from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Expense
from .forms import ExpenseForm


@login_required
def expense_list(request):
    expenses = Expense.objects.filter(user=request.user)

    # Get filter values from GET parameters
    selected_category = request.GET.get('category', '')
    selected_month = request.GET.get('month', '')

    # Apply category filter
    if selected_category:
        expenses = expenses.filter(category=selected_category)

    # Apply month filter (format: YYYY-MM)
    if selected_month:
        year, month = selected_month.split('-')
        expenses = expenses.filter(date__year=year, date__month=month)

    total = sum(e.amount for e in expenses)

    context = {
        'expenses': expenses,
        'total': total,
        'selected_category': selected_category,
        'selected_month': selected_month,
        'categories': Expense.CATEGORY_CHOICES,
    }
    return render(request, 'expenses/expense_list.html', context)


@login_required
def expense_create(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            messages.success(request, 'Expense added successfully.')
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/expense_form.html', {'form': form, 'title': 'Add Expense'})


class ExpenseUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'expenses/expense_form.html'
    success_url = reverse_lazy('expense_list')

    def test_func(self):
        expense = self.get_object()
        return self.request.user == expense.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Expense'
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Expense updated successfully.')
        return super().form_valid(form)


class ExpenseDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Expense
    template_name = 'expenses/expense_confirm_delete.html'
    success_url = reverse_lazy('expense_list')

    def test_func(self):
        expense = self.get_object()
        return self.request.user == expense.user

    def form_valid(self, form):
        messages.success(self.request, 'Expense deleted.')
        return super().form_valid(form)