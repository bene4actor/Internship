import os
from io import BytesIO
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.utils.text import slugify
from keydev_reports.views import ReplacerView

from internship_project import settings
from keydev_reports.report_tools import WordEditor
from .forms import InternshipForm
from .models import Intern

def date_to_russian_text(date):
    # Пример преобразования даты в русский текст
    return date.strftime('%d %B %Y')

class TitleMixin:
    def set_report_title(self):
        """
        Переопределяем название отчета в зависимости от формы
        :return: Новое название отчета
        """
        form_fields = self.form_fields
        title = self.title
        form_instance = self.form_instance
        if 'date' in form_fields:
            date = form_instance.cleaned_data['date'].strftime('%d.%m.%Y')
            return f'{title} {date}'
        elif 'date_min' in form_fields and 'date_max' in form_fields:
            date_min = form_instance.cleaned_data['date_min'].strftime('%d.%m.%Y')
            date_max = form_instance.cleaned_data['date_max'].strftime('%d.%m.%Y')
            return f'{title}  {date_min} - {date_max}'
        return title

class InternshipStatement(TitleMixin, ReplacerView):
    """
    Представление отчета 'Заявление на стажировку'
    """
    title = 'Заявление на стажировку'
    report_template = 'Intern'  # Ваш шаблон
    model = Intern  # Модель для стажеров
    obj_pk = 'intern'  # Ключ для стажера
    form_class = InternshipForm  # Форма для подачи заявления
    form_fields = ('start_date', 'end_date', 'full_name', 'contact_info', 'email')  # Поля формы
    url_name = 'internship_statement'

    def update_data(self, data: dict):
        """
        Обновляет данные для отчета перед их отправкой на замену в шаблон.
        :param data: Словарь данных отчета.
        :return: Обновленные данные.
        """
        # Получаем данные из формы
        intern = get_object_or_404(Intern, pk=self.kwargs['intern_id'])
        formatted_start_date = date_to_russian_text(intern.start_date)
        formatted_end_date = date_to_russian_text(intern.end_date)

        # Заменяем данные в словаре
        data['replace_data']['full_name'] = intern.full_name
        data['replace_data']['contact_info'] = intern.contact_info
        data['replace_data']['email'] = intern.email
        data['replace_data']['start_date'] = formatted_start_date
        data['replace_data']['end_date'] = formatted_end_date
        return data


