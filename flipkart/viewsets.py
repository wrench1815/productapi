from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination

from . import models
from . import serializers


class CustomResultPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class FlipkartMobileViewSet(viewsets.ReadOnlyModelViewSet):
    '''
        Route for Flipkart Mobiles

        Filters Available: upcoming, -upcoming, out_of_stock, -out_of_stock
        Keyword: availability
        Usage: ?availability=<filter> eg; ?availability=upcoming or ?availability=-upcoming
        
        Sorting available: default(id), price, -price
        Keyword: ordering
        Usage: ?ordering=<keyword> eg; ?ordering=price or ?ordering=-price
        Note: default filter works when there is no keyword

        Searching Avaialble: name
        Keyword: search
        Usage: ?search=<keyword> eg; ?search=samsung

        Pagination: Active
        Keyword: page_size, page
        Usage: ?page_size=<number>&page=<number> eg; ?page_size=10&page=2
        Note: Page size refers to numbers of items per page and Page refers to the page number

        Result Format: {'count': <number>, 'next': <url>, 'previous': <url>, 'results': <list>}
        Note: count refers to the total number of result items, next and previous refer to the next and previous pages respectively and results refers to the list of results

    '''
    queryset = models.Mobile.objects.all()
    serializer_class = serializers.FlipkartMobileSerializer
    pagination_class = CustomResultPagination
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['price']
    ordering = ['-id']
    search_fields = ['name']

    def get_queryset(self):
        '''
            Custom Queryset for Filters

            Note: only one filter can be called at a time
        '''
        queryset = super().get_queryset()

        av = str(self.request.query_params.get('availability')).lower()

        # Return only the mobiles that are upcoming
        if av == 'upcoming':
            queryset = queryset.filter(availability__upcoming=True)

        # Return only the mobiles that are not upcoming
        elif av == '-upcoming':
            queryset = queryset.filter(availability__upcoming=False)

        # Return only the mobiles that are out of stock
        elif av == 'out_of_stock':
            queryset = queryset.filter(availability__out_of_stock=True)

        # Return only the mobiles that are not out of stock
        elif av == '-out_of_stock':
            queryset = queryset.filter(availability__out_of_stock=False)

        return queryset


class FlipkartBrandViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Brand.objects.all()
    serializer_class = serializers.FlipkartBrandSerializer


class FlipkartVendorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Vendor.objects.all()
    serializer_class = serializers.FlipkartVendorSerializer
