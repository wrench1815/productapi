from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination

from . import models
from . import serializers


class CustomResultPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class AmazonMobileViewSet(viewsets.ReadOnlyModelViewSet):
    '''
        Route for Amazon Mobiles

        Filters Available: upcoming, -upcoming, out_of_stock, -out_of_stock
        Keyword: availability
        Usage: ?availability=<filter> eg; ?availability=upcoming or ?availability=-upcoming
        
        Sorting available: default(id), price, -price
        Keyword: ordering
        Usage: ?ordering=<keyword> eg; ?ordering=price or ?ordering=-price
        Note: default filter works when there is no keyword

        Searching Avaialble: name, os, network, ram
        Keyword: search, os, network, ram
        Usage: ?search=<keyword> eg; ?search=samsung
        Note: the search is Fuzzy Case Insensitive

        Filter by additional pramas: brand, price(range), vendor
            brand
            Keyword: brand
            Usage: ?brand=<brand_id> eg: ? brand=1
            price(range)
            Keyword: price_start, price_end
            Usage: ?price_start=<start_range>&price_end=<end_range> eg: ?price_start=100&price_end=500
            vendor
            Keyword: vendor
            Usage: ?price_start=<vendor_id> eg: ?vendor=1

        Pagination: Active
        Keyword: page_size, page
        Usage: ?page_size=<number>&page=<number> eg; ?page_size=10&page=2
        Note: Page size refers to numbers of items per page and Page refers to the page number

        Result Format: {'count': <number>, 'next': <url>, 'previous': <url>, 'results': <list>}
        Note: count refers to the total number of result items, next and previous refer to the next and previous pages respectively and results refers to the list of results

    '''
    queryset = models.Mobile.objects.all()
    serializer_class = serializers.AmazonMobileSerializer
    pagination_class = CustomResultPagination
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['price']
    ordering = ['-id']
    search_fields = ['name']

    def get_queryset(self):
        '''
            Custom Queryset for Filters
        '''
        queryset = super().get_queryset()

        # get brand from query parameters
        q_brand = self.request.query_params.get('brand')

        # get availablity from query parameters
        q_av = str(self.request.query_params.get('availability')).lower()

        # get price_start from query parameters
        q_price_start = self.request.query_params.get('price_start')

        # get price_end from query parameters
        q_price_end = self.request.query_params.get('price_end')

        # get price_end from query parameters
        q_vendor = self.request.query_params.get('vendor')

        # get os from query parameters
        q_os = self.request.query_params.get('os')

        # get network from query parameters
        q_network = self.request.query_params.get('network')

        # get ram from query parameters
        q_ram = self.request.query_params.get('ram')

        if q_brand and q_av:
            queryset = queryset.filter(brand__id=int(q_brand))

            # Return only the mobiles that are upcoming
            if q_av == 'upcoming':
                queryset = queryset.filter(availability__upcoming=True)

            # Return only the mobiles that are not upcoming
            elif q_av == '-upcoming':
                queryset = queryset.filter(availability__upcoming=False)

            # Return only the mobiles that are out of stock
            elif q_av == 'out_of_stock':
                queryset = queryset.filter(availability__out_of_stock=True)

            # Return only the mobiles that are not out of stock
            elif q_av == '-out_of_stock':
                queryset = queryset.filter(availability__out_of_stock=False)

        elif q_os:
            # perform case insensitive search if 'q_os' contains in field
            queryset = queryset.filter(specifications__os__os__icontains=q_os)

        elif q_network:
            # perform case insensitive search if 'q_network' contains in field
            queryset = queryset.filter(
                specifications__general__network__icontains=q_network)

        elif q_ram:
            # perform case insensitive search if 'q_ram' contains in field
            queryset = queryset.filter(
                specifications__memory__ram__icontains=q_ram)

        # if price_start and price_end are passed in query params
        elif q_price_start and q_price_end:
            queryset = queryset.filter(price__range=(int(q_price_start),
                                                     int(q_price_end)))
        # if vendor is passed in query params
        elif q_vendor:
            queryset = queryset.filter(vendor__id=int(q_vendor))

            # Return only the mobiles that are upcoming
            if q_av == 'upcoming':
                queryset = queryset.filter(availability__upcoming=True)

            # Return only the mobiles that are not upcoming
            elif q_av == '-upcoming':
                queryset = queryset.filter(availability__upcoming=False)

            # Return only the mobiles that are out of stock
            elif q_av == 'out_of_stock':
                queryset = queryset.filter(availability__out_of_stock=True)

            # Return only the mobiles that are not out of stock
            elif q_av == '-out_of_stock':
                queryset = queryset.filter(availability__out_of_stock=False)

        else:
            # Return only the mobiles that are upcoming
            if q_av == 'upcoming':
                queryset = queryset.filter(availability__upcoming=True)

            # Return only the mobiles that are not upcoming
            elif q_av == '-upcoming':
                queryset = queryset.filter(availability__upcoming=False)

            # Return only the mobiles that are out of stock
            elif q_av == 'out_of_stock':
                queryset = queryset.filter(availability__out_of_stock=True)

            # Return only the mobiles that are not out of stock
            elif q_av == '-out_of_stock':
                queryset = queryset.filter(availability__out_of_stock=False)

        return queryset


class AmazonBrandViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Brand.objects.all()
    serializer_class = serializers.AmazonBrandSerializer


class AmazonVendorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Vendor.objects.all()
    serializer_class = serializers.AmazonVendorSerializer
