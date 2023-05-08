import openpyxl
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from catalogue.models import Product
from warehouse.models import WarehouseItem
from warehouse.serializers import WarehouseItemSerializer


class WarehouseItemViewSet(viewsets.ModelViewSet):
    queryset = WarehouseItem.objects.all()
    serializer_class = WarehouseItemSerializer

    @action(detail=False, methods=["post"])
    def load_items(self, request):
        excel_file = request.FILES.get("file")
        if not excel_file:
            return Response("No file uploaded", status=status.HTTP_400_BAD_REQUEST)
        iterated_rows = 1
        try:
            wb = openpyxl.load_workbook(excel_file)
            ws = wb.active
            data = []
            for row in ws.iter_rows(min_row=2, values_only=True):
                article, quantity, income_price, sale_price = row
                data.append({
                    "article": article,
                    "quantity": quantity,
                    "income_price": income_price,
                    "sale_price": sale_price,
                    "product": Product.objects.get(article=article)
                })
                iterated_rows += 1
            for item in data:
                instance = WarehouseItem(**item)
                instance.save()
            return Response(status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(f"{str(e)} row {iterated_rows}", status=status.HTTP_400_BAD_REQUEST)
