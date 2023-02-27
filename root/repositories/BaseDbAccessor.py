

class BaseDbAccessor:
    def __init__(self):
        self.limit = 10
        self.offset = 0
    
    def do_pagination(self, queryset, request):
        limit = int(request.get('limit', self.limit))
        offset = int(request.get('offset', self.offset))

        pass

