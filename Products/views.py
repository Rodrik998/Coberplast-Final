from django.shortcuts import render

from Products.models import products
from rest_framework import generics, status
from rest_framework.response import Response

import pandas as pd

from tablib import Dataset

from Products.admin import ProductResource, CategoryResource


def simple_upload(request):
    if request.method == 'POST':
        product_resource = ProductResource()
        dataset = Dataset()
        new_product = request.FILES['Productos_Coberplast']

        imported_data = dataset.load(new_product.read())
        result = product_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            product_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'Templates/index.html')



# class ImportProductsData(generics.GenericAPIView):
#     parser_classes = [parsers.MultiPartParser]

#     def post(self, request, *args, **kwargs):
#         file = request.FILES['excel']
#         df = pd.read_excel(file)
        
#         """Rename the headeers in the excel file
#         to match Django models fields"""
        
#         rename_columns = {"Student Email": "email", "Student Name": "name",\
#                             "Roll Number": "roll_no", "Year": "year"}
        
#         df.rename(columns = rename_columns, inplace=True)
        
#         #Call the Student Resource Model and make its instance
#         student_resource = StudentResource()
        
#         # Load the pandas dataframe into a tablib dataset
#         dataset = Dataset().load(df)
        
#         # Call the import_data hook and pass the tablib dataset
#         result = student_resource.import_data(dataset,\
#             dry_run=True, raise_errors = True)

#         if not result.has_errors():
#             result = studentform_resource.import_data(dataset, dry_run=False)
#             return Response({"status": "Student Data Imported Successfully"})

#         return Response({"status": "Not Imported Student Data"},\
#                 status=status.HTTP_400_BAD_REQUEST)