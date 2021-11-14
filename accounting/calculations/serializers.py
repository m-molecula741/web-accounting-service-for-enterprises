from rest_framework import serializers

from .models import AccInfo, Income, Expenses


class IncomeSerializer(serializers.ModelSerializer):
    """сериализатор продажи товара"""

    class Meta:
        model = Income
        fields = ("product_name", "article", "date_sales", "product_price", "product_count")


class ExpensesSerializer(serializers.ModelSerializer):
    """сериализатор купли товара"""

    class Meta:
        model = Expenses
        fields = '__all__'


class AccInfoSerializer(serializers.ModelSerializer):
    """сериализатор для отчетности"""

    class Meta:
        model = AccInfo
        fields = '__all__'
