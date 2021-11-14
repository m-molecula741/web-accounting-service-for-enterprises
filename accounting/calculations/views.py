from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
from json import *
import json
from django.http import HttpResponse, JsonResponse

from django.db import connection
from .models import *
from .serializers import IncomeSerializer, ExpensesSerializer, AccInfoSerializer


class AddIncome(APIView):
    """продажа товара"""
    def post(self, request):
        print("da")
        income = IncomeSerializer(data=request.data)
        if income.is_valid():
            print(income)
            income.save()
            return Response(status=201)
        else:
            print(income)
            return Response(status=507)


class AddExpenses(APIView):
    """покупка товара"""
    def post(self, request):
        expense = ExpensesSerializer(data=request.data)
        if expense.is_valid():
            expense.save()
            print(type(expense))
            return Response(status=201)
        else:
            return Response(status=507)


class Info(APIView):
    """отчетность"""
    def post(self, request):
        info = dict(
            bis_reg_form=request.data["bis_reg_form"],
            taxation_system=request.data["taxation_system"],
            article=request.data["article"],
            date_start=request.data["date_start"],
            date_end=request.data["date_end"],
            base_rate=request.data["base_rate"]
        )
        print(info)

        tax = ['income usn6', 'income-expenses usn15', 'ENVD', 'PSN']

        if info['taxation_system'] in tax:
            sum_income = 0
            if info["article"] == None:
                incms = Income.objects.filter(date_sales__range=[info["date_start"], info["date_end"]])
            else:
                incms = Income.objects.filter(date_sales__range=[info["date_start"], info["date_end"]], article=info["article"])
            for inc in incms:
                sum_income += inc.product_price * inc.product_count
            print(sum_income)

            sum_expenses = 0
            if info["article"] == None:
                expns = Expenses.objects.filter(date_sales__range=[info["date_start"], info["date_end"]])
                print('obj expns', expns)
            else:
                expns = Expenses.objects.filter(date_sales__range=[info["date_start"], info["date_end"]],
                                                article=info["article"])
                print(expns)
            for exp in expns:
                sum_expenses += exp.product_price * exp.product_count
            print('exp is ', sum_expenses)


            if info['taxation_system'] == 'income usn6':
                total_tax = sum_income * 0.06
                total = sum_income - sum_expenses - total_tax
                print(total)

            elif info['taxation_system'] == 'income-expenses usn15':
                total_tax = (sum_income - sum_expenses) * 0.15
                total = sum_income - sum_expenses - total_tax
                print(total)

            elif info['taxation_system'] == 'ENVD':
                total_tax = sum_income * 0.15
                total = sum_income - sum_expenses - total_tax
                print(total)

            elif info['taxation_system'] == 'PSN':
                base = info["base_rate"]
                total_tax = base * 0.06
                total = sum_income - sum_expenses - total_tax
                print(total)

            new_income = AccInfo.objects.create(
                bis_reg_form=info["bis_reg_form"],
                taxation_system=info["taxation_system"],
                article=info["article"],
                date_start=info["date_start"],
                date_end=info["date_end"],
                profit=total
            )

            if info["article"] != None:
                resp = {
                    "profit": total,
                    "data_start": info["data_start"],
                    "date_end": info["date_end"],
                    "total_tax": total_tax,
                    "article": info["article"]
                }
            else:
                resp = {
                    "profit": total,
                    "date_start": info["date_start"],
                    "date_end": info["date_end"],
                    "total_tax": total_tax
                }

        return JsonResponse(resp)










